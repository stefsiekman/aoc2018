class Edge:

    def __init__(self, line):
        partz = line.split(" must be finished before step ")
        lefts = partz[0].split(" ")
        rights = partz[1].split(" ")
        self.left = lefts[1]
        self.right = rights[0]

def solve(lines):
    edges = [Edge(line) for line in lines]
    nodes = [chr(c).upper() for c in range(ord('a'), ord('z') + 1)]
    graph = {}

    for node in nodes:
        graph[node] = []
        for edge in edges:
            if edge.right == node:
                graph[node].append(edge)

    nodesLeft = nodes[:]

    while len(nodesLeft) > 0:
        nextNode = nodesLeft[0]

        for node in graph:
            if len(graph[node]) == 0:
                nextNode = node
                break
        if not nextNode in graph:
            break

        for node in graph:
            for edge in graph[node]:
                if edge.left == nextNode:
                    graph[node] = [e for e in graph[node] if e != edge]

        del graph[nextNode]
        nextNodes = [n for n in nodesLeft if n != nextNode]
        print(nextNode, end="")

    print("")


with open("input.txt", "r") as file:
    solve(file.read().splitlines())
