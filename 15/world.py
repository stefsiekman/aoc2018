from entity import Entity

class World:

    def __init__(self, lines):
        # Get the dimensions
        self.width = len(lines[0]) - 2
        self.height = len(lines) - 2
        print(f"Reading world of {self.width}x{self.height}...")

        # Init the tiles to all empty
        self.tiles = [[False] * self.width for _ in range(self.height)]

        # List of entities
        self.entities = []

        # Start processing the tiles
        for y, line in enumerate(lines[1:-1]):
            for x, char in enumerate(line[1:-1]):
                if char == "#":
                    self.tiles[y][x] = True
                elif char in ["G", "E"]:
                    self.entities.append(Entity(self, (x,y), char))

        # Report some stats
        self.elves = len([e for e in self.entities if e.elf])
        self.goblins = len([e for e in self.entities if not e.elf])
        print(f"Found {self.elves} elves and {self.goblins} goblins.")

    def round(self):
        # Give all the entities a turn in reading order
        self.sortEntities()
        for entity in self.entities:
            # Terminate the game if an entities says someone's won
            if not entity.turn():
                return False

        # Indicate that we need to play another round
        return False

    def sortEntities(self):
        self.entities.sort()

    def nonWallPositions(self, positions):
        """Return all the positions in a list that are not in a wall"""
        return [pos for pos in positions
            if  pos[0] >= 0 and pos[0] < self.width  # X in range of world
            and pos[1] >= 0 and pos[1] < self.height # Y in range of world
            and not self.tiles[pos[1]][pos[0]]]      # Tile is not a wall

    def entityAt(self, position):
        """Find the entity, if any, that is at a given position"""
        for entity in self.entities:
            if entity.pos == position:
                return entity

    def entitiesAt(self, positions):
        """Find the entities, if any, that are at given positions"""
        return [e for e in
            [self.entityAt(pos) for pos in positions] # Find entity at position
            if e] # Remove any Nones that were found

    def removeEntity(self, entity):
        """Removes an entity from the world"""
        # Double check it has dies
        assert entity.hp <= 0, f"Tried to remove {entity}"

        # Remove from the central list
        self.entities.remove(entity)

        # Decrement the entity counters
        if entity.elf:
            self.elves -= 1
        else:
            self.goblins -= 1
