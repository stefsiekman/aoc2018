from node import Node
from queue import Queue

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

class Base:

    nodes = {}

    def __init__(self, regex):
        self.root = Node((0,0))
        self.root.addTo(self.nodes)
        queue = Queue()

        queue.put((self.root, regex))

        misses = 0

        while not queue.empty():
            node, regex = queue.get()

            # Skip if the regex is empty, nothing to explore
            if not regex:
                misses += 1
                continue

            # Directional movements from a node
            if regex[0] in ["N", "E", "S", "W"]:
                newNode = node.addNode(self.nodes, regex[0])
                queue.put((newNode, regex[1:]))

            # Process junctions
            elif regex[0] == "(":
                sections, after = splitSections(regex)

                for section in sections:
                    newRegex = section + after
                    if newRegex:
                        queue.put((node, newRegex))

            else:
                newRegex = regex[1:]
                if newRegex:
                    queue.put((node, regex[1:]))

            print(f"\rScanned {len(self.nodes)} nodes, misses is {misses}, queue size is {queue.qsize()}", end="")

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
