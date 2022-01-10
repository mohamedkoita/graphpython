import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Authentication'], [2, 'REST', 'Notification'], [3, 'REST', 'Account'], [4, 'REST', 'Statistics']]

relations = [
[0, 1, {"link": ["GET /uaa"]}],
[0, 2, {"link": ["GET /notifications "] }],
[0, 3, {"link": ["GET /accounts "]}],
[0, 4, {"link": ["GET /statistics "]}],
[2, 3, {"link": ["GET /accounts/{accountname} "]}],
[3, 1, {"link": ["POST /uaa/users "]}],
[3, 4, {"link": ["PUT /statistics/{accountname} "]}]
]

piggy = createArchi("Piggymetrics")

createServices(piggy, services)

createRelations(piggy, relations)

piggy.toCSV()

drawGraph(piggy)
