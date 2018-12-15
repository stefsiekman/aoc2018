from queue import Queue
from entity import Entity
import utils.tuple as tupleutil

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
        return [pos for pos in positions if not self.isWallPosition(pos)]

    def isWallPosition(self, pos):
        return pos[0] < 0 or pos[0] >= self.width \
            or pos[1] < 0 or pos[1] >= self.height \
            or self.tiles[pos[1]][pos[0]]


    def nonEntityPosition(self, positions):
        """Return all the positions in a list that are not taken by an entity"""
        return [pos for pos in positions if not self.entityAt(pos)]

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

    def enemyRanges(self, entity):
        """List of all positions that are in range of an enemy of the entity"""
        # Get all the enemies first
        enemies = self.enemies(entity)

        # List all the positions around them (in a set, duplicaties removed)
        unfilteredRanges = set()
        for e in enemies:
            for pos in e.positionsInRange():
                unfilteredRanges.add(pos)

        # Remove the positions that are taken by another entity
        return self.nonEntityPosition(unfilteredRanges)

    def enemies(self, entity):
        """List of all enemies of an entity"""
        return [e for e in self.entities if e.elf != entity.elf]

    def locationTowards(self, start, destinations):
        """
        Find a neighbouring location to start that moves to the closest
        destination
        """

        # Helping datastructures
        visited = set(start)
        todo = Queue()

        # Add the inital positions to explore
        for pos in tupleutil.around(start):
            if not self.isWallPosition(pos):
                # Put a node with itself as root
                todo.put((pos, pos))

        prints = 0

        while not todo.empty():
            # Get the next item to process
            pos, moveTo = todo.get() # moveTo is the origin direction return

            # Is it a wall?
            if self.isWallPosition(pos):
                # Nothing to do, dead end
                continue

            # Have we already been here?
            if pos in visited:
                # Nothing to do, again
                continue

            # Are we at a destination?
            if pos in destinations:
                # Return the original direction to move
                return moveTo

            # Add new locations to visit
            for newPos in tupleutil.around(pos):
                todo.put((newPos, moveTo))

            # Mark node as visited
            visited.add(pos)

        # No route was found
        return None
        # TODO: this can be removed, yay Python!

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
