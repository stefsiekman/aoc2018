import utils.runner as runner

class Cart:
    def __init__(self, char, position):
        self.intersections = 0

        dirDict = {
            ">": (-1,0),
            "<": (1,0),
            "^": (0,1),
            "v": (0,-1)
        }

        self.lastPosition = addTuples(position, dirDict[char])


    def choose(self, options):
        chosen = options[self.intersections % 3]
        self.intersections += 1
        return chosen

    def move(self, position, char):
        newPosition = nextPosition(char, self, self.lastPosition, position)
        self.lastPosition = position
        return newPosition

def nextPosition(char, cart, lastPosition, currentPosition):
    fromDirection = tuple(z[0] - z[1] for z in zip(lastPosition, currentPosition))
    directions = nexts(char, fromDirection)

    # If there was a single possible direction, we can simply add
    if type(directions) == tuple:
        return addTuples(directions, currentPosition)
    else:
        return addTuples(cart.choose(directions), currentPosition)

def addTuples(a, b):
    return tuple(z[0] + z[1] for z in zip(a, b))


def nexts(char, frm):
    if char == "+":
        # Order all directions in order Left - Straight - Right
        allDirections = [(0,-1), (1,0), (0,1), (-1,0)]
        skipped = []
        for index, dir in enumerate(allDirections):
            if dir == frm:
                return allDirections[index+1:] + skipped
            else:
                skipped.append(dir)
        print("Failed to return")
        exit()

    elif char == "|" or char == "-":
        return tuple(-a for a in frm)

    elif char == "/":
        if frm == (-1,0):
            return (0,-1)
        elif frm == (0,-1):
            return (-1,0)
        elif frm == (0,1):
            return (1,0)
        elif frm == (1,0):
            return (0,1)
        print("Invalid direction:", frm)
        exit()

    elif char == "\\":
        if frm == (-1,0): # from left
            return (0,1)
        elif frm == (0,1): # from bottom
            return (-1,0)
        elif frm == (0,-1): # from top
            return (1,0)
        elif frm == (1,0): # from right
            return (0,-1)
        print("Invalid direction:", frm)
        exit()

    print("Invalid char:", char)
    exit()

class Board:

    def __init__(self, lines):
        self.width = max([len(l) for l in lines])
        self.height = len(lines)

        self.tiles = [[None] * self.width for _ in range(self.height)]

        print("Creating board")
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char in ["+", "-", "|", "/", "\\"]:
                    self.tiles[y][x] = (char, None)
                elif char in [">", "<"]:
                    self.tiles[y][x] = ("-", Cart(char, (x,y)))
                elif char in ["^", "v"]:
                    self.tiles[y][x] = ("|", Cart(char, (x,y)))

    def tick(self):
        moved = set()
        collision = None
        for y, line in enumerate(self.tiles):
            for x, tile in enumerate(line):
                # printChar = " " if tile == None else tile[0]
                if tile == None:
                    # print(printChar, end="")
                    continue
                if tile[1] == None or tile[1] in moved:
                    # print(tile[0], end="")
                    continue
                # print("#", end="")

                if collision:
                    continue

                # Move the cart
                cart = tile[1]
                newPosition = cart.move((x,y), tile[0])

                # Check for collisions
                if self.tiles[newPosition[1]][newPosition[0]][1] != None:
                    collision = f"{newPosition[0]},{newPosition[1]}"

                self.tiles[y][x] = (tile[0], None)
                newX, newY = newPosition
                self.tiles[newY][newX] = (self.tiles[newY][newX][0], cart)
                moved.add(cart)
            # print("")

        return collision

def solve(lines):
    board = Board(lines)
    while True:
        result = board.tick()
        if result != None:
            return result

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
