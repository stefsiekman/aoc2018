import utils.runner as runner
from PIL import Image

class Star:

    def __init__(self, line):
        partsA = line.split("> velocity=<")
        partsB = partsA[0].split("<")
        poss = partsB[1].split(",")
        self.x = int(poss[0])
        self.y = int(poss[1])
        partsC = partsA[1].split(">")
        vels = partsC[0].split(",")
        self.dx = int(vels[0])
        self.dy = int(vels[1])

    def move(self):
        self.x += self.dx
        self.y += self.dy

def solve(lines):
    stars = [Star(n) for n in lines]

    minW = 10000000
    minH = 10000000

    for sec in range(1,1000000):
        for star in stars:
            star.move()

        minX = min([s.x for s in stars])
        maxX = max([s.x for s in stars])
        minY = min([s.y for s in stars])
        maxY = max([s.y for s in stars])
        w = maxX - minX + 1
        h = maxY - minY + 1

        if w < minW:
            minW = w
            print(f"\rw = {minW}, h = {minH}          ", end="")
        if h < minH:
            minH = h
            print(f"\rw = {minW}, h = {minH}          ", end="")

        if w > minW or h > minH:
            break

        if w > 100 or h > 50:
            continue

        sky = [0] * (w*h)

        for star in stars:
            sky[(star.x+(minX if minX <=0 else -minX)) + (star.y+(minY if minY <=0 else -minY)) * w] = 1

        image = Image.new("RGB", (w,h))
        data = [(c*255,c*255,c*255) for c in sky]
        image.putdata(data)
        image.save(f"sky-{sec}.png")

    print("")

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
