from graph import Graph


class DepthFirstSearch:
    __marked: dict[int, bool]
    count: int

    def __init__(self, g: Graph, start: int) -> None:
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
