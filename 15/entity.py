import utils.tuple as tupleutil

class Entity:

    def __init__(self, world, pos, char):
        self.world = world
        self.pos = pos
        self.elf = char == "E"

        self.hp = 200
        self.attack = 3

    def turn(self):
        # print(f"\nTurn of {self} -> ", end="")
        inRange = self.enemiesInRange()

        # Attack if possible
        if len(inRange) > 0:
            # print(f"attack ({len(inRange)} in range)")
            # Return whether the game should end
            return self.fight(inRange)

        # Otherwise, the entity will move
        # print("move")

        # Get goals to move to
        destinations = self.world.enemyRanges(self)

        # Find what direction we will have to move to
        moveTo = self.world.locationTowards(self.pos, destinations)

        if moveTo:
            self.pos = moveTo
            inRange = self.enemiesInRange()

            # Attack if possible
            if len(inRange) > 0:
                # print(f"attack ({len(inRange)} in range)")
                # Return whether the game should end
                return self.fight(inRange)

        # We can continue the game
        return True

    def fight(self, others):
        """ Fight an entity, returns whether the game should end"""
        # Determine which entity is best to attack
        other = others[0]
        for o in others:
            if o.hp < other.hp:
                other = o

        # Make sure we're attacking a different type fo entity
        assert self.elf != other.elf, f"{self} tried to attack {other}"

        # FIIGGHHTTT
        return not (other.damage(self.attack) and not self.hasEnemies())

    def damage(self, amount):
        """Deals damage to entity, handles dieing, return True iff died"""

        # Deal the damage
        self.hp -= amount

        # Check if the entity has died
        if self.hp <= 0:
            self.world.removeEntity(self)
            return True

        return False

    def positionsInRange(self):
        """Position tuples that are in attack range of this entity"""
        # Check that all around positions are not inside a wall
        return self.world.nonWallPositions(tupleutil.around(self.pos))

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
        type = "E" if self.elf else "G"
        return f"{type}({self.pos}, hp={self.hp})"
