import utils.runner as runner

def toBools(list):
    return [False if l == "." else True for l in list]

def trimStart(pots):
    index = 0
    for pot in pots:
        if pot:
            return index
        else:
            index += 1

def trimEnd(pots):
    return trimStart(reversed(pots))

def solve(lines):
    pots = toBools(lines[0])
    rules = [(toBools(l[:5]), toBools(l[-1])[0]) for l in lines[2:]]

    startIndex = 0

    for day in range(1,1001):
        paddedPots = [False]*4 + pots + [False]*4
        startIndex -= 4
        newPots = [False] * len(paddedPots)

        # Find any matching patterns
        for rule in rules:
            for index in range(len(paddedPots) - 5):
                if rule[0] == paddedPots[index:index+5]:
                    newPots[index+2] = rule[1]

        startIndex += trimStart(newPots)
        pots = newPots[trimStart(newPots):len(newPots)-trimEnd(newPots)]

        str = "".join(["#" if p else "." for p in pots])
        print(f"{day}: {str}")

    sum = 0
    for index, pot in enumerate(pots):
        if pot:
            sum += index + startIndex

    return sum + 22 * (50000000000 - 1000)

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
