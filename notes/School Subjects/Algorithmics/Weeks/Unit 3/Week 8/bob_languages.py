import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

# Prim's Algorithm

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    g = nx.DiGraph()

    g.add_edge(15, 16)
    g.add_edge(15, 31)
    g.add_edge(16, 32)
    g.add_edge(31, 32)
    g.add_edge(22, 126)
    g.add_edge(32, 126)
    g.add_edge(16, 127)
    g.add_edge(22, 141)
    g.add_edge(16, 141)
    g.add_edge(32, 169)

    canvas.node(15).add().label('course').add(text='LA15')
    canvas.node(16).add().label('course').add(text='LA16')
    canvas.node(31).add().label('course').add(text='LA31')
    canvas.node(32).add().label('course').add(text='LA32')
    canvas.node(22).add().label('course').add(text='LA22')
    canvas.node(126).add().label('course').add(text='LA126')
    canvas.node(127).add().label('course').add(text='LA127')
    canvas.node(169).add().label('course').add(text='LA169')
    canvas.node(141).add().label('course').add(text='LA141')

    canvas.nodes().add().label('course').add(text='LA')

    # Render graph
    add_graph(canvas, g)


canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
