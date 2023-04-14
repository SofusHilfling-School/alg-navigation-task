
from dfs import DepthFirstSearch
from dijkstra import Dijkstra
from graph import Graph


graph: list[list[tuple[int, float]]] = [
    [(11, 2)],
    [(2, 2.5)],
    [(1, 2.5), (3, 2)],
    [(2, 2), (4, 1.5), (6, 3)],
    [(3, 1.5), (5, 2.5), (9, 7)],
    [(4, 2.5)],
    [(3, 3), (7, 1.5)],
    [(6, 1.5), (9, 5)],
    [(9, 3), (11, 4)],
    [(7, 5), (4, 7), (8, 3)],
    [(11, 2)], 
    [(8, 4), (0, 2)]
]


g = Graph()

for i, adjs in enumerate(graph):
    for (adj, distance) in adjs:
        g.addEdge(i, adj, distance)

dfs = DepthFirstSearch(g, 0)

print(f'count: {dfs.count}')
print(f'is marked?: {dfs.marked(10)}')

dijkstra = Dijkstra(g, 0)

## print path to 7 from 0
pathTo7 = dijkstra.pathTo(7)
for step in range(len(pathTo7)):
    print(pathTo7.pop().to_node)