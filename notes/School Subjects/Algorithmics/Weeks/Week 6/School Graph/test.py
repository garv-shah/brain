import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from collections import deque

g = nx.Graph(nx.nx_pydot.read_dot('project.dot'))

options = {
    "font_size": 10,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw_networkx(g, **options)


nt = Network('500px', '500px')
nt.from_nx(g)
nt.toggle_physics(True)
nt.show_buttons()
nt.show('nx.html')

# ax = plt.gca()
# ax.margins(0.20)
# plt.axis("off")
# plt.show()
