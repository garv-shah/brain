import algorithmx
import webbrowser
import networkx as nx

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    # Generate a random graph
    g = nx.fast_gnp_random_graph(10, 0.3, seed=50)

    # Render graph
    canvas.nodes(g.nodes).add().label().remove()
    canvas.edges(g.edges).add()


canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
