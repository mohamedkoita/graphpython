import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'gRPC', 'Payment'], [1, 'gRPC', 'Order'], [2, 'gRPC', 'Product'], [3, 'gRPC/REST', 'Sku']]

relations = [
[1, 0, {"link": ["gRPC NewCharge ", "gRPC RefundCharge "]}],
[1, 3, {"link": ["gRPC Get ", "gRPC GetWithInventoryLock "] }],
[2, 3, {"link": ["gRPC ProductData "]}],
[3, 2, {"link": ["gRPC Get "]}]
]

digota = createArchi("Digota")

createServices(digota, services)

createRelations(digota, relations)

digota.toCSV()

drawGraph(digota)
