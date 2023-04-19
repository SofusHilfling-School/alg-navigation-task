
import click
from dfs import DepthFirstSearch
from dijkstra import Dijkstra
from graph import Graph, Node


@click.command(no_args_is_help=True, context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-a', '--algorithm', default='dijkstra', help='set the algorithm to use when pathing. Valid inputs are "dijkstra" or "dfs"')
@click.option('-p', '--pathonly', is_flag=True, help='prints the whole path without waiting for user input')
@click.option('-m', '--map', default="map.txt", help='system path to map that will be used for navigation')
@click.option('--dev', default=False, is_flag=True)
@click.argument('start')
@click.argument('destination')
def navigate(algorithm: str, pathonly: bool, map: str | None, dev: bool, start: int | str, destination: int | str):
    'Navigate between two points on a map, start and destination must both be keys specified in the map'
    
    if dev:
        print(f"log: parameters: algorithm={algorithm}, pathonly={pathonly}, map={map}, dev={dev}, start={start}, destination={destination}")

    graph = importGraph(map)
    if dev:
        print('log: graph edges')
        graph.printGraph()

    startKey = parseNodeInput(graph, start)
    if startKey == None:
        print("Invalid value for START, either use the key or name for a valid node in the graph")
        return
    destinationKey = parseNodeInput(graph, destination)
    if destinationKey == None:
        print("Invalid value for DESTINATION, either use the key or name for a valid node in the graph")
        return

    alg = DepthFirstSearch(graph, startKey) if algorithm == 'dfs' else Dijkstra(graph, startKey)
    if not alg.hasPathTo(destinationKey):
        print(f"There is no path between '{start}' and '{destination}'")
        return

    path = alg.pathTo(destinationKey)
    if dev:
        print(f'log: path: {path}')

    total = 0
    for edge in path:
        total += edge.distance_between

    if pathonly:
        print(graph.nodes[startKey].name, end='')
        for step in range(len(path)):
            edge = path.pop()
            node = graph.nodes[edge.to_node]
            node_name = node.name if node.name != None else node.key
            print(f' -> {node_name}', end='')
        print()
        print(f"Total distance: {total}km")
    else:
        for step in range(len(path)):
            edge = path.pop()
            node = graph.nodes[edge.to_node]
            node_name = node.name if node.name != None else node.key

            if dev:
                print(f"log: {node}")
                print(f"log: {edge}")

            print(f"Continue towards '{node_name}' for {edge.distance_between}km", end=', ')
            print(f"{total}km until you arrive at destination")
            total -= edge.distance_between

            input('Press any key to continue...')
            print('\033[1A\033[K\r', end='')
        
        print(f"🎉 You have arrived at destination '{graph.nodes[destinationKey].name}' 🎉")

def importGraph(filePath: str) -> Graph:
    with open(filePath) as file:
        lines = file.readlines()
    
    g = Graph()
    for line in lines:
        fields = line.rstrip('\n').split(' ')

        number_of_inputs = len(fields)
        if number_of_inputs == 2 and fields[1] != '':
            g.addNode(Node(int(fields[0]), fields[1]))
        elif number_of_inputs == 3:
            g.addEdge(int(fields[0]), int(fields[1]), float(fields[2]))

    return g

def parseNodeInput(graph: Graph, input: str | int) -> int | None:
    try:
        return int(input)
         
    except ValueError as verr:
        pass # do job to handle: s does not contain anything convertible to int

    return graph.getKey(lambda n : n.name == input)


if __name__ == '__main__':
    navigate()