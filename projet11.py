import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'WEB UI'], [1, 'REST', 'Quote'], [2, 'REST', 'Catalogue'], [3, 'REST', 'Order'], [4, 'REST', 'Dealer'], [5, 'REST', 'Shipment']]

relations = [
[0, 1, {"link": ["GET /quote ", "POST /quote ", "GET /quote/{quoteId} ", "DELETE /quote/{quoteId} ", "PUT /quote/{quoteId} ", "GET /quote/bydealer/{dealername} "]}],
[0, 2, {"link": ["GET /catalogue", "POST /catalogue ", "GET /catalogue/{skuNumber} ", "DELETE /catalogue/{skuNumber} ", "PUT /catalogue/{skuNumber} "] }],
[0, 3, {"link": ["GET /orders ", "POST /orders ", "GET /orders/{orderId} ", "PUT /orders/{orderId} ", "DELETE /orders/{orderId} ", "PUT /orders/{orderId}/status ", "POST /orders/{orderId}/events "]}],
[0, 4, {"link": ["GET /dealer ", "POST /dealer ", "GET /dealer/{dealerName} ", "DELETE /dealer/{dealerName} ", "PUT /dealer/{dealerName} "]}],
[0, 5, {"link": ["GET /shipments ", "POST /shipments ", "GET /shipments/{id} ", "DELETE /shipments/{id} ", "PUT /shipments/{id} ", "GET /shipments/{id}/events "]}]
]

partsu = createArchi("PartsU")

createServices(partsu, services)

createRelations(partsu, relations)

partsu.toCSV()

drawGraph(partsu)
