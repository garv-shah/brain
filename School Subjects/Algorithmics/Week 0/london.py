import networkx as nx
import matplotlib.pyplot as plt
import random as random
import csv

g = nx.Graph()

with open('stations.csv') as station_csv:
    stations_dict = csv.DictReader(station_csv)
    for row in stations_dict:
        g.add_edge(row['StationA'], row['StationB'])
        g[row['StationA']][row['StationB']]['Line'] = row['Line']
        g[row['StationA']][row['StationB']]['weight'] = row['Distance']

# Display the graph

options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3,
}

pos = nx.spring_layout(g)

nx.draw_networkx_nodes(g, pos, node_size=550, node_color='yellow')
nx.draw_networkx_labels(g, pos)

nx.draw_networkx_edges(g, pos, width=3, edge_color='darkblue')
# nx.draw_networkx_edge_labels(g,pos)

plt.axis("off")
plt.show()
