import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

# Prim's Algorithm

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    total_cost = 0
    canvas.label('title').remove()
    g = nx.Graph()

    g.add_edge("A", "B", weight=8)
    g.add_edge("B", "F", weight=17)
    g.add_edge("F", "J", weight=24)
    g.add_edge("J", "L", weight=14)
    g.add_edge("L", "K", weight=15)
    g.add_edge("K", "G", weight=19)
    g.add_edge("G", "C", weight=20)
    g.add_edge("C", "A", weight=13)
    g.add_edge("C", "D", weight=12)
    g.add_edge("B", "D", weight=14)
    g.add_edge("B", "D", weight=14)
    g.add_edge("D", "E", weight=3)
    g.add_edge("E", "F", weight=7)
    g.add_edge("E", "H", weight=16)
    g.add_edge("G", "H", weight=8)
    g.add_edge("H", "I", weight=5)
    g.add_edge("K", "I", weight=17)
    g.add_edge("I", "J", weight=7)

    # Render graph
    add_graph(canvas, g)
    canvas.nodes().color('gray')
    canvas.pause(1)

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
