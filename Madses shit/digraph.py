graph = dict()

def addEdge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append(node2)


def main():
    print("How many nodes and edges?")
    nodes, edges = input().split()

    for _ in range(int(edges)):
        print("Which nodes are connected?")
        node1, node2 = input().split()
        addEdge(node1, node2)

    for key, val in graph.items():
        print(f"{key}-->{val}")


if __name__=="__main__":
    main()