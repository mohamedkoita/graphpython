import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Customer-service'], [2, 'REST', 'Vet-service'], [3, 'REST', 'Visit-service']]

relations = [
[0, 1, {"link": ["GET /owners/{ownerId} "]}],
[0, 2, {"link": ["GET /vet/vets "] }],
[0, 3, {"link": ["GET /pets/visits "]}]
]

petclinic = createArchi("Petclinic")

createServices(petclinic, services)

createRelations(petclinic, relations)

petclinic.toCSV()

drawGraph(petclinic)
