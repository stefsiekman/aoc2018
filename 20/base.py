from node import Node
from queue import Queue, LifoQueue

def splitSections(regex):
    depth = 0
    index = 1
    sectionStart = index
    sections = []
    while True:
        if regex[index] == "(":
            depth += 1
        if regex[index] == ")":
            depth -= 1
        if depth < 1:
            c = regex[index]
            if (c == "|" and depth == 0) or depth == -1:
                # Extract section
                sections.append(regex[sectionStart:index])
                sectionStart = index + 1
                pass

            if depth == -1:
                break


        index += 1
        assert index < len(regex), f"Index ({index}) is in regex range"

    return (sections, regex[index+1:])

indxMem = {}
def continueIndices(regex, start):
    indices = [start+1]

    if regex[start+1] == ")":
        return indices

    if start in indxMem:
        return indxMem[start]

    index = start
    depth = 0

    while True:
        index += 1
        char = regex[index]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == "|" and depth == 0:
            indices.append(index+1)

        if depth == -1:
            break

    indxMem[start] = indices
    return indices

conatMem = {}

def continueAt(regex, start):
    index = start

    if regex[start] == ")":
        return start + 1

    if start in conatMem:
        return conatMem[start]

    caught = []

    depth = 0
    while True:
        index += 1
        char = regex[index]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

        if char == "|" and depth == 0:
            caught.append(index)

        if depth == -1:
            break

    result = index + 1

    for c in caught:
        conatMem[c] = result

    conatMem[start] = result
    return result


class Base:

    nodes = {}

    def __init__(self, regex):
        self.root = Node((0,0))
        self.root.addTo(self.nodes)
        queue = LifoQueue()

        queue.put((self.root, 0))

        lastPrint = 0
        nrNodes = 0

        while not queue.empty():
            node, index = queue.get()

            if index >= len(regex):
                continue

            char = regex[index]

            # Directional movements from a node
            if char in ["N", "E", "S", "W"]:
                newNode, wasNew = node.addNode(self.nodes, char)
                if wasNew:
                    nrNodes += 1
                queue.put((newNode, index+1))

            # Process junctions
            elif char == "(":
                for newIndex in continueIndices(regex, index):
                    queue.put((node, newIndex))

            elif char in [")", "|"]:
                queue.put((node, continueAt(regex, index)))

            else:
                queue.put((node, index+1))

            if nrNodes != lastPrint:
                print(f"\rScanned {len(self.nodes)} nodes, {queue.qsize()} due", end="")
                lastPrint = nrNodes

        print(" Done!")

    def doors(self):
        visited = set()
        queue = Queue()
        queue.put((self.root, 0))

        maxDoors = 0

        while not queue.empty():
            node, doors = queue.get()

            if node in visited:
                continue
            visited.add(node)

            if doors > maxDoors:
                maxDoors = doors

            for n in node.existingNeighbours():
                queue.put((n, doors + 1))
            pass

        return maxDoors
