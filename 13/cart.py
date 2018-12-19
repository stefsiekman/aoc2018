import utils.tuple as tupleutil

charDirectionMap = {
    ">": 1,
    "v": 2,
    "<": 3,
    "^": 0
}

directionCharMap = ["^", ">", "v", "<"]

directionOffsetMap = [(-1,0), (0,1), (1,0), (0,-1)]

class Cart:

    intersections = 0

    def __init__(self, char):
        self.direction = charDirectionMap[char]

    def nextPos(self, current):
        return tupleutil.add(current, self.offset())

    def offset(self):
        d = self.direction
        assert d >= 0 and d <= 4, f"Direction ({d}) is in valid range"
        return directionOffsetMap[d]

    def isHorizontal(self):
        return self.direction in [1,3]

    def isVertical(self):
        return not self.isHorizontal()

    def turnIntersection(self):
        # Intersection turning starts with -1 (left)
        turnAmount = self.intersections % 3 - 1
        self.turn(turnAmount)
        self.intersections += 1

    def turnRight(self):
        self.turn(1)

    def turnLeft(self):
        self.turn(-1)

    def turn(self, direction):
        self.direction = (self.direction + direction) % 4

    def __str__(self):
        return directionCharMap[self.direction]
