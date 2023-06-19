import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx
from queue import PriorityQueue

# Best First Search Algorithm

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


heuristic_weights = {
    "A": 4,
    "B": 2,
    "C": 3,
    "D": 3,
    "E": 2,
    "F": 1,
    "G": 2,
    "H": 2,
    "I": 1,
    "J": 0
}


def start():
    canvas.label('title').remove()
    g = nx.DiGraph()

    g.add_edge("A", "B", weight=2)
    g.add_edge("A", "C", weight=3)
    g.add_edge("B", "A", weight=4)
    g.add_edge("B", "D", weight=3)
    g.add_edge("B", "E", weight=2)
    g.add_edge("B", "F", weight=1)
    g.add_edge("C", "A", weight=4)
    g.add_edge("C", "G", weight=2)
    g.add_edge("D", "B", weight=2)
    g.add_edge("E", "B", weight=2)
    g.add_edge("E", "H", weight=2)
    g.add_edge("F", "B", weight=2)
    g.add_edge("G", "C", weight=3)
    g.add_edge("G", "I", weight=1)
    g.add_edge("H", "E", weight=2)
    g.add_edge("H", "I", weight=1)
    g.add_edge("I", "G", weight=2)
    g.add_edge("I", "H", weight=2)
    g.add_edge("I", "J", weight=0)
    g.add_edge("I", "J", weight=0)
    g.add_edge("J", "I", weight=1)

    # Render graph
    add_graph(canvas, g)
    canvas.nodes().color('gray')
    canvas.pause(1)

    q = PriorityQueue()
    seen = []
    current_node = 'B'
    q.put((heuristic_weights[current_node], current_node))
    source_dict = {}

    while True:
        seen.append(current_node)
        canvas.node(current_node).highlight().size('1.25x').pause(0.5)
        canvas.node(current_node).color('dark-gray')
        for neighbor in g.neighbors(current_node):
            if neighbor not in seen:
                q.put((heuristic_weights[neighbor], neighbor))
                seen.append(neighbor)
                source_dict[neighbor] = current_node

        if q.empty():
            break
        else:
            current_node = q.get()[1]
            if current_node in source_dict:
                canvas.edge((source_dict[current_node], current_node)).traverse('red').pause(0.5)
            print(current_node)

canvas.onmessage('start', start)
webbrowser.open('http://localhost:5050')
server.start()
