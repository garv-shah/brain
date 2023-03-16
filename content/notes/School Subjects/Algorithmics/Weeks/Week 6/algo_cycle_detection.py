import algorithmx
from collections import deque
import networkx as nx

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    # Generate a random graph
    g = nx.fast_gnp_random_graph(10, 0.3)
    # g = nx.Graph([
    #     (4, 3),
    #     (3, 0),
    #     (0, 2),
    # ])
    nx.set_node_attributes(g, False, 'seen')

    # Render graph
    canvas.nodes(g.nodes).add().label().remove()
    canvas.edges(g.edges).add()
    canvas.pause(1)

    # Modified DFS
    s = deque()
    seen = []
    current_node = 0
    cycle_detected = False

    while True:
        for neighbor in reversed(sorted(list(g.neighbors(current_node)))):
            if neighbor not in seen:
                s.append(neighbor)

        if len(s) == 0:
            break
        else:
            seen.append(current_node)
            print(current_node)
            new_node = s.pop()

            current_node = new_node

            canvas.node(current_node).highlight().size('1.25x')
            canvas.node(current_node).color('blue')
            canvas.pause(0.5)

            # if the current node has already been visited then there must have been a cycle
            cycle_detected = current_node in seen

    print(f'A cycle {"was" if cycle_detected else "was not"} detected')


canvas.onmessage('start', start)
server.start()
