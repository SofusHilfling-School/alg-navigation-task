graph = dict()


def addEdge(node1, node2, cost):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append((node2, int(cost)))


def main():
    nodes, edges = input().split()

    for _ in range(int(edges)):
        node1, node2, cost = input().split()
        addEdge(node1, node2, cost)

    for key, val in graph.items():
        print(f"{key}-->{val}")


if __name__=="__main__":
    main()