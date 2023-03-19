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

    g.add_edge(1, 5, weight=3.2)
    g.add_edge(4, 5, weight=3.5)
    g.add_edge(4, 6, weight=9.3)
    g.add_edge(3, 6, weight=5.2)
    g.add_edge(3, 1, weight=2.9)
    g.add_edge(7, 1, weight=1.9)
    g.add_edge(2, 1, weight=3.6)
    g.add_edge(5, 7, weight=2.8)
    g.add_edge(2, 7, weight=3.4)
    g.add_edge(2, 3, weight=1.7)
    g.add_edge(7, 4, weight=3.7)
    g.add_edge(0, 7, weight=1.6)
    g.add_edge(0, 2, weight=2.6)
    g.add_edge(0, 6, weight=5.8)
    g.add_edge(0, 4, weight=3.8)
    g.add_edge(2, 6, weight=4.0)

    # Render graph
    add_graph(canvas, g)
    canvas.nodes().color('gray')
    canvas.pause(1)

    n = 1
    seen = [n]
    canvas.node(n).color('dark-gray')

    while len(seen) < len(g.nodes):
        arr = []
        smallest = {"node": None, "weight": float('inf')}
        for node in seen:
            for n2 in g.neighbors(node):
                weight = g.edges[node, n2]['weight']
                if [(node, n2), weight] not in arr and [(n2, node), weight] not in arr and n2 not in seen:
                    arr.append([(node, n2), weight])
                if weight < smallest['weight'] and n2 not in seen:
                    smallest = {"node": n2, "weight": weight}
                    n = node

        arr = sorted(arr, key=lambda x: x[1])
        print(arr)
        print('')

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
