import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'Workflow service'], [1, 'REST', 'Package Service'], [2, 'REST', 'Drone Scheduler'], [3, 'REST', 'Delivery service'], [4, 'Event', 'Ingestion service']]

relations = [
[0, 1, {"link": ["PUT /api/package/{packageId} "]}],
[0, 2, {"link": ["PUT /api/dronedeliveries/{id} "] }],
[0, 3, {"link": ["PUT /api/deliveries/{id} "]}],
[4, 0, {"link": ["EVENT OperationEvent "]}]
]

mspnp = createArchi("Mspnp")

createServices(mspnp, services)

createRelations(mspnp, relations)

mspnp.toCSV()

drawGraph(mspnp)
