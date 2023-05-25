import networkx as nx
from utilities.custom import render_graph
from utilities.data import edges, line_colours, pos
import time

# Draggable utility to reposition nodes
force_local_debug = False
try:
    from utilities.local.draggable import DraggableNodes
except ImportError:
    force_local_debug = False


def setup_graph():
    global g

    # Add nodes and edges to the graph
    for edge in edges:
        g.add_edge(edge['from'], edge['to'], color=line_colours[edge['line']], weight=edge['weight'])

    # If the force_local_debug flag is set, render the graph using the draggable nodes utility (for repositioning)
    if force_local_debug:
        plot = DraggableNodes(g, pos, edges, line_colours)
        plot.show()
    else:
        render_graph(g, edges, pos, line_colours)


def dist(start, end):
    """
    Abstraction of node distance.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :return: direct distance between start and end nodes. If the nodes are not connected, returns infinity.
    :rtype: float
    """

    if start == end:
        return 0
    try:
        return min(dist_dict[frozenset({start, end})])
    except KeyError:
        return float('inf')


def dijkstra(start, end):
    """
    Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :return: The shortest distance between two nodes along with the path.
    :rtype: dict[str, float | list[str]]
    """

    # set all nodes to infinity with no predecessor
    distance = {node: float('inf') for node in g.nodes()}
    predecessor = {node: None for node in g.nodes()}
    unexplored = list(g.nodes())

    distance[start] = 0

    while len(unexplored) > 0:
        min_node = min(unexplored, key=lambda node: distance[node])
        unexplored.remove(min_node)

        for neighbour in g.neighbors(min_node):
            current_dist = distance[min_node] + dist(min_node, neighbour)
            # a shorter path has been found to the neighbour -> relax value
            if current_dist < distance[neighbour]:
                distance[neighbour] = current_dist
                predecessor[neighbour] = min_node

    # reconstructs the path
    path = [end]
    while path[0] != start:
        path.insert(0, predecessor[path[0]])

    return {'cost': distance[end], 'path': path}


def held_karp(start, end, visit):
    """
    Held-Karp Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :param visit: set of nodes to visit
    :type visit: set[str]

    :return: The shortest distance path from the start to end node while visiting all nodes in the visit set.
    :rtype: dict[str, float | list[str]]
    """
    # make sure visit is a set
    if type(visit) is not set:
        print("Error: visit must be a set of nodes")
        return {'cost': float('inf'), 'path': None}
    # visit set being empty means direct distance, ∴ we can use Dijkstra's instead
    if len(visit) == 0:
        djk = dijkstra(start, end)
        return {'cost': djk['cost'], 'path': djk['path']}
    else:
        minimum = {'cost': float('inf')}
        for rand_node in visit:
            # divides larger path into smaller subpaths by going from start to any random node C while visiting
            # everything else in the visit set. This is then combined with djk from C to the end to get the full path.
            sub_path = held_karp(start, rand_node, visit.difference({rand_node}))
            djk = dijkstra(rand_node, end)
            cost = sub_path['cost'] + djk['cost']
            if cost < minimum['cost']:
                # the path is calculated by adding the final path from dijkstra's to the sub-path
                # the [1:] is used to remove the first node from dijkstra's as if not, the rand_node is duplicated
                minimum = {'cost': cost, 'path': sub_path['path'] + djk['path'][1:]}
        return minimum


if __name__ == "__main__":
    g = nx.Graph()
    setup_graph()

    # Create a dictionary of distances, similar to a distance matrix, but allowing for multiple edges between nodes
    dist_dict = {frozenset({edge['from'], edge['to']}): [] for edge in edges}
    for edge in edges:
        dist_dict[frozenset({edge['from'], edge['to']})].append(edge['weight'])

    home = 'Brandon Park'
    # visit_set = set(g.nodes()).difference({home})
    visit_set = {'Chadstone', 'Flinders Street', 'Glen Waverley', 'Caulfield', 'Melbourne Central', 'Mount Waverley', 'Oakleigh', 'Camberwell'}
    start_time = time.perf_counter()

    print(f"Let's say I have {len(visit_set)} friends, they live closest to the following nodes: {visit_set}")
    print(f"The following would be the fastest path to go from my house ({home}) to all my friends' and back:")
    print(held_karp(home, home, visit_set))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"\nIt took {elapsed_time:.4f} seconds to run.")

