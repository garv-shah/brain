import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure, text


def custom_draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=None,
        label_pos=0.5,
        font_size=10,
        font_color="k",
        font_family="sans-serif",
        font_weight="normal",
        alpha=None,
        bbox=None,
        horizontalalignment="center",
        verticalalignment="center",
        ax=None,
        rotate=True,
        clip_on=True,
        rad=0.0
):
    """Draw edge labels.

    Parameters
    ----------
    G : graph
        A networkx graph

    pos : dictionary
        A dictionary with nodes as keys and positions as values.
        Positions should be sequences of length 2.

    edge_labels : dictionary (default={})
        Edge labels in a dictionary of labels keyed by edge two-tuple.
        Only labels for the keys in the dictionary are drawn.

    label_pos : float (default=0.5)
        Position of edge label along edge (0=head, 0.5=center, 1=tail)

    font_size : int (default=10)
        Font size for text labels

    font_color : string (default='k' black)
        Font color string

    font_weight : string (default='normal')
        Font weight

    font_family : string (default='sans-serif')
        Font family

    alpha : float or None (default=None)
        The text transparency

    bbox : Matplotlib bbox, optional
        Specify text box properties (e.g. shape, color etc.) for edge labels.
        Default is {boxstyle='round', ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0)}.

    horizontalalignment : string (default='center')
        Horizontal alignment {'center', 'right', 'left'}

    verticalalignment : string (default='center')
        Vertical alignment {'center', 'top', 'bottom', 'baseline', 'center_baseline'}

    ax : Matplotlib Axes object, optional
        Draw the graph in the specified Matplotlib axes.

    rotate : bool (deafult=True)
        Rotate edge labels to lie parallel to edges

    clip_on : bool (default=True)
        Turn on clipping of edge labels at axis boundaries

    Returns
    -------
    dict
        `dict` of labels keyed by edge

    Examples
    --------
    >>> G = nx.dodecahedral_graph()
    >>> edge_labels = nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))

    Also see the NetworkX drawing examples at
    https://networkx.org/documentation/latest/auto_examples/index.html

    See Also
    --------
    draw
    draw_networkx
    draw_networkx_nodes
    draw_networkx_edges
    draw_networkx_labels
    """

    if ax is None:
        ax = plt.gca()
    if edge_labels is None:
        labels = {(u, v): d for u, v, d in G.edges(data=True)}
    else:
        labels = edge_labels
    text_items = {}
    for (n1, n2), label in labels.items():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (
            x1 * label_pos + x2 * (1.0 - label_pos),
            y1 * label_pos + y2 * (1.0 - label_pos),
        )
        pos_1 = ax.transData.transform(np.array(pos[n1]))
        pos_2 = ax.transData.transform(np.array(pos[n2]))
        linear_mid = 0.5 * pos_1 + 0.5 * pos_2
        d_pos = pos_2 - pos_1
        rotation_matrix = np.array([(0, 1), (-1, 0)])
        ctrl_1 = linear_mid + rad * rotation_matrix @ d_pos
        ctrl_mid_1 = 0.5 * pos_1 + 0.5 * ctrl_1
        ctrl_mid_2 = 0.5 * pos_2 + 0.5 * ctrl_1
        bezier_mid = 0.5 * ctrl_mid_1 + 0.5 * ctrl_mid_2
        (x, y) = ax.transData.inverted().transform(bezier_mid)

        if rotate:
            # in degrees
            angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
            # make label orientation "right-side-up"
            if angle > 90:
                angle -= 180
            if angle < -90:
                angle += 180
            # transform data coordinate angle to screen coordinate angle
            xy = np.array((x, y))
            trans_angle = ax.transData.transform_angles(
                np.array((angle,)), xy.reshape((1, 2))
            )[0]
        else:
            trans_angle = 0.0
        # use default box of white with white border
        if bbox is None:
            bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
        if not isinstance(label, str):
            label = str(label)  # this makes "1" and 1 labeled the same

        t = ax.text(
            x,
            y,
            label,
            size=font_size,
            color=font_color,
            family=font_family,
            weight=font_weight,
            alpha=alpha,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            rotation=trans_angle,
            transform=ax.transData,
            bbox=bbox,
            zorder=1,
            clip_on=clip_on,
        )
        text_items[(n1, n2)] = t

    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )

    return text_items


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
    {'from': 'Brandon Park', 'to': 'Oakleigh', 'weight': 25, 'line': '693 Bus Line'},
]

lineColours = {
    # Train Lines
    'Glen Waverley': '#BA3B46',
    'Sandringham': '#F038FF',
    'Camberwell': '#FF8600',
    'Pakenham': '#faea3e',
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
bg_colour = '#D3D3D3'

for index in range(len(edges)):
    from_node = edges[index]['from']
    to_node = edges[index]['to']
    color = lineColours[edges[index]['line']]
    weight = edges[index]['weight']

    g.add_edge(from_node, to_node, color=color, weight=weight)

colors = nx.get_edge_attributes(g, 'color').values()
weights = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])

