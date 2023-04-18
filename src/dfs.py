from graph import Edge, Graph

class DepthFirstSearch:
    """
    Class that represents depth first search for graph pathfinding
    
    Attributes
    ----------
    __marked : dict[int, bool]
        dictionary contains the nodes that has been visited
    count : int
        a counter that add up for each new node visited
    
    Functions
    ---------
    __dfs(self, g: Graph, v: int) -> None
        function that traverses through a graph
    
    pathTo(self, v: int) -> list[Edge] | None
    """
    edgeTo: dict[int, Edge]
    __marked: dict[int, bool]

    def __init__(self, g: Graph, start: int) -> None:
        """
        Constructor for the dfs algorithm
        Parameters
        ----------
        g
            a graph object
        start
            start position/node in the graph
        """
        # creates a dictionary of edges, we don't know the edges yet so they are set to none 
        self.edgeTo = {v: None for v in g.nodes.keys()} 
        # sets all nodes in a graph to be unvisited, we haven't visited any nodes and we need to know which we havn't been to
        self.__marked = {key: False for key in g.nodes.keys()}

        self.__dfs(g, start)

    def __dfs(self, g: Graph, v: int) -> None:
        # sets node v to true, we have now visited it
        self.__marked[v] = True
        # goes through the edges that node v has
        for w in g.edges[v]:
            # if we havn't been at one of the edges v has then go to that node and start over
            if not self.__marked[w.to_node]:
                self.edgeTo[w.to_node] = w
                self.__dfs(g, w.to_node)

    def hasPathTo(self, v: int) -> bool:
        'Return a boolean indicating whether there is a path between the start node and the node v'
        # If vertex has been marked we know there is a path between the start node and v
        return self.__marked[v]

    def pathTo(self, v: int) -> list[Edge] | None:
        'Return a list of edges representing the path between the start node and node v, the list is sorted based on the path from v to start'
        # Return none if there are no path between the start node and v
        if not self.hasPathTo(v):
            return None
        # a list of edges representing a path between the start node and v
        path: list[Edge] = []
        # set the initial edge to the one pointing to v
        e = self.edgeTo[v]
        while e != None:
            # add the edge pointing to the current node
            path.append(e)
            # change e to the node the edge is pointing from
            e = self.edgeTo[e.from_node]
        return path