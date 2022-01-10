import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'gRPC/Event', 'API GATEWAY'], [1, 'gRPC/Event', 'Ordering'], [2, 'gRPC/Event', 'Basket'], [3, 'gRPC', 'Catalog'], [4, 'Event', 'Payment']]

relations = [
[0, 1, {"link": ["gRPC CreateOrderDraftFromBasket() "]}],
[0, 2, {"link": ["gRPC GetBasketById() ", "gRPC UpdateBasket() "] }],
[0, 3, {"link": ["gRPC getItemById() ", "gRPC getItemsById() "]}],
[1, 2, {"link": ["EVENT OrderStartedIntegrationEvent "]}],
[2, 1, {"link": ["EVENT UserCheckoutAcceptedIntegrationEvent "]}],
[1, 4, {"link": ["EVENT OrderStatusChangedToStockConfirmedIntegrationEvent "]}],
[4, 1, {"link": ["EVENT orderPaymentIntegrationEvent "]}],
[3, 1, {"link": ["EVENT ProductPriceChangedIntegrationEvent "]}]
]

eshop = createArchi("eShop")

createServices(eshop, services)

createRelations(eshop, relations)

eshop.toCSV()

drawGraph(eshop)
