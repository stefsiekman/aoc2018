from node import Node
from queue import Queue

<<<<<<< HEAD
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
=======
>>>>>>> f855424... Use much easier stack method

class Base:
    nodes = {}

<<<<<<< HEAD
    def __init__(self, regex):
        self.root = Node((0,0))
        self.root.addTo(self.nodes)
        queue = LifoQueue()

        queue.put((self.root, 0))
=======
    def __init__(self):
        self.root = Node()
        self.root.add_to(self.nodes)
>>>>>>> f855424... Use much easier stack method

    def parse(self, regex):
        stack = [self.root]
        last_node = self.root

<<<<<<< HEAD
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
=======
        for char in regex:
            if char in ["N", "E", "S", "W"]:
                new_node = last_node.add_node(char, self.nodes)
                last_node = new_node
            elif char == "|":
                last_node = stack[-1]
            elif char == ")":
                last_node = stack.pop()
            elif char == "(":
                stack.append(last_node)

        print(f"Parsed {len(self.nodes)} nodes.")

    def most_doors(self):
        visited = set()
        queue = Queue()
        queue.put((self.root, 0))

        max_doors = 0

        while not queue.empty():
            node, doors = queue.get()
>>>>>>> f855424... Use much easier stack method

            if node in visited:
                continue
            else:
<<<<<<< HEAD
                queue.put((node, index+1))
=======
                visited.add(node)
>>>>>>> f855424... Use much easier stack method

            if doors > max_doors:
                max_doors = doors

            for n in node.existing_neighbours():
                queue.put((n, doors + 1))
            pass

        return max_doors

    def far_rooms(self, min_distance=1000):
        visited = set()
        queue = Queue()
        queue.put((self.root, 0))

        fars = 0

        while not queue.empty():
            node, doors = queue.get()

            if node in visited:
                continue
            else:
                visited.add(node)

            if doors >= min_distance:
                fars += 1

            for n in node.existing_neighbours():
                queue.put((n, doors + 1))
            pass

        return fars

    def __str__(self):
        minX = min([self.nodes[n].pos[0] for n in self.nodes.keys()])
        minY = min([self.nodes[n].pos[1] for n in self.nodes.keys()])
        maxX = max([self.nodes[n].pos[0] for n in self.nodes.keys()])
        maxY = max([self.nodes[n].pos[1] for n in self.nodes.keys()])

        width = maxX - minX + 1
        height = maxY - minY + 1

        lines = [["#"] * width * 3 for _ in range(height * 3)]

        for y in range(height):
            for x in range(width):
                baseX = x + minX
                baseY = y + minY

                n = self.nodes[(baseX, baseY)]

                if n.pos in self.nodes:
                    lines[y * 3 + 1][x * 3 + 1] = " " if (baseX != 0 or baseY != 0) else "0"
                    if n.north:
                        lines[y * 3 + 0][x * 3 + 1] = " "
                    if n.east:
                        lines[y * 3 + 1][x * 3 + 2] = " "
                    if n.south:
                        lines[y * 3 + 2][x * 3 + 1] = " "
                    if n.west:
                        lines[y * 3 + 1][x * 3 + 0] = " "

        return "\n".join(["".join(l) for l in lines])
