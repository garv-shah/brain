import datetime
import math
import random

import sys
import networkx as nx
from utilities.custom import render_graph
from utilities.data import edges, line_data, pos, node_lat_long, friend_data, time_data
import time
import datetime as dt
import heapq as hq

# Draggable utility to reposition nodes
force_local_debug = False
try:
    from utilities.local.draggable import DraggableNodes
except ImportError:
    force_local_debug = False


def lat_long_distance(coord1, coord2):
    # assign lat/long from coords
    lat1 = coord1[0]
    long1 = coord1[1]
    lat2 = coord2[0]
    long2 = coord2[1]

    # radius of earth
    r = 6371

    # equation definitions from haversine formula
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(long2 - long1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # distance in kilometers
    d = r * c

    return d


def calculate_nodes(node_data):
    distance_dict = {}
    for friend in friend_data:
        friend_home = friend_data[friend]['home']
        # initial min vals that will be set to smallest iterated distance
        min_dist = float('inf')
        closest_node = None

        for node in node_data:
            location = node_data[node]
            distance = lat_long_distance(friend_home, location)
            if distance < min_dist:
                min_dist = distance
                closest_node = node

        distance_dict[friend] = {}
        distance_dict[friend]['closest_node'] = closest_node
        distance_dict[friend]['distance'] = min_dist
    return distance_dict


def calculate_prices():
    zones = set()
    # add all traversed zones into a set to see which zones were visited
    for start, end in pairwise(hamiltonian_path['path']):
        line = edge_lookup_matrix[frozenset({start, end})][0]['line']
        zones.add(line_data[line]['zone'])

    money = 0

    # if it took us 2 hours or less
    if hamiltonian_path['cost'] <= 120:
        # 2 hour bracket
        if 1 in zones and 2 in zones:
            if concession:
                money = 2.30
            else:
                money = 4.60
        elif 2 in zones:
            # just zone 2
            if concession:
                money = 1.55
            else:
                money = 3.10
    else:
        # daily fare bracket
        if 1 in zones and 2 in zones:
            if concession:
                money = 4.60
            else:
                money = 9.20
        elif 2 in zones:
            # just zone 2
            if concession:
                money = 3.10
            else:
                money = 6.20

    # if it is a weekend or a holiday
    if holiday:
        if concession and money > 3.35:
            money = 3.35
        elif money > 6.70:
            money = 6.70

    return money


def setup_graph():
    global g

    # Add nodes and edges to the graph
    for edge in edges:
        g.add_edge(edge['from'], edge['to'], color=line_data[edge['line']]['colour'], weight=edge['weight'])

    # If the force_local_debug flag is set, render the graph using the draggable nodes utility (for repositioning)
    if force_local_debug:
        plot = DraggableNodes(g, pos, edges, line_data)
        plot.show()
    else:
        render_graph(g, edges, pos, line_data)


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def select_friend(question, default="Garv"):
    valid = [friend for friend in friend_data]
    line_count = 0

    while True:
        print(question)
        line_count += 1
        for i in range(len(valid)):
            print(f"{i + 1}. {valid[i]}")
            line_count += 1
        choice = input().lower()
        if default is not None and choice == "":
            return_val = default
            break
        elif choice.isdigit():
            if int(choice) in range(1, len(valid) + 1):
                return_val = valid[int(choice) - 1]
                break
            else:
                print(f"Please respond with a number between 1 and {len(valid)}.\n")
                line_count += 1
        else:
            print(f"Please respond with a number between 1 and {len(valid)}.\n")
            line_count += 1

    for i in range(line_count + 1):
        line_up = '\033[1A'
        line_clear = '\x1b[2K'
        print(line_up, end=line_clear)

    print(f"{question} {return_val}")
    return return_val


def pairwise(iterable):
    """s -> (s0, s1), (s2, s3), (s4, s5), ..."""
    a = iter(iterable)
    return zip(a, a)


def dist(start, end, current_time):
    """
    Abstraction of node distance.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :param current_time: the current time when the distance is being called
    :type current_time: dt.datetime

    :return: direct distance between start and end nodes. If the nodes are not connected, returns infinity.
    :rtype: float
    """

    # if the start and end node are the same, it takes no time to get there
    if start == end:
        return 0
    elif frozenset({start, end}) not in edge_lookup_matrix:
        # if no edge exists between nodes
        return float('inf')

    connecting_edges = edge_lookup_matrix[frozenset({start, end})]
    distances = []

    # go over each possible edge between nodes (multiple possible)
    for edge in connecting_edges:
        line = edge['line']

        distances.append(time_data[line][start][dt.datetime.strftime(current_time, "%H:%M")])

    return min(distances)


def dijkstra(start, current_time):
    """
    Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: The distance dictionary and the predecessor dictionary.
    :rtype: dict
    """

    # set all nodes to infinity with no predecessor
    distances = {}
    distance = {node: float('inf') for node in g.nodes()}
    predecessor = {}
    unexplored = []

    size = len(g.nodes())

    for node in list(g.nodes()):
        if node == start:
            unexplored.append((0, node))
        else:
            unexplored.append((float('inf'), node))

    hq.heapify(unexplored)

    distance[start] = 0
    distances[start] = 0

    while size > 0:
        min_node = hq.heappop(unexplored)
        node = min_node[1]
        node_dist = distance[node]
        size = size - 1

        for neighbour in g.neighbors(node):
            current_dist = node_dist + dist(node, neighbour, current_time + dt.timedelta(minutes=node_dist))
            # a shorter path has been found to the neighbour ∴ relax value
            if current_dist < distance[neighbour]:
                distances[neighbour] = current_dist
                distance[neighbour] = current_dist
                hq.heappush(unexplored, (current_dist, neighbour))
                predecessor[neighbour] = node

    return {'distances': distances, 'predecessors': predecessor}


def fetch_hk(start, end, visit, current_time):
    """
    Fetches Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :param visit: set of nodes to visit
    :type visit: set[str]

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: The shortest distance path from the start to end node while visiting all nodes in the visit set.
    :rtype: dict[str, float | list[str]]
    """

    name = f"{start}-{end}{visit}@{current_time}"

    global cached_hk
    if name not in cached_hk:
        cached_hk[name] = held_karp(start, end, visit, current_time)

    return cached_hk[name]


def fetch_djk(start, end, current_time, visit_set):
    """
    Fetches Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str | None

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :param visit_set: optional, the set of nodes to visit. only needed if end is None
    :type visit_set: set | None

    :return: The shortest distance between two nodes along with the path.
    :rtype: dict[str, float | list[str]]
    """

    name = f"{start}@{current_time}"

    global cached_djk
    if name not in cached_djk:
        cached_djk[name] = dijkstra(start, current_time)

    djk = cached_djk[name]
    distances = djk['distances']
    # reconstructs the path

    # if end doesn't exist, set end to the closest node
    if end is None:
        visit_distances = {key: distances[key] for key in visit_set}
        end = min(visit_distances, key=visit_distances.get)

    path = [end]
    while path[0] != start:
        path.insert(0, djk['predecessors'][path[0]])

    return {'cost': djk['distances'][end], 'path': path, 'start': start, 'end': end}


def candidate_solution(start, end, visit, current_time):
    """
    NN Heuristic

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :param visit: set of nodes to visit
    :type visit: set[str]

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: A candidate for the shortest distance path from the start to end node while visiting all nodes in the visit set.
    :rtype: dict[str, float | list[str]]
    """

    path = [start]
    cost = 0
    current_vertex = start
    visit_set = visit.copy()

    while len(visit_set) != 0:
        closest_node = fetch_djk(current_vertex, None, current_time, visit_set)
        path.append(closest_node['end'])
        cost += closest_node['cost']
        visit_set.remove(closest_node['end'])
        current_vertex = closest_node['end']

    # go back to the end node
    closest_node = fetch_djk(current_vertex, end, current_time, None)
    path.append(closest_node['end'])
    cost += closest_node['cost']

    return {'path': path, 'cost': cost}


def calculate_cost(path, current_time):
    """
    Dijkstra's Cost Calculator

    :param path: path to get the cost of
    :type path: list[str]

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: The cost of traversing that path.
    :rtype: int
    """
    cost = 0
    route = path.copy()

    for i in range(len(route) - 1):
        djk = fetch_djk(route[i], route[i + 1], current_time, None)
        cost += djk['cost']

    return cost


def pairwise_swap(u, v, path):
    """
    2-opt

    :param path: path for the swap to be performed on
    :type path: list[str]

    :param u: first node of first edge
    :type u: int

    :param v: first node of second edge
    :type v: int

    :return: path after swap.
    :rtype: list[str]
    """

    new_tour = []

    for i in range(u + 1):
        new_tour.append(path[i])
    for i in range(v, u, -1):
        new_tour.append(path[i])
    for i in range(v + 1, len(path)):
        new_tour.append(path[i])

    return new_tour


def hill_climbing(candidate, current_time, fail_count=0):
    """
    Dijkstra's Cost Calculator

    :param candidate: candidate solution to improve upon
    :type candidate: list[str]

    :param fail_count: number of times the algorithm has not improved
    :type fail_count: int

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: an improved path.
    :rtype: list[str]
    """

    if fail_count > 200:
        return candidate
    else:
        cost = calculate_cost(candidate, current_time)
        u = random.randint(0, len(candidate)-3)
        v = random.randint(u+1, len(candidate)-2)

        # print(f"u value of {u} and v value of {v}")

        new_tour = pairwise_swap(u, v, candidate)
        new_cost = calculate_cost(new_tour, current_time)

        if new_cost < cost:
            print(f"The cost has been improved from {cost} to {new_cost}")
            return hill_climbing(new_tour, current_time, 0)
        else:
            return hill_climbing(candidate, current_time, fail_count + 1)


def held_karp(start, end, visit, current_time):
    """
    Held-Karp Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :param visit: set of nodes to visit
    :type visit: set[str]

    :param current_time: the current time when Dijkstra's is being called
    :type current_time: dt.datetime

    :return: The shortest distance path from the start to end node while visiting all nodes in the visit set.
    :rtype: dict[str, float | list[str]]
    """
    # make sure visit is a set
    if type(visit) is not set:
        print("Error: visit must be a set of nodes")
        return {'cost': float('inf'), 'path': None}
    # visit set being empty means direct distance, ∴ we can use Dijkstra's instead
    if len(visit) == 0:
        djk = fetch_djk(start, end, current_time, None)
        return {'cost': djk['cost'], 'path': djk['path']}
    else:
        minimum = {'cost': float('inf')}
        for rand_node in visit:
            # divides larger path into smaller subpaths by going from start to any random node C while visiting
            # everything else in the visit set. This is then combined with djk from C to the end to get the full path.
            sub_path = fetch_hk(start, rand_node, visit.difference({rand_node}), current_time)
            djk = fetch_djk(rand_node, end, current_time + dt.timedelta(minutes=sub_path['cost']), None)
            cost = sub_path['cost'] + djk['cost']
            if cost < minimum['cost']:
                # the path is calculated by adding the final path from dijkstra's to the sub-path
                # the [1:] is used to remove the first node from dijkstra's as if not, the rand_node is duplicated
                minimum = {'cost': cost, 'path': sub_path['path'] + djk['path'][1:]}
        return minimum


def main():
    global edge_lookup_matrix
    global cached_djk
    global cached_hk
    global holiday
    global concession
    global hamiltonian_path
    global g

    g = nx.Graph()
    setup_graph()

    # concession = query_yes_no("Do you possess a concession card?")
    # holiday = query_yes_no("Is today a weekend or a holiday?")
    # user_name = select_friend("Who are you?")
    # while True:
    #     string_time = input('What is the current time? (HH:MM) ')
    #     try:
    #         selected_time = dt.datetime.strptime(string_time, r"%H:%M")
    #         break
    #     except ValueError:
    #         print("Please enter a valid time in the HH:MM format")

    concession = True
    holiday = True
    user_name = 'Garv'
    string_time = '08:30'
    selected_time = dt.datetime.strptime(string_time, r"%H:%M")
    print("The algorithm is running with the following parameters:")
    print(f"Concession card: {concession}")
    print(f"Holiday: {holiday}")
    print(f"User: {user_name}")
    print(f"Time: {string_time}")

    # The above code has hard coded input parameters for testing purposes.
    # Production code may use user inputer global variables.

    print("")

    start_time = time.perf_counter()
    cached_djk = {}
    cached_hk = {}

    # Create a lookup matrix so that edge data can be accessed given any two vertices
    # Create a dictionary of distances, similar to a distance matrix, but allowing for multiple edges between nodes
    edge_lookup_matrix = {frozenset({edge['from'], edge['to']}): [] for edge in edges}
    for edge in edges:
        edge_lookup_matrix[frozenset({edge['from'], edge['to']})].append(edge)

    # visit_set = set(g.nodes()).difference({home})
    friend_distances = calculate_nodes(node_lat_long)
    visit_set = set(val['closest_node'] for key, val in friend_distances.items())
    people_at_nodes = {node: [] for node in visit_set}
    for key, val in friend_distances.items():
        people_at_nodes[val['closest_node']].append(key)

    home = friend_distances[user_name]['closest_node']
    friend_distances['You'] = friend_distances[user_name]
    friend_distances.pop(user_name)

    # force visit_set
    print(g.nodes())
    visit_set = {'Glen Waverley',
                 'CGS WH',
                 'Mount Waverley',
                 'Richmond',
                 'Parliament',
                 'Melbourne Central',
                 'Flinders Street',
                 'Brighton Beach',
                 'Camberwell',
                 'Oakleigh',
                 'Wheelers Hill Library',
                 'Chadstone',
                 'Caulfield',
                 # 'CGS CC',
                 # 'Brandon Park'
                 }.difference({home})

    print(f"I have {len(friend_distances)} friends and they live closest to the following {len(visit_set)} nodes:")
    [print(
        f"{key if key != 'You' else f'{key} ({user_name})'} {'lives' if key != 'You' else 'live'} "
        f"{round(val['distance'], 3)}km from {val['closest_node']}") for key, val in friend_distances.items()]

    # print out friends that would take more than 20 minutes to walk (average human walking speed is 5.1 km/h)
    long_walk = [f"{key} ({round(friend_distances[key]['distance'] / 5.1 * 60, 2)})"
                 for key, val in friend_distances.items() if val['distance'] / 5.1 * 60 > 20]
    if len(long_walk) > 0:
        print(f'\nWarning! These {len(long_walk)} friends have to walk more than 20 minutes in order to get to their '
              f'transport hub. Possibly consider adding hubs closer to their houses: ', end=' ')
        print(f'{" and ".join([", ".join(long_walk[:-1]), long_walk[-1]] if len(long_walk) > 2 else long_walk)}')

    candidate = candidate_solution(home, home, visit_set, selected_time)
    print("candidate")
    print(candidate)
    print("improved")
    print(hill_climbing(candidate['path'], selected_time))
    hamiltonian_path = fetch_hk(home, home, visit_set, selected_time)

    print(f"\nThe trip would cost you ${calculate_prices():,.2f} and would take you "
          f"{round(hamiltonian_path['cost'] + 2 * friend_distances['You']['distance'] / 5.1 * 60, 2)} "
          f"minutes, taking the following route: ")

    # prints out the route with correct wording and the people picked up at each point
    for index in range(len(hamiltonian_path['path'])):
        if index == 0:
            print('From', end=' ')

        node = hamiltonian_path['path'][index]
        print(node, end='')
        if node in people_at_nodes:
            print(f" ({', '.join(people_at_nodes[hamiltonian_path['path'][index]])})", end='')
            people_at_nodes.pop(node)

        if index == len(hamiltonian_path['path']) - 1:
            print('.')
        elif index == len(hamiltonian_path['path']) - 2:
            print(' and back to ', end='')
        else:
            print(' to ', end='')

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"\nIt took {elapsed_time:.4f} seconds to run.")

    return elapsed_time


if __name__ == "__main__":
    global edge_lookup_matrix
    global cached_djk
    global cached_hk
    global holiday
    global concession
    global hamiltonian_path
    global g

    running_time = []

    for i in range(1):
        running_time.append(main())

    print(running_time)
    print(f'Average running time is {sum(running_time) / len(running_time)}')
