from queue import Queue
import utils.tuple as tupleutil

directionOffsetMap = {
    "N": (0,-1),
    "E": (1,0),
    "S": (0,1),
    "W": (-1,0)
}

class Node:

    north = None
    east  = None
    south = None
    west  = None

    def __init__(self, pos):
        self.pos = pos

    def addTo(self, nodes):
        nodes[self.pos] = self

    def addNode(self, nodes, d):
        newPos = tupleutil.add(self.pos, directionOffsetMap[d])
        newNode = None

        # Is there already a node at the new position?
        if newPos in nodes:
            newNode = nodes[newPos]
        else:
            newNode = Node(newPos)
            newNode.addTo(nodes)

        # Update the links between the nodes
        if d == "N":
            self.north = newNode
            newNode.south = self
        elif d == "E":
            self.east = newNode
            newNode.west = self
        elif d == "S":
            self.south = newNode
            newNode.north = self
        elif d == "W":
            self.west = newNode
            newNode.east = self

        return newNode

    def existingNeighbours(self):
        return [n for n in [self.north, self.east, self.south, self.west] if n]
