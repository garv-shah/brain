import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from collections import deque

g = nx.Graph([
    ("Lounge", "Dining"),
    ("Lounge", "Hall"),
    ("Dining", "Kitchen"),
    ("Dining", "Hall"),
    ("Hall", "Bed 1"),
    ("Hall", "Bath"),
    ("Hall", "Bed 2"),
    ("Hall", "Verandah"),
    ("Kitchen", "Verandah"),
])

options = {
    "font_size": 10,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw_networkx(g, **options)

# BFS Algorithm
# q = deque()
# seen = []
# current_node = "Kitchen"
# q.append(current_node)
#
# while True:
#     seen.append(current_node)
#     for neighbor in g.neighbors(current_node):
#         if neighbor not in seen:
#             q.append(neighbor)
#             seen.append(neighbor)
#
#     if len(q) == 0:
#         break
#     else:
#         current_node = q.popleft()
#         print(current_node)

# DFS Algorithm
s = deque()
seen = []
current_node = "Kitchen"

while True:
    for neighbor in reversed(sorted(list(g.neighbors(current_node)))):
        if neighbor not in seen:
            s.append(neighbor)

    if len(s) == 0:
        break
    else:
        seen.append(current_node)
        print(current_node)

        current_node = s.pop()


# nt = Network('500px', '500px')
# nt.from_nx(g)
# nt.toggle_physics(True)
# nt.show_buttons()
# nt.show('nx.html')

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
