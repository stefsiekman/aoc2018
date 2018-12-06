def closest(locations, tile):
    distances = [abs(tile[0] - l[0]) + abs(tile[1] - l[1]) for l in locations]
    return sum(distances)

def solve(lines):
    locations = [(int(line.split(", ")[0]), int(line.split(", ")[1]))
                 for line in lines]

    grid = [-1] * (400 * 400)
    amount = {}

    for tile in [(x, y) for x in range(0,400) for y in range(0,400)]:
        clos = closest(locations, tile)
        grid[tile[0] + tile[1] * 400] = clos

    n = 0
    for g in grid:
        if g < 10000:
            n += 1
        else:
            print("not 10000")

    print(n)



with open("input.txt", "r") as file:
    solve(file.read().splitlines())
