import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from collections import deque

g = nx.Graph([
    ("D", "C"),
    ("D", "A"),
    ("C", "A"),
    ("A", "B"),
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

# Modified DFS
s = deque()
seen = []
current_node = "A"
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

        current_node = s.pop()

        # if the current node has already been visited then there must have been a cycle
        cycle_detected = current_node in seen

print(f'A cycle {"was" if cycle_detected else "was not"} detected')

# nt = Network('500px', '500px')
# nt.from_nx(g)
# nt.toggle_physics(True)
# nt.show_buttons()
# nt.show('nx.html')

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
