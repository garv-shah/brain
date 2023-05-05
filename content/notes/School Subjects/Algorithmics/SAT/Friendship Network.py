import algorithmx
from algorithmx.networkx import add_graph
import webbrowser
import networkx as nx

server = algorithmx.http_server(port=4040)
canvas = server.canvas()

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


def start():
    total_cost = 0
    canvas.label('title').remove()
    edge_list = []
    node_list = []

    # create node and edge list
    for index in range(len(edges)):
        edge = edges[index]
        edge_list.append([edge['from'], edge['to'], index])
        node_list.append(edge['from'])
        node_list.append(edge['to'])

    # remove duplicates from node_list
    node_list = list(dict.fromkeys(node_list))

    canvas.nodes(node_list).add()
    canvas.edges(edge_list).add()

    for index in range(len(edge_list)):
        current_edge = canvas.edge(edge_list[index])
        current_edge.color(lineColours[edges[index]['line']])
        current_edge.label().add(text=edges[index]['weight'])

    for index in range(len(node_list)):
        node = node_list[index]

        canvas.node(node).label('name').add(text=node,color='black')
        canvas.node(node).label().add(text=str(index + 1))


    # canvas.nodes().color('gray')
    # canvas.pause(1)
    #
    # n = "A"
    # g.nodes[n]['seen'] = True
    # seen = [n]
    # canvas.node(n).color('dark-gray')
    #
    # while len(seen) < len(g.nodes):
    #     smallest = {"node": None, "weight": float('inf')}
    #     for node in seen:
    #         for n2 in g.neighbors(node):
    #             weight = g.edges[node, n2]['weight']
    #             if weight < smallest['weight'] and n2 not in seen:
    #                 smallest = {"node": n2, "weight": weight}
    #                 n = node
    #
    #     canvas.edge((n, smallest['node'])).traverse('red').pause(0.5)
    #     n = smallest['node']
    #     total_cost += smallest['weight']
    #     seen.append(n)
    #     canvas.node(n).highlight().size('1.25x').pause(0.5)
    #     canvas.node(n).color('dark-gray')
    #
    # canvas.label('title').add(text=f'MST Cost: {total_cost}')


canvas.onmessage('start', start)
webbrowser.open('http://localhost:4040')
server.start()
