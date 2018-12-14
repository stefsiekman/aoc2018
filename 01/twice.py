import sys

sys.setrecursionlimit(10000)

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value == self.value:
            return True

        # Check whether we should insert left or right
        if value < self.value:
            # Create new node, or add to existing
            if self.hasLeft():
                return self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            # Create new node, or add to existing
            if self.hasRight():
                return self.right.insert(value)
            else:
                self.right = Node(value)

        return False

    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None


def calcWith(lines):
    frequency = 0
    visited = 0
    minVisited = 0
    maxVisited = 0
    tree = Node(0)
    found = False

    while not found:
        for line in lines:
            operation = line[0]
            value = int(line[1:])

            if operation == "+":
                frequency += value
            elif operation == "-":
                frequency -= value
            else:
                print("Unknown operation encountered")

            alreadyThere = tree.insert(frequency)
            if alreadyThere:
                print("Found frequency at: %d" % frequency)
                found = True
                break

            visited += 1
            
            if frequency < minVisited:
                minVisited = frequency
            if frequency > maxVisited:
                maxVisited = frequency

            if visited % 10000 == 0:
                rangeVisited = maxVisited - minVisited
                percentageVisited = round(float(visited) / rangeVisited * 100)
                print("Visited %d of %d (%d%%) frequencies" % (visited, rangeVisited, percentageVisited))

    print("Final frequency: %d" % frequency)

with open("input.txt", "r") as inputFile:
    calcWith(inputFile.read().splitlines())
