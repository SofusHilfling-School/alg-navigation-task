graph = dict()

def addEdge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append(node2)
    graph[node2].append(node1) # for undirected graph