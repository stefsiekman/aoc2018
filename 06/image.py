from PIL import Image

SIZE = 400

def closest(locations, tile):
    distances = [abs(tile[0] - l[0]) + abs(tile[1] - l[1]) for l in locations]

    minDist = min(distances)
    found = False
    minIndex = -1

    for index, dist in enumerate(distances):
        if dist == minDist:
            if not found:
                found = True
                minIndex = index
            else:
                return -1

    return minIndex

def solve(lines):
    locations = [(int(line.split(", ")[0]), int(line.split(", ")[1]))
                 for line in lines]

    grid = [-1] * (SIZE * SIZE)
    amount = {}

    print("Gathering data...")

    for tile in [(x, y) for x in range(0,SIZE) for y in range(0,SIZE)]:
        clos = closest(locations, tile)
        grid[tile[0] + tile[1] * SIZE] = clos

        if tile[0] == 0 or tile[0] >= SIZE-1 or tile[1] == 0 or tile[1] >= SIZE-1:
            amount[clos] = -1
        elif not clos in amount:
            amount[clos] = 0

        if amount[clos] >= 0:
            amount[clos] += 1
        elif amount[clos] != -1:
            amount[clos] = 1

    print("Creating image...")
    colors = [int(((g+1) * 5)) for g in grid]
    data = [(c,200,255) for c in colors]
    image = Image.new('HSV', (SIZE,SIZE), 'white')
    image.putdata(data)
    image.convert('RGB').save('map.png')
    image.show()


with open("input.txt", "r") as file:
    solve(file.read().splitlines())
