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

    grid = [-1] * (500 * 500)
    amount = {}

    for tile in [(x, y) for x in range(0,500) for y in range(0,500)]:
        clos = closest(locations, tile)
        grid[tile[0] + tile[1] * 500] = clos

        if tile[0] == 0 or tile[0] >= 499 or tile[1] == 0 or tile[1] >= 499:
            amount[clos] = -1
        elif not clos in amount:
            amount[clos] = 0

        if amount[clos] >= 0:
            amount[clos] += 1
        elif amount[clos] != -1:
            amount[clos] = 1

    maxAmount = 0
    for am in amount:
        num = amount[am]

        if num > maxAmount:
            maxAmount = num

    print(maxAmount)



with open("input.txt", "r") as file:
    solve(file.read().splitlines())
