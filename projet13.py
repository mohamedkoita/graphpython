import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'Front End'], [1, 'REST', 'Payment'], [2, 'REST', 'Catalogue'], [3, 'REST', 'Orders'], [4, 'REST', 'Users'], [5, 'REST', 'Carts'], [6, 'REST', 'Shipping'], [7, 'EVENT', 'Queue-Master']]

relations = [
[0, 2, {"link": ["GET /catalogue ", "GET /catalogue/images ", "GET /tags "]}],
[0, 3, {"link": ["GET /orders/* ", "POST /orders "] }],
[0, 4, {"link": ["GET /customers ", "GET /customers/{id} ", "GET /cards ", "GET /card ", "GET /address ", "POST /cards ", "GET /cards/{id} ", "POST /register ", "GET /login "]}],
[0, 5, {"link": ["GET /cart ", "DELETE /cart ", "POST /cart ", "POST /cart/update ", "DELETE /cart/{id} "]}],
[3, 1, {"link": ["POST /paymentAuth "]}],
[3, 6, {"link": ["POST /shipping "]}],
[6, 7, {"link": ["EVENT shipping-task "]}]
]

msdemo = createArchi("MSdemo")

createServices(msdemo, services)

createRelations(msdemo, relations)

msdemo.toCSV()

drawGraph(msdemo)
