import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Inventory'], [2, 'REST', 'Account'], [3, 'REST', 'Product'], [4, 'REST', 'Shopping-Cart'], [5, 'REST', 'Order'], [6, 'REST', 'Payment'], [7, 'REST', 'Store']]

relations = [
[0, 1, {"link": ["GET /api/inventory/{productId} "]}],
[0, 2, {"link": ["GET /uaa ", "POST /logout "] }],
[0, 3, {"link": ["GET /api/product/{productId} "]}],
[0, 4, {"link": ["GET /api/cart/cart ", "POST /api/cart/events ", "POST /api/cart/checkout "]}],
[0, 5, {"link": ["GET /api/order/orders/{orderId} ", "GET /api/order/user/{userId}/orders "]}],
[4, 1, {"link": ["GET /inventory/{productId} "]}],
[4, 5, {"link": ["EVENT SHOPPING_TO_ORDER "]}],
[4, 6, {"link": ["EVENT SHOPPING_TO_PAYMENT "]}],
[5, 1, {"link": ["PUT /inventory/{productId}/decrease?n={amount} "]}],
]

blueprint = createArchi("Blueprint")

createServices(blueprint, services)

createRelations(blueprint, relations)

blueprint.toCSV()

drawGraph(blueprint)
