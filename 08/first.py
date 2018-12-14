import utils.runner as runner

class Node:

    def __init__(self, depth=0):
        self.depth = depth

    def process(self, numbers):
        self.childrenCount = numbers[0]
        self.metasCount = numbers[1]

        # Go through all the children
        offset = 2
        childrenLength = 0
        self.children = []
        for n in range(self.childrenCount):
            self.children.append(Node(self.depth+1))
            length = self.children[n].process(numbers[offset:])
            childrenLength += length
            offset += length


        # Find the list of metas
        metaBegin = 2 + childrenLength
        metaEnd = metaBegin + self.metasCount
        self.metas = numbers[metaBegin:metaEnd]

        # Return the length of this node in the numbers list
        return metaEnd

    def count(self):
        return sum([c.count() for c in self.children]) + sum(self.metas)

def solve(numbers):
    root = Node()
    root.process(numbers)
    return root.count()


if __name__ == "__main__":
    result = solve([int(n) for n in runner.start().split(" ")])
    runner.done(result)
