import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

edges = [
    {'from': 'Glen Waverley', 'to': 'CGS WH', 'weight': 16, 'line': '754 Bus Line'},
    {'from': 'Glen Waverley', 'to': 'CGS WH', 'weight': 23, 'line': '753 Bus Line'},
    {'from': 'Glen Waverley', 'to': 'Mount Waverley', 'weight': 12, 'line': '623 Bus Line'},
    {'from': 'Glen Waverley', 'to': 'Mount Waverley', 'weight': 8, 'line': 'Glen Waverley'},
    {'from': 'Mount Waverley', 'to': 'Richmond', 'weight': 20, 'line': 'Glen Waverley'},
    {'from': 'Richmond', 'to': 'Parliament', 'weight': 20, 'line': 'Glen Waverley'},
    {'from': 'Parliament', 'to': 'Melbourne Central', 'weight': 20, 'line': 'Glen Waverley'},
    {'from': 'Melbourne Central', 'to': 'Flinders Street', 'weight': 20, 'line': 'Glen Waverley'},
    {'from': 'Flinders Street', 'to': 'Richmond', 'weight': 20, 'line': 'Glen Waverley'},
    {'from': 'Flinders Street', 'to': 'Brighton Beach', 'weight': 20, 'line': 'Sandringham'},
    {'from': 'Richmond', 'to': 'Camberwell', 'weight': 20, 'line': 'Camberwell'},
    {'from': 'Oakleigh', 'to': 'Richmond', 'weight': 20, 'line': 'Pakenham'},
    {'from': 'Richmond', 'to': 'Parliament', 'weight': 20, 'line': 'Pakenham'},
    {'from': 'Parliament', 'to': 'Melbourne Central', 'weight': 20, 'line': 'Pakenham'},
    {'from': 'Melbourne Central', 'to': 'Flinders Street', 'weight': 20, 'line': 'Pakenham'},
    {'from': 'Flinders Street', 'to': 'Richmond', 'weight': 20, 'line': 'Pakenham'},
    {'from': 'CGS WH', 'to': 'Wheelers Hill Library', 'weight': 17, 'line': 'Walk'},
    {'from': 'Wheelers Hill Library', 'to': 'Oakleigh', 'weight': 20, 'line': '693 Bus Line'},
    {'from': 'Chadstone', 'to': 'Oakleigh', 'weight': 3, 'line': '800 Bus Line'},
    {'from': 'Chadstone', 'to': 'Caulfield', 'weight': 11, 'line': '900 Bus Line'},
    {'from': 'Caulfield', 'to': 'Flinders Street', 'weight': 16, 'line': 'Frankston'},
    {'from': 'Caulfield', 'to': 'Oakleigh', 'weight': 16, 'line': '900 Bus Line'},
    {'from': 'Caulfield', 'to': 'Oakleigh', 'weight': 27, 'line': 'Pakenham'},
    {'from': 'Caulfield', 'to': 'CGS CC', 'weight': 15, 'line': 'Tram'},
    {'from': 'Wheelers Hill Library', 'to': 'Brandon Park', 'weight': 6, 'line': '693 Bus Line'},
    {'from': 'Oakleigh', 'to': 'Brandon Park', 'weight': 25, 'line': '693 Bus Line'},
]

lineColours = {
    # Train Lines
    'Glen Waverley': '#BA3B46',
    'Sandringham': '#F038FF',
    'Camberwell': '#FF8600',
    'Pakenham': '#E2EF70',
    'Frankston': '#70E4EF',
    # Misc Methods
    'Walk': '#538083',
    'Tram': '#2A7F62',
    # Bus Lines
    '754 Bus Line': '#86E7B8',
    '753 Bus Line': '#93FF96',
    '623 Bus Line': '#B2FFA8',
    '693 Bus Line': '#D0FFB7',
    '800 Bus Line': '#7DCFB6',
    '900 Bus Line': '#AABD8C',
}

g = nx.Graph()

for index in range(len(edges)):
    from_node = edges[index]['from']
    to_node = edges[index]['to']
    color = lineColours[edges[index]['line']]
    weight = edges[index]['weight']

    g.add_edge(from_node, to_node, color=color, weight=weight)

#     current_edge.color(lineColours[edges[index]['line']])
#     current_edge.label().add(text=edges[index]['weight'])
#
# for index in range(len(node_list)):
#     node = node_list[index]
#
#     canvas.node(node).label('name').add(text=node,color='black')
#     canvas.node(node).label().add(text=str(index + 1))

print(g.edges)

colors = nx.get_edge_attributes(g, 'color').values()
weights = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])


pos = {'Glen Waverley': (1.2768713098241284, 0.49920912491483405), 'CGS WH': (1.4265826300847813, 0.1204628887684871), 'Mount Waverley': (0.7043105941642556, 0.7733282005439384), 'Richmond': (0.341812028442958, 0.4373730047276754), 'Parliament': (-0.4284117911380293, 0.7517066156790655), 'Melbourne Central': (-0.45435855635285616, 0.42191397468088576), 'Flinders Street': (-0.42932311065271866, 0.08181531365151296), 'Brighton Beach': (-0.665772732541814, -0.23509480230767532), 'Camberwell': (0.07247908565059714, 0.8255351955388853), 'Oakleigh': (0.633506906308221, 0.12303939377628548), 'Wheelers Hill Library': (1.1109175815449, -0.34135548220469414), 'Chadstone': (0.11467939187567033, -0.7484751364978814), 'Caulfield': (-0.12498201317170499, -0.3226959725728168), 'CGS CC': (-0.8083854616920082, -0.7323602688127431), 'Brandon Park': (0.5691253741247339, -0.6003212036334155)}


# Draggable nodes utility
# pos = nx.layout.kamada_kawai_layout(g)
#
# plot = DraggableNodes(g, pos)
# plot.show()

cmap = plt.cm.viridis(np.linspace(0, 1, g.number_of_edges()))
nx.draw_networkx(g, pos, with_labels=True, labels={idx: val for idx, val in enumerate(g.nodes())},)
nx.draw_networkx_edges(g, pos, edge_color=cmap)
[nx.draw_networkx_edge_labels(g, pos, edge_labels={e: i}, font_color=cmap[i]) for i, e in enumerate(g.edges())]

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
