import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

# Dijkstra's Algorithm

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    canvas.label('title').remove()
    g = nx.Graph()

    g.add_edge("C", "F", weight=6)
    g.add_edge("C", "A", weight=4)
    g.add_edge("F", "A", weight=5)
    g.add_edge("F", "D", weight=1)
    g.add_edge("F", "E", weight=6)
    g.add_edge("A", "D", weight=7)
    g.add_edge("A", "B", weight=2)
    g.add_edge("E", "B", weight=5)
    g.add_edge("D", "E", weight=6)
    g.add_edge("D", "B", weight=6)

    # Render graph
    add_graph(canvas, g)
    canvas.pause(1)

    source = "C"
    destination = "E"
    distance = {}
    predecessor = {}
    unexplored_list = []

    for node in g.nodes:
        distance[node] = float('inf')
        predecessor[node] = None
        unexplored_list.append(node)

    distance[source] = 0

    while len(unexplored_list) > 0:
        min_node = None
        for node in unexplored_list:
            if min_node is None:
                min_node = node
            elif distance[node] < distance[min_node]:
                min_node = node

        unexplored_list.remove(min_node)
        for neighbor in g.neighbors(min_node):
            this_dist = distance[min_node] + g.edges[min_node, neighbor]['weight']
            if this_dist < distance[neighbor]:
                distance[neighbor] = this_dist
                predecessor[neighbor] = min_node

    node = destination
    while node != source:
        canvas.edge((node, predecessor[node])).traverse('red').pause(0.5)
        node = predecessor[node]

    canvas.label('title').add(text=f'Distance: {distance[destination]}')


canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
