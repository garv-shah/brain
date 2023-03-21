import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

# Dijkstra's Algorithm

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    total_cost = 0
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
    canvas.nodes().color('gray')
    canvas.pause(1)

    source = "C"
    distance = []
    predecessor = []
    unexplored_list = []

    for node in g.nodes:
        distance[node] = float('inf')
        predecessor[node] = None
        unexplored_list.append(node)

    distance[source] = 0

    n = "A"
    g.nodes[n]['seen'] = True
    seen = [n]
    canvas.node(n).color('dark-gray')

    while len(seen) < len(g.nodes):
        smallest = {"node": None, "weight": float('inf')}
        for node in seen:
            for n2 in g.neighbors(node):
                weight = g.edges[node, n2]['weight']
                if weight < smallest['weight'] and n2 not in seen:
                    smallest = {"node": n2, "weight": weight}
                    n = node

        canvas.edge((n, smallest['node'])).traverse('red').pause(0.5)
        n = smallest['node']
        total_cost += smallest['weight']
        seen.append(n)
        canvas.node(n).highlight().size('1.25x').pause(0.5)
        canvas.node(n).color('dark-gray')

    canvas.label('title').add(text=f'MST Cost: {total_cost}')


canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
