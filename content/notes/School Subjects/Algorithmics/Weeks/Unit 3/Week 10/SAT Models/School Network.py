import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

server = algorithmx.http_server(port=5050)
canvas = server.canvas()

edges = [
    {'from': 'Library', 'to': 'Reading Room', 'weight': 0.25},
    {'from': 'Library', 'to': 'Inquiry Space', 'weight': 0.5},
    {'from': 'Library', 'to': 'Art Staffroom', 'weight': 0.5},
    {'from': 'Art Staffroom', 'to': 'CAD Room', 'weight': 0.25},
    {'from': 'Art Staffroom', 'to': 'TV Studio', 'weight': 0.5},
    {'from': 'Art Staffroom', 'to': 'Black Theatre', 'weight': 0.25},
    {'from': 'CAD Room', 'to': 'Graphic Design Room', 'weight': 0.25},
    {'from': 'TV Studio', 'to': 'Mem Hall', 'weight': 0.5},
    {'from': 'TV Studio', 'to': 'Art Office', 'weight': 0.75},
    {'from': 'Mem Hall', 'to': 'Black Theatre', 'weight': 0.75},
    {'from': 'Art Office', 'to': 'SMR', 'weight': 0.25},
    {'from': 'Art Office', 'to': 'Black Theatre', 'weight': 0.5},
    {'from': 'SMR', 'to': 'Soundhouse', 'weight': 0.5},
    {'from': 'Soundhouse', 'to': 'Entrance', 'weight': 0.75},
    {'from': 'Entrance', 'to': 'Black Theatre', 'weight': 0.25},
    {'from': 'Art Office', 'to': 'Entrance', 'weight': 0.5},
    {'from': 'Entrance', 'to': 'Reception', 'weight': 0.25},
    {'from': 'Entrance', 'to': 'Car Park', 'weight': 0.25},
    {'from': 'Reception', 'to': 'Car Park', 'weight': 0.25},
    {'from': 'Courtyard', 'to': 'Entrance', 'weight': 0.5},
    {'from': 'Courtyard', 'to': 'Library', 'weight': 0.25},
    {'from': 'Courtyard', 'to': 'Reading Room', 'weight': 0.5},
    {'from': 'Courtyard', 'to': 'E Cluster', 'weight': 1},
    {'from': 'Courtyard', 'to': 'F Cluster', 'weight': 0.75},
    {'from': 'E Cluster', 'to': 'F Cluster', 'weight': 0.25},
    {'from': 'E Cluster', 'to': 'Quadrangle', 'weight': 0.25},
    {'from': 'D Cluster', 'to': 'Quadrangle', 'weight': 0.25},
    {'from': 'D7', 'to': 'Quadrangle', 'weight': 0.25},
    {'from': 'J Cluster', 'to': 'Quadrangle', 'weight': 0.5},
    {'from': 'J Cluster', 'to': 'F Cluster', 'weight': 0.25},
    {'from': 'E Cluster', 'to': 'J Cluster', 'weight': 0.25},
    {'from': 'H Cluster', 'to': 'J Cluster', 'weight': 0.25},
    {'from': 'H Cluster', 'to': 'L Cluster', 'weight': 0.25},
    {'from': 'Lecture Theatre', 'to': 'L Cluster', 'weight': 0.75},
    {'from': 'Lecture Theatre', 'to': 'F Cluster', 'weight': 0.5},
    {'from': 'Lecture Theatre', 'to': 'Library', 'weight': 0.5},
    {'from': 'Lecture Theatre', 'to': 'Mem Hall', 'weight': 0.75},
]


def start():
    canvas.label('title').remove()
    edge_list = []
    node_list = []

    # create node and edge list
    for index in range(len(edges)):
        edge = edges[index]
        edge_list.append([edge['from'], edge['to'], index])
        node_list.append(edge['from'])
        node_list.append(edge['to'])

    # remove duplicates from node_list
    node_list = list(dict.fromkeys(node_list))

    canvas.nodes(node_list).add()
    canvas.edges(edge_list).add()

    for index in range(len(edge_list)):
        current_edge = canvas.edge(edge_list[index])
        current_edge.label().add(text=edges[index]['weight'])

    for index in range(len(node_list)):
        node = node_list[index]

        canvas.node(node).label('name').add(text=node,color='black')
        canvas.node(node).label().add(text=str(index + 1))


    # canvas.nodes().color('gray')
    # canvas.pause(1)
    #
    # n = "A"
    # g.nodes[n]['seen'] = True
    # seen = [n]
    # canvas.node(n).color('dark-gray')
    #
    # while len(seen) < len(g.nodes):
    #     smallest = {"node": None, "weight": float('inf')}
    #     for node in seen:
    #         for n2 in g.neighbors(node):
    #             weight = g.edges[node, n2]['weight']
    #             if weight < smallest['weight'] and n2 not in seen:
    #                 smallest = {"node": n2, "weight": weight}
    #                 n = node
    #
    #     canvas.edge((n, smallest['node'])).traverse('red').pause(0.5)
    #     n = smallest['node']
    #     total_cost += smallest['weight']
    #     seen.append(n)
    #     canvas.node(n).highlight().size('1.25x').pause(0.5)
    #     canvas.node(n).color('dark-gray')
    #
    # canvas.label('title').add(text=f'MST Cost: {total_cost}')


canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
