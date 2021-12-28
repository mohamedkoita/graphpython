import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

services = [[1, 'WEB UI'], [2, 'Registry'], [3, 'Authentication'], [4, 'ImageProvider'], [5, 'Persistence'], [6, 'Recommender']]

relations = [
[1, 2, {"link": "POST /{name}/{location} \n DELETE /{name}/{location}"}],
[1, 3, {"link": "POST /cart/add/{id} \n POST /cart/remove/{id} \n PUT /cart/{id} \n POST /useractions/login \n POST /useractions/logout \n POST /useractions/placeorder \n POST /useractions/isLoggedIn", }],
[1, 4, {"link": "POST /getProductImages \n POST /getWebImages"}],
[1, 5, {"link": "GET /products \n GET /categories \n GET /users \n GET /orders" }],
[1, 6, {"link": "POST /recommend/{uid}"}],
[6, 5, {"link": "GET /orders \n GET /ordersitems"}],
[3, 5, {"link": "POST /products \n POST /orders \n POST /ordersitems"}],
[4, 5, {"link": "GET /generatedb \n /GET products \n GET/categories"}]
]

def createNode(services):
    for svc in services:
        G.add_node(svc[0], service=svc[1])

def createEdge(relations):
    G.add_edges_from(relations)

createNode(services)

createEdge(relations)


nodes_labels = nx.get_node_attributes(G, 'service')
edges_labels = nx.get_edge_attributes(G, 'link')

pos = nx.spring_layout(G)
fig= plt.figure()
ax=fig.add_axes([0,0,1,1])

nx.draw_networkx(G, pos, labels=nodes_labels, with_labels=True, node_size=5000)
nx.draw_networkx_edge_labels(G, pos, label_pos=0.5, font_size=8, edge_labels=edges_labels)

plt.show()
