from graph import Edge, Graph

from pq import IndexMinPrioityQueue

class Dijkstra:
    """
    Class that represents Dijkstras algorithm for graph pathfinding
    
    Attributes
    ----------
    distTo : dict[int, float]
        dictionary contains the distance to a node
    edgeTo : dict[int, float]
        dictionary contains the edges to nodes
    
    Functions
    ---------
    hasPathTo(self, v: int) -> bool

    pathTo(self, v: int) -> list[Edge] | None
    """
    distTo: dict[int, float]
    edgeTo: dict[int, Edge]
    
    def __init__(self, g: Graph, start: int) -> None:
        """
        Parameters
        ----------
        g
            a graph object
        start
            start position/node in the graph
        """
        'Find shortest path from start node to all other nodes in graph.'
        # creates a dictionary of edges, we don't know the edges yet so they are set to none 
        self.edgeTo = {v: None for v in g.nodes.keys()}
        # creates a dictionary of distance(weight) for nodes and sets them to large value inf
        # we need this for comparison 
        self.distTo = {v:float('inf') for v in g.nodes.keys()}
        # distance to start node is 0 we can't get closer
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
                new_dist = self.distTo[v] + e.distance_between
                # check if the new distance is less than the old
                if self.distTo[w] > new_dist:
                    # update the distance between the two nodes
                    self.distTo[w] = new_dist
                    # set the the current edge as the shortest edge to the current node
                    self.edgeTo[w] = e
                    # add node to priority queue sorted based on distance
                    pq.push(w, new_dist)

    def hasPathTo(self, v: int) -> bool:
        #'Checks whether a path between start node and node v exists.'
        #If it doesn't exist we can't go that way
        return self.distTo[v] < float('inf')
    
    def pathTo(self, v: int) -> list[Edge] | None:
        'Return the shortest path between start node and node v.'
        #If to check if path exists if not it'll return none
        if not self.hasPathTo(v):
            return None
        #list of paths
        path = []
        # a nodes edge to target node v 
        e = self.edgeTo[v]
        while e != None:
            # putting the edge in the list of paths if there is a path
            path.append(e)
            # the edges from target node back to original node we are possibly not done with original node
            e = self.edgeTo[e.from_node]
        return path

