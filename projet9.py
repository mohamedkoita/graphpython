import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'Catalogue'], [1, 'REST', 'Ratings'], [2, 'REST', 'Cart'], [3, 'EVENT', 'Dispatch'], [4, 'REST', 'Shipping'], [5, 'REST', 'Users'], [6, 'REST', 'Payments']]

relations = [
[1, 0, {"link": ["GET /product/{sku} "]}],
[2, 0, {"link": ["GET /product "] }],
[4, 2, {"link": ["POST /shipping/{id} "]}],
[6, 2, {"link": ["DELETE /cart/{id} "]}],
[6, 3, {"link": ["EVENT Dispatch "]}],
[6, 5, {"link": ["GET /check/{id} ", "POST /check/{id} "]}]
]

robotshop = createArchi("Robot-shop")

createServices(robotshop, services)

createRelations(robotshop, relations)

robotshop.toCSV()

drawGraph(robotshop)
