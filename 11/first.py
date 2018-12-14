import utils.runner as runner

mem = {}

def power(serial, x, y):
    if len(mem) >= (300*300) or (x, y) in mem:
        return mem[(x,y)]

    rack = x + 10
    power = rack * y
    power += serial
    power *= rack
    power = int(power / 100) % 10
    power -= 5

    mem[(x,y)] = power

    return power

def value(serial, xs, ys, size):
    sum = 0
    for x in range(xs, min(xs+size, 301)):
        for y in range(ys, min(301, ys+size)):
            sum += power(serial, x, y)

    return sum

def solve(serial):
    maxS = 0
    maxPos = (0,0,0)
    for size in range(1, 100):
        for x in range(1,298+1):
            for y in range(1, 299):
                val = value(serial, x, y, size)
                if val > maxS:
                    maxS = val
                    maxPos=(x,y,size)
        print(f"done size {size} {maxPos} {maxS}")

    return f"{maxPos[0]},{maxPos[1]},{maxPos[2]}"


if __name__ == "__main__":
    result = solve(int(runner.start()))
    runner.done(result)
