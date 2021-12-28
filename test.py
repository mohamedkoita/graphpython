import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set

from grave import plot_network

network = nx.powerlaw_cluster_graph(50, 1, .2)
dom_set = min_weighted_dominating_set(network)

for node, node_attrs in network.nodes(data=True):
    node_attrs['is_dominator'] = True if node in dom_set else False

def color_dominators(node_attrs):
    if node_attrs.get('is_dominator', False):
        return {'color': 'red'}
    else:
        return {'color': 'black'}

fig, ax = plt.subplots()
plot_network(network, node_style=color_dominators)
plt.show()
