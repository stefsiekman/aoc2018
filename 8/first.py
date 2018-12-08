import utils.runner as runner

def solveMiddle(nodes, numbers):
    if len(numbers) < 2:
        return (0, 0)

    print(f"Solving middle {numbers}")

    index = 0
    sum = 0
    print(f"{nodes} to go over")
    for n in range(nodes):
        newNodes = numbers[index]
        metas = numbers[index + 1]

        index += 2

        print(f"Nodes {n} has {newNodes} nodes and {metas} metas")

        if newNodes > 0:
            res = solveMiddle(newNodes, numbers[(index):])

            sum += res[1]
            index += res[0]

        for m in range(metas):
            sum += numbers[index]
            print(f"Adding meta {numbers[index]}")
            index += 1

    return (index, sum)


def solve(numbers):
    nodes = numbers[0]
    metas = numbers[1]

    print("calling")
    res = solveMiddle(nodes, numbers[2:])

    return res[1] + sum(numbers[len(numbers)-metas:])

if __name__ == "__main__":
    result = solve([int(n) for n in runner.start().split(" ")])
    runner.done(result)
