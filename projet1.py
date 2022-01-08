import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'WEB UI'], [1, 'REST', 'Registry'], [2, 'REST', 'Authentication'], [3, 'REST', 'ImageProvider'], [4, 'REST', 'Persistence'], [5, 'REST', 'Recommender']]

relations = [
[0, 1, {"link": "POST /{name}/{location} \n DELETE /{name}/{location}"}],
[0, 2, {"link": "POST /cart/add/{id} \n POST /cart/remove/{id} \n PUT /cart/{id} \n POST /useractions/login \n POST /useractions/logout \n POST /useractions/placeorder \n POST /useractions/isLoggedIn", }],
[0, 3, {"link": "POST /getProductImages \n POST /getWebImages"}],
[0, 4, {"link": "GET /products \n GET /categories \n GET /users \n GET /orders" }],
[0, 4, {"link": "POST /recommend/{uid}"}],
[5, 4, {"link": "GET /orders \n GET /ordersitems"}],
[2, 4, {"link": "POST /products \n POST /orders \n POST /ordersitems"}],
[3, 4, {"link": "GET /generatedb \n /GET products \n GET/categories"}]
]

G = nx.Graph()

createNode(G, services)

createEdge(G, relations)

drawGraph(G)
