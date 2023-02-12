import networkx as nx
import matplotlib.pyplot as plt
import re


def edges_from_dot(filen):
    # edge were tables generated from .dot files exported from edgy
    # using a regex to extract wanted information
    edges = []
    regex = '"(.)" -- "(.)"( "label "="(.)"(,"color "="(.∗)")?.*)?;'  # example: "a" -- "b"["label"="9"];
    with open(filen, "r") as file:
        for line in file:
            # only on lines describing edges
            match = re.match(regex, line)
            if match:
                # remove intermediary group
                a, b, _, weight, _, color = match.groups()

                # apply attributes
                settings = dict()
                if weight is not None:
                    settings["weight"] = weight
                edges.append((a, b, settings))

    return edges


def draw(graph):
    plt.figure()
    plt.axis("off")

    # style options
    options = {
        "node_size": 650,
        "width": 2,
        "with_labels": True,
    }

    # draw graph verticies and edges
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, **options)

    # draw weight values
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()


def graph_from_dot(filen, show=True):
    graph = nx.Graph()
    graph.add_edges_from(edges_from_dot(filen))
    return graph


if __name__ == "__main__":
    graph = graph_from_dot("project.dot")
    draw(graph)
