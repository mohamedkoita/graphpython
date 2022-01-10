import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'WEB UI'], [1, 'REST', 'Registry'], [2, 'REST', 'Authentication'], [3, 'REST', 'ImageProvider'], [4, 'REST', 'Persistence'], [5, 'REST', 'Recommender']]

relations = [
[0, 1, {"link": ["POST /{name}/{location} ", " DELETE /{name}/{location}"]}],
[0, 2, {"link": ["POST /cart/add/{id} ", " POST /cart/remove/{id} ", " PUT /cart/{id} ", " POST /useractions/login ", " POST /useractions/logout ", " POST /useractions/placeorder ", " POST /useractions/isLoggedIn"] }],
[0, 3, {"link": ["POST /getProductImages ", " POST /getWebImages"]}],
[0, 4, {"link": ["GET /products ", " GET /categories ", " GET /users ", " GET /orders"] }],
[0, 5, {"link": ["POST /recommend/{uid}"]}],
[5, 4, {"link": ["GET /orders ", " GET /ordersitems"]}],
[2, 4, {"link": ["POST /products ", " POST /orders ", " POST /ordersitems"]}],
[3, 4, {"link": ["GET /generatedb ", " /GET products ", " GET/categories"]}]
]

teastore = createArchi("Teastore")

createServices(teastore, services)

createRelations(teastore, relations)

teastore.toCSV()

drawGraph(teastore)
