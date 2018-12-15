import utils.tuple as tupleutil

class Entity:

    def __init__(self, world, pos, char):
        self.world = world
        self.pos = pos
        self.elf = char == "E"

        self.hp = 200
        self.attack = 3

    def turn(self):
        print(f"\nTurn of {self} -> ", end="")
        inRange = self.enemiesInRange()

        # Attack if possible
        if len(inRange) > 0:
            print("attack")
            # Return whether the game should end
            return self.fight(inRange[0])

        # Otherwise, the entity will move
        print("move")

        # Else, yay!
        return True

    def fight(self, other):
        """ Fight an entity, returns whether the game should end"""
        # Make sure we're attacking a different type fo entity
        assert self.elf != other.elf, f"{self} tried to attack {other}"

        # FIIGGHHTTT
        return not (other.damage(self.attack) and not self.hasEnemies())

    def damage(self, amount):
        """Deals damage to entity, handles dieing, return True iff died"""

        # Deal the damage
        self.hp -= amount

        print(f"    {self} was attacked")

        # Check if the entity has died
        if self.hp <= 0:
            print("    Died as a result")
            world.removeEntity(self)
            return True

        return False

    def positionsInRange(self):
        """Position tuples that are in attack range of this entity"""

        # List all the direction 'vectors'
        around = [(0,-1), (1,0), (0,1), (-1,0)]

        # Add these to the position to get a list of neighbours
        allAround = [tupleutil.add(self.pos, dir) for dir in around]

        # Check that these positions are not inside a wall
        return self.world.nonWallPositions(allAround)

    def enemiesInRange(self):
        """List of all the entities of a different type in range, sorted"""
        enemies = [e for e in self.entitiesInRange() if e.elf != self.elf]
        enemies.sort()
        return enemies

    def entitiesInRange(self):
        """List of the entities that are directly next to this entitiy"""
        return self.world.entitiesAt(self.positionsInRange())

    def hasEnemies(self):
        """Checks if there are still any enemies left to fight"""
        if self.elf:
            return self.world.goblins > 0
        else:
            return self.world.elves > 0

    def positionIndex(self):
        return self.pos[0] + self.world.width * self.pos[1]

    def __lt__(self, other):
        return self.positionIndex() < other.positionIndex()

    def __str__(self):
        type = "Elf" if self.elf else "Goblin"
        return f"{type}({self.pos}, hp={self.hp})"
