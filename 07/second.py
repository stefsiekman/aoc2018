class Edge:

    def __init__(self, line):
        partz = line.split(" must be finished before step ")
        lefts = partz[0].split(" ")
        rights = partz[1].split(" ")
        self.left = lefts[1]
        self.right = rights[0]

def next(graph, nodesLeft, nodes):
    nextNode = nodesLeft[0]

    found = False
    for node in nodesLeft:
        if len(graph[node]) == 0:
            nextNode = node
            found = True
            break
    if not found:
        return None

    if not nextNode in graph:
        return None

    return nextNode

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

    workers = [None] * 5

    time = 0
    while True:
        for index, worker in enumerate(workers):
            if worker != None:
                if worker[1] <= time:
                    del graph[worker[0]]
                    nextNodes = [n for n in nodesLeft if n != worker[0]]
                    for node in graph:
                        for edge in graph[node]:
                            if edge.left == worker[0]:
                                graph[node] = [e for e in graph[node] if e != edge]

                    workers[index] = None

        for index, worker in enumerate(workers):
            if len(nodesLeft) < 1:
                break
            if worker == None:
                nextNode = next(graph, nodesLeft, nodes)
                if nextNode == None:
                    break
                workers[index]= (nextNode, time + ord(nextNode) - ord('A') + 61)
                nodesLeft = [n for n in nodesLeft if n != nextNode]

        if len(nodesLeft) < 1:
            break

        time += 1

    maxTime = 0
    for worker in workers:
        if worker != None:
            if worker[1] > maxTime:
                maxTime = worker[1]

    print(f"All tasks will be finished after {maxTime}")


with open("input.txt", "r") as file:
    solve(file.read().splitlines())
