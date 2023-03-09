import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from collections import deque

g = nx.DiGraph([
    ('1', '2'),
    ('1', '5'),
    ('1', '6'),
    ('2', '7'),
    ('2', '3'),
    ('3', '5'),
    ('3', '6'),
    ('4', '3'),
    ('4', '6'),
    ('5', '2'),
    ('5', '4'),
])

options = {
    "font_size": 16,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 4,
    "width": 5,
}

nx.draw_networkx(g, **options)

# BFS Algorithm
q = deque()
seen = []
current_node = '1'
q.append(current_node)

while True:
    seen.append(current_node)
    for neighbor in g.neighbors(current_node):
        if neighbor not in seen:
            q.append(neighbor)
            seen.append(neighbor)

    if len(q) == 0:
        break
    else:
        current_node = q.popleft()
        print(current_node)


# nt = Network('500px', '500px')
# nt.from_nx(g)
# nt.toggle_physics(True)
# nt.show_buttons()
# nt.show('nx.html')

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
