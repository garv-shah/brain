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
        cmap = plt.cm.viridis(np.linspace(0, 1, g.number_of_edges()))
        nx.draw_networkx(self.G, self.position_data, with_labels=True)
        nx.draw_networkx_edges(self.G, self.position_data, edge_color=cmap)
        [nx.draw_networkx_edge_labels(self.G, self.position_data, edge_labels={e: i}, font_color=cmap[i]) for i, e in enumerate(g.edges())]
        plt.show()

        while True:
            if self.dirty:
                plt.clf()
                cmap = plt.cm.viridis(np.linspace(0, 1, g.number_of_edges()))
                nx.draw_networkx(self.G, self.position_data, with_labels=True)
                nx.draw_networkx_edges(self.G, self.position_data, edge_color=cmap)
                [nx.draw_networkx_edge_labels(self.G, self.position_data, edge_labels={e: i}, font_color=cmap[i]) for i, e in enumerate(g.edges())]
                self.dirty = False

            plt.pause(1 / 60)
