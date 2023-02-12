import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph([(6, 4), (4, 5), (4, 3), (3, 2), (5, 2), (5, 1), (1, 2)])

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw_networkx(g, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
