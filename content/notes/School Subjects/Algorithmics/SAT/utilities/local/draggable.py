from typing import Any
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import networkx as nx
import numpy as np

VertexId = Any


class DraggableNodes:
    currently_dragging: bool = False
    position_data: dict[VertexId, tuple[float, float]]
    edges: list[dict[str, Any]]
    line_data: dict[str, str]
    dirty: bool = False
    g: nx.Graph

    def __init__(
            self,
            g: nx.Graph,
            initial_positions: dict[VertexId, tuple[float, float]] | dict[VertexId, list[float]],
            edges: list[dict[str, Any]],
            line_data: dict[str, Any]
    ):
        self.g = g
        self.edges = edges
        self.line_data = line_data
        # networkx generates the position data as a two-element array, this doesn't really print very well, so I'm
        # using tuples
        self.position_data = {k: (v[0], v[1])
                              for k, v in initial_positions.items()}

    def on_button_down(self, _event):
        self.currently_dragging = True

    def on_button_up(self, _event):
        self.currently_dragging = False
        print()
        print(self.position_data)

    def on_mouse_move(self, event):
        if self.currently_dragging:
            vertex = self.vertex((event.xdata, event.ydata))
            if vertex is not None:
                # Move vertex to current mouse position
                self.position_data[vertex] = (event.xdata, event.ydata)

                # Trigger re-draw
                self.dirty = True

    def vertex(self, pos: tuple[int, int]) -> VertexId | None:
        # Find the closest vertex and assume we're dragging that because I can't be bothered figuring out how to map the
        # two co-ordinate systems onto each other
        closest = None
        for id, loc in self.position_data.items():
            x, y = loc[0], loc[1]
            distance = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** (1 / 2)
            if closest is None or distance < closest[0]:
                closest = (distance, id)

        if closest is not None:
            return closest[1]

        return None

    def connect(self):
        plt.gca().figure.canvas.mpl_connect("motion_notify_event", self.on_mouse_move)
        plt.gca().figure.canvas.mpl_connect("button_press_event", self.on_button_down)
        plt.gca().figure.canvas.mpl_connect("button_release_event", self.on_button_up)

    def show(self):
        fig, axes = plt.subplots()
        plt.ion()
        self.connect()
        draw(self.g, self.position_data, axes)
        plt.show()

        while True:
            if self.dirty:
                plt.clf()
                draw(self.g, self.position_data, axes)
                self.dirty = False

            plt.pause(1 / 60)


def draw(g, pos, axes):
    axes.margins(0.20)

    nx.draw_networkx_nodes(g, pos, node_color='black')

    cmap = plt.cm.viridis(np.linspace(0, 1, g.number_of_edges()))
    nx.draw_networkx_edges(g, pos, edge_color=cmap)
    [nx.draw_networkx_edge_labels(g, pos, edge_labels={e: i}, font_color=cmap[i]) for
     i, e in enumerate(g.edges())]

    for node, (x, y) in pos.items():
        text(x - 0.06, y + 0.06, node, fontsize=6, ha='right', va='bottom')
        index = list(g.nodes()).index(node) + 1
        text(x, y, index, fontsize=8, ha='center', va='center', color='white')

    plt.axis("off")
