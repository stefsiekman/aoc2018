from node import Node
from queue import Queue


class Base:
    nodes = {}

    def __init__(self):
        self.root = Node()
        self.root.add_to(self.nodes)

    def parse(self, regex):
        stack = [self.root]
        last_node = self.root

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

            if node in visited:
                continue
            else:
                visited.add(node)

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
