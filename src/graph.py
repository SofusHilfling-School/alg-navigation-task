class Edge:
    to_node: int
    from_node: int
    distanceBetween: float

    def __init__(self, to_node, from_node) -> None:
        self.to_node = to_node
        self.from_node = from_node

class Node:
    pass

class Graph:
    edges: dict[int, list[Edge]]
    nodes: dict[int, Node]

    def __init__(self):
        self.edges = {}
        self.nodes = {}

    def addNode(self, key: int, node: Node = None) -> None:
        if key not in self.nodes:
            self.nodes[key] = node

    def addEdge(self, from_node: int, edge: Edge | int, distance: float = 0) -> None:
        if type(edge) is int:
            edge = Edge(edge, from_node)
        else:
            edge.from_node = from_node

        # set distance for edge
        edge.distanceBetween = distance

        if from_node not in self.nodes:
            self.addNode(from_node)
        if edge.to_node not in self.nodes:
            self.addNode(edge.to_node)

        if from_node not in self.edges:
            self.edges[from_node] = [edge]
        else:
            self.edges[from_node].append(edge)

    def printGraph(self):
        for source, edges in self.edges.items():
            destinations = [str(e.to_node) for e in edges]
            
            print(f"{source}-->{', '.join(destinations)}")