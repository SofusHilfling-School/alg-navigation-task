from graph import Graph


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
    marked(self, v: int) -> bool
        function that checks wether node has been visited or not
    """
    __marked: dict[int, bool]
    count: int

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
        # sets all nodes in a graph to be unvisited, we haven't visited any nodes and we need to know which we havn't been to
        self.__marked = {key: False for key in g.nodes.keys()}
        # counter for number of nodes algorithm has been through, we need the shortest one
        self.count = 0
        self.__dfs(g, start)

    def __dfs(self, g: Graph, v: int) -> None:
        # sets node v to true, we have now visited it
        self.__marked[v] = True
        # counter goes up by 1
        self.count += 1
        # goes through the edges that node v has
        for w in g.edges[v]:
            # if we havn't been at one of the edges v has then go to that node and start over
            if not self.__marked[w.to_node]:
                self.__dfs(g, w.to_node)

    #checks if node v has been visited
    def marked(self, v: int) -> bool:
        return self.__marked[v]
