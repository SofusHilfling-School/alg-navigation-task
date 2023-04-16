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
        self.__marked = {key: False for key in g.nodes.keys()}
        self.count = 0
        self.__dfs(g, start)

    def __dfs(self, g: Graph, v: int) -> None:
        self.__marked[v] = True
        self.count += 1
        for w in g.edges[v]:
            if not self.__marked[w.to_node]:
                self.__dfs(g, w.to_node)

    def marked(self, v: int) -> bool:
        return self.__marked[v]