pos = {'Glen Waverley': (1.2768713098241284, 0.49920912491483405), 'CGS WH': (1.4265826300847813, 0.1204628887684871),
       'Mount Waverley': (0.7043105941642556, 0.7733282005439384), 'Richmond': (0.341812028442958, 0.4373730047276754),
       'Parliament': (-0.4284117911380293, 0.7517066156790655),
       'Melbourne Central': (-0.45435855635285616, 0.42191397468088576),
       'Flinders Street': (-0.42932311065271866, 0.08181531365151296),
       'Brighton Beach': (-0.665772732541814, -0.23509480230767532),
       'Camberwell': (0.07247908565059714, 0.8255351955388853), 'Oakleigh': (0.633506906308221, 0.12303939377628548),
       'Wheelers Hill Library': (1.1109175815449, -0.34135548220469414),
       'Chadstone': (0.11467939187567033, -0.7484751364978814),
       'Caulfield': (-0.12498201317170499, -0.3226959725728168), 'CGS CC': (-0.8083854616920082, -0.7323602688127431),
       'Brandon Park': (0.5691253741247339, -0.6003212036334155)}

# Draggable nodes utility
# pos = nx.layout.kamada_kawai_layout(g)
#
# plot = DraggableNodes(g, pos)
# plot.show()

fig, axes = plt.subplots()
axes.margins(0.20)

nx.draw_networkx_nodes(g, pos, node_color='black')

# Sorts the edges into their curvature
right_curved_edges = []
r_cmap = []

left_curved_edges = []
l_cmap = []

straight_edges = []
s_cmap = []

for edge in g.edges():
    edge_occurrences = [entry for entry in edges if
                        (edge[0] == entry['from'] and edge[1] == entry['to']) or
                        (edge[1] == entry['from'] and edge[0] == entry['to'])
                        ]

    edge_count = len(edge_occurrences)

    first = edge_occurrences[0] if edge_count > 0 else None
    second = edge_occurrences[1] if edge_count > 1 else None
    third = edge_occurrences[2] if edge_count > 2 else None

    if edge_count == 1:
        straight_edges.append((first['from'], first['to'], first))
        s_cmap.append(lineColours[first['line']])
    elif edge_count == 2:
        left_curved_edges.append((first['from'], first['to'], first))
        l_cmap.append(lineColours[first['line']])

        right_curved_edges.append((second['from'], second['to'], second))
        r_cmap.append(lineColours[second['line']])
    elif edge_count == 3:
        left_curved_edges.append((first['from'], first['to'], first))
        l_cmap.append(lineColours[first['line']])

        right_curved_edges.append((second['from'], second['to'], second))
        r_cmap.append(lineColours[second['line']])

        straight_edges.append((third['from'], third['to'], third))
        s_cmap.append(lineColours[third['line']])

# Draw edges

arc_radius = 0.25
nx.draw_networkx_edges(g, pos, ax=axes, edgelist=straight_edges, edge_color=s_cmap)
[
    custom_draw_networkx_edge_labels(
        g, pos, ax=axes,
        bbox=dict(boxstyle="round", ec=bg_colour, fc=bg_colour),
        edge_labels={(edge[0], edge[1]): edge[2]['weight']}, rotate=False, font_size=6,
        font_color=lineColours[edge[2]['line']]) for edge in straight_edges
]

nx.draw_networkx_edges(g, pos, ax=axes, edgelist=right_curved_edges, connectionstyle=f'arc3, rad = {arc_radius}',
                       arrows=True, edge_color=r_cmap)
[
    custom_draw_networkx_edge_labels(
        g, pos, ax=axes, rad=arc_radius,
        bbox=dict(boxstyle="round", ec=bg_colour, fc=bg_colour),
        edge_labels={(edge[0], edge[1]): edge[2]['weight']}, rotate=False, font_size=6,
        font_color=lineColours[edge[2]['line']]) for edge in right_curved_edges
]

nx.draw_networkx_edges(g, pos, ax=axes, edgelist=left_curved_edges, connectionstyle=f'arc3, rad = -{arc_radius}',
                       arrows=True, edge_color=l_cmap)
[
    custom_draw_networkx_edge_labels(
        g, pos, ax=axes, rad=-arc_radius,
        bbox=dict(boxstyle="round", ec=bg_colour, fc=bg_colour),
        edge_labels={(edge[0], edge[1]): edge[2]['weight']}, rotate=False, font_size=6,
        font_color=lineColours[edge[2]['line']]) for edge in left_curved_edges
]

# Add node labels

for node, (x, y) in pos.items():
    text(x - 0.06, y + 0.06, node, fontsize=6, ha='right', va='bottom')
    index = list(g.nodes()).index(node)
    text(x, y, index, fontsize=8, ha='center', va='center', color='white')

plt.axis("off")
fig.set_facecolor(bg_colour)
plt.show()
