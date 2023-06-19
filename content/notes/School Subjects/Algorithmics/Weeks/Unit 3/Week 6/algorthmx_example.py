import algorithmx
# Depth First Search

import networkx as nx

server = algorithmx.http_server(port=5050)
canvas = server.canvas()


def start():
    # Generate a random graph
    G = nx.fast_gnp_random_graph(10, 0.3, seed=50)
    nx.set_node_attributes(G, False, 'seen')

    # Render graph
    canvas.nodes(G.nodes).add().label().remove()
    canvas.edges(G.edges).add()
    canvas.pause(1)

    # Recursive DFS function
    def dfs(n):
        G.nodes[n]['seen'] = True

        canvas.node(n).highlight().size('1.25x')
        canvas.node(n).color('blue')
        canvas.pause(0.5)

        for n2 in G.neighbors(n):
            if G.nodes[n2]['seen']:
                continue

            canvas.edge((n, n2)).traverse('red').pause(0.5)
            dfs(n2)  # DFS on neighbor
            canvas.edge((n2, n)).traverse('blue').pause(0.5)
            canvas.node(n).highlight().size('1.25x').pause(0.5)

    dfs(0)


canvas.onmessage('start', start)
server.start()
