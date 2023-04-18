
import click
from dfs import DepthFirstSearch
from dijkstra import Dijkstra
from graph import Graph

@click.command()
@click.option('-a', '--algorithm', default='dijkstra', help='set the algorithm to use when pathing. Valid inputs are "dijkstra" or "dfs"')
@click.option('-n', '--noprompt', is_flag=True, help='prints the whole path without waiting for user input')
@click.option('-m', '--map', default=None, help='system path to map that will be used for navigation')
@click.option('--dev', default=False, is_flag=True)
@click.argument('start')
@click.argument('destination')
def navigate(algorithm: str, noprompt: bool, map: str | None, dev: bool, start: int, destination: int):
    
    start = int(start)
    destination = int(destination)

    if dev:
        print(f"log: parameters: algorithm={algorithm}, noprompt={noprompt}, map={map}, dev={dev}, start={start}, destination={destination}")

    graph = defaultGraph() if map == None else importGraph(map)
    if dev:
        print('log: graph')
        graph.printGraph()

    alg = DepthFirstSearch(graph, start) if algorithm == 'dfs' else Dijkstra(graph, start)
    if not alg.hasPathTo(destination):
        print(f"There is no path between '{start}' and '{destination}'")
        return

    path = alg.pathTo(destination)


    for step in range(len(path)):
        print(path.pop().to_node)
        if not noprompt:
            input('Press any key to continue...')
            print('\033[1A\033[K\r', end='')


    pass

def defaultGraph() -> Graph:
    edges: list[list[tuple[int, float]]] = [
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

    for i, adjs in enumerate(edges):
        for (adj, distance) in adjs:
            g.addEdge(i, adj, distance)

    return g


def importGraph(map: str) -> Graph:
    pass

if __name__ == '__main__':
    navigate()