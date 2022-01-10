import networkx as nx
import matplotlib.pyplot as plt
from main import *

services = [[0, 'gRPC/REST', 'FRONTEND'], [1, 'gRPC/REST', 'Cart'], [2, 'gRPC/REST', 'Currency'], [3, 'gRPC', 'Shipping'], [4, 'gRPC', 'Payment'], [5, 'gRPC/REST', 'Checkout'], [6, 'gRPC', 'Recommandation'], [7, 'gRPC', 'Email'], [8, 'gRPC/REST', 'Product Catalog'], [9, 'gRPC', 'Ad']]

relations = [
[0, 1, {"link": ["POST /cart ", "POST /cart/empty ", "GET /cart ", "gRPC addItem() ", "gRPC getCart() ", "gRPC emptyCart() "]}],
[0, 2, {"link": ["POST /setCurrency ", "gRPC getSupportedCurrencies() ", "gRPC convert()"] }],
[0, 3, {"link": ["gRPC getQuote() "]}],
[0, 5, {"link": ["POST /cart/checkout ", "gRPC placeOrder() "]}],
[0, 6, {"link": ["gRPC ListRecommandations() "]}],
[0, 8, {"link": ["GET /product/{id} ", "gRPC GetProduct", "gRPC ListProducts "]}],
[0, 9, {"link": ["gRPC getAds "]}],
[5, 1, {"link": ["gRpc getCart ", "gRPC emptyCart"]}],
[5, 2, {"link": ["gRPC convert "]}],
[5, 3, {"link": ["gRPC shipOrder ", "gRPC getQuote "]}],
[5, 4, {"link": ["gRPC Pcharge "]}],
[5, 7, {"link": ["gRPC sendOrderConfirmation "]}],
[5, 8, {"link": ["gRPC getProduct "]}],
[6, 8, {"link": ["gRPC ListProducts "]}],
]

gcpdemo = createArchi("Gcpdemo")

createServices(gcpdemo, services)

createRelations(gcpdemo, relations)

gcpdemo.toCSV()

drawGraph(gcpdemo)
