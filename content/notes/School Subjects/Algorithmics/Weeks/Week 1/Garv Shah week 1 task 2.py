import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph([
    ('a', 'b'),
    ('b', 'c'),
    ('c', 'd'),
    ('d', 'e'),
    ('e', 'a'),
    ('f', 'b'),
    ('f', 'c'),
    ('f', 'd')
])

node_outline_colour_map = ['black', 'red', 'red', 'blue', 'blue', 'black']
edge_colour_map = ['black', 'black', 'red', 'black', 'black', 'black', 'blue', 'black']

options = {
    "font_size": 28,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": node_outline_colour_map,
    "edge_color": edge_colour_map,
    "linewidths": 3,
    "width": 4,
}

pos = nx.spring_layout(g)

nx.draw_networkx(g, pos, **options)

edge_labels = {('a', 'b'): '2',
               ('b', 'c'): '7',
               ('c', 'd'): '9',
               ('d', 'e'): '8',
               ('e', 'a'): '3',
               ('f', 'b'): '1',
               ('f', 'c'): '4',
               ('f', 'd'): '4'}

nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, rotate=False, font_size=16)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.10)
plt.axis("off")
plt.show()
