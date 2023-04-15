from graph import Edge, Graph

from pq import IndexMinPrioityQueue

class Dijkstra:
    distTo: dict[int, float]
    edgeTo: dict[int, Edge]
    
    def __init__(self, g: Graph, start: int) -> None:
        'Find shortest path from start node to all other nodes in graph.'
        self.edgeTo = {v: None for v in g.nodes.keys()}
        self.distTo = {v:float('inf') for v in g.nodes.keys()}
        self.distTo[start] = 0

        pq = IndexMinPrioityQueue()
        pq.push(start, 0)
        while not pq.empty():
            # get lowest value in priority queue
            v = pq.pop()
            # loop through all nodes edges
            for e in g.edges[v]:
                # get the node that the edge is pointing to
                w = e.to_node
                # calculate new distance
                new_dist = self.distTo[v] + e.distanceBetween
                # check if the new distance is less than the old
                if self.distTo[w] > new_dist:
                    # update the distance between the two nodes
                    self.distTo[w] = new_dist
                    # set the the current edge as the shortest edge to the current node
                    self.edgeTo[w] = e
                    # add node to priority queue sorted based on distance
                    pq.push(w, new_dist)

    def hasPathTo(self, v: int) -> bool:
        'Checks whether a path between start node and node v exists.'
        return self.distTo[v] < float('inf')
    
    def pathTo(self, v: int) -> list[Edge] | None:
        'Return the shortest path between start node and node v.'
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e != None:
            path.append(e)
            e = self.edgeTo[e.from_node]
        return path

