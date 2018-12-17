from queue import Queue, LifoQueue
import utils.tuple as tupleutil
from PIL import Image

class Scan:

    well = (500,0)
    clay = set()
    touched = set()
    water = set()

    def __init__(self, lines):
        for line in lines:
            parts = line.split(", ")

            xs = []
            ys = []

            for part in parts:
                list = xs
                if part.startswith("y"):
                    list = ys

                numbers = part[2:]
                if ".." in numbers:
                    numberParts = numbers.split("..")
                    for n in range(int(numberParts[0]), int(numberParts[1])+1):
                        list.append(n)
                else:
                    list.append(int(numbers))

            for x in xs:
                for y in ys:
                    self.clay.add((x,y))

        self.minY = min(y for _,y in self.clay)
        self.maxY = max(y for _,y in self.clay)

        print(f"Scan complete, found {len(self.clay)} clay squares.")
        print(f"With a Y range of {self.minY}..{self.maxY}")

    def run(self):
        waterBefore, touchedBefore = -1, -1
        drips = 0
        while len(self.water) > waterBefore or len(self.touched) > touchedBefore:
            waterBefore = len(self.water)
            touchedBefore = len(self.touched)
            self.drip()
            drips += 1
            print(f"\rDripped {drips} drips.", end="")

            if drips % 1000 == 0:
                self.writeImage()

        print()
        print("Done!")
        self.print()

        return len(self.touched) - 1

    def drip(self):
        todo = LifoQueue()
        todo.put(self.well)
        passed = set()
        while not todo.empty():
            block = todo.get()
            if block[1] > self.maxY:
                continue
            if block in self.clay or block in passed or block in self.water:
                continue

            self.touched.add(block)
            passed.add(block)
            below = tupleutil.add(block, (0,1))
            if not self.canSupport(below):
                todo.put(below)
            else:
                left = tupleutil.add(block, (-1,0))
                right = tupleutil.add(block, (1,0))
                if (self.canSupport(left) and (right in passed or self.canSupport(left))) or (self.canSupport(right) and (left in passed or self.canSupport(right))):
                    if self.borderedLeft(block) and self.borderedRight(block):
                        self.water.add(block)
                        break
                todo.put(left)
                todo.put(right)

    def borderedLeft(self, block):
        return self.bordered(block, -1)

    def borderedRight(self, block):
        return self.bordered(block,  1)

    def bordered(self, block, direction):
        while True:
            if self.canSupport(block):
                return True
            below = tupleutil.add(block, (0,1))
            if not self.canSupport(below):
                return False
            block = tupleutil.add(block, (direction, 0))

    def print(self, block=None):
        print(self, block)

    def __str__(self, block=None):
        minXs = [min(x for x,_ in self.clay)]
        if len(self.touched) > 0:
            minXs.append(min(x for x,_ in self.touched))
        minX = min(minXs)
        maxXs = [max(x for x,_ in self.clay)]
        if len(self.touched) > 0:
            maxXs.append(max(x for x,_ in self.touched))
        maxX = max(maxXs)

        string = ""

        for y in range(self.maxY+1):
            for x in range(minX, maxX+1):
                p = (x,y)
                if p == block:
                    string += "@"
                elif p in self.clay:
                    string += "#"
                elif p == self.well:
                    string += "+"
                elif p in self.water:
                    string += "~"
                elif p in self.touched:
                    string += "|"
                else:
                    string += "."
            string += "\n"

        return string

    def writeImage(self):
        colorMap = {
            "@": (255,0,0),
            "#": (255,255,255),
            "+": (100,255,100),
            "~": (50,50,255),
            ".": (200,200,50),
            "|": (100,100,100)
        }
        colors = []
        width = 0
        height = len(self.__str__().splitlines())
        for line in self.__str__().splitlines():
            width = len(line)
            colors += [colorMap[c] for c in line]

        image = Image.new("RGB", (width, height))
        image.putdata(colors)
        image.save(f"ground-{len(self.water)}.png")

    def canSupport(self, block):
        return block in self.clay or block in self.water
