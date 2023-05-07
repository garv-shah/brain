import networkx as nx
import matplotlib.pyplot as plt

from typing import Any


VertexId = Any


class DraggableNodes:
    currently_dragging: bool = False
    position_data: dict[VertexId, tuple[float, float]]
    dirty: bool = False
    G: nx.Graph

    def __init__(self, G: nx.Graph, initial_positions: dict[VertexId, tuple[float, float]] | dict[VertexId, list[float]]):
        self.G = G
        # networkx generates the position data as a two-element array, this doesn't really print very well so I'm using tuples
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
        # Find closest vertex and assume we're dragging that because I can't be bothered figuring out how to map the two co-ordinate systems onto each other
        closest = None
        for id, loc in self.position_data.items():
            x, y = loc[0], loc[1]
            distance = (((pos[0] - x) ** 2 + (pos[1] - y) ** 2)) ** (1/2)
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
        plt.ion()
        self.connect()
        nx.draw(self.G, self.position_data)
        plt.show()

        while True:
            if self.dirty:
                plt.clf()
                nx.draw(self.G, self.position_data)
                self.dirty = False

            plt.pause(1 / 60)


g = nx.Graph()

g.add_edge("C", "F", weight=6)
g.add_edge("C", "A", weight=4)
g.add_edge("F", "A", weight=5)
g.add_edge("F", "D", weight=1)
g.add_edge("F", "E", weight=6)
g.add_edge("A", "D", weight=7)
g.add_edge("A", "B", weight=2)
g.add_edge("E", "B", weight=5)
g.add_edge("D", "E", weight=6)
g.add_edge("D", "B", weight=6)

pos = nx.layout.kamada_kawai_layout(g, weight=None)
plot = DraggableNodes(g, pos)
plot.show()
