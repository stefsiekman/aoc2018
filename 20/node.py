import utils


directionToOffset = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}


class Node:
    north = None
    east = None
    south = None
    west = None

    def __init__(self, pos=(0, 0)):
        self.pos = pos

    def add_node(self, char, nodes):
        new_pos = utils.tuple_add(self.pos, directionToOffset[char])

        if new_pos in nodes:
            new_node = nodes[new_pos]
        else:
            new_node = Node(new_pos)

        if char == "N":
            self.north = new_node
            new_node.south = self
        elif char == "E":
            self.east = new_node
            new_node.west = self
        elif char == "S":
            self.south = new_node
            new_node.north = self
        elif char == "W":
            self.west = new_node
            new_node.east = self

        new_node.add_to(nodes)

        return new_node

    def existing_neighbours(self):
        return [n for n in [self.north, self.east, self.south, self.west] if n]

    def add_to(self, nodes):
        nodes[self.pos] = self
