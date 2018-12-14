import utils.runner as runner
import utils.progress as progress

class Marbel:

    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left if left != None else self
        self.right = right if right != None else self

    def add(self, number):
        toLeft = self.right
        toRight = self.right.right
        newMarbel = Marbel(number, toLeft, toRight)
        toLeft.right = newMarbel
        toRight.left = newMarbel
        return newMarbel

    def remove7Left(self):
        toRemove = self.left.left.left.left.left.left.left
        toLeft = toRemove.left
        toRight = toRemove.right
        toLeft.right = toRight
        toRight.left = toLeft

        return (toRemove.number, toRight)

def solve(lines):
    players    = int(lines[0])
    lastMarbel = int(lines[1])

    cPlayer = 1
    scores = [0] * players

    cMarbel = Marbel(0)

    progress.setup(lastMarbel)

    for marbel in range(1,lastMarbel+1):
        if marbel % 23 == 0:
            scores[cPlayer-1] += marbel
            res = cMarbel.remove7Left()
            scores[cPlayer-1] += res[0]
            cMarbel = res[1]

        else:
            cMarbel = cMarbel.add(marbel)

        cPlayer += 1
        if cPlayer > players:
            cPlayer = 1

        progress.done(marbel)

    progress.complete()

    return max(scores)


if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
