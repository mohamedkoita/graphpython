import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
from archi import *
from examples import *

#Ecrire une fonction d'acceuil qui va demander le projet qu'on veut executer et si on veut dessiner seulement le graphe
#Ou y ajouter l'export csv

#Fonctions relatives a la classe aux classes Architecture, Service et Relation
#Ici on entre le nom de l'architecture pour créer une nouvelle architecture
def createArchi(name):
    return Archi(name)

#Ici on entre comme parametres le tableau contenant les services et l'architecture
def createServices(architecture, services):
    for svc in services:
        service = Service(svc[0], svc[1], svc[2])
        architecture.addService(service)
        service.addArchi(architecture)

#Ici on entre le tableau initial contenant les relations et le tableau issus de la fonction createService
def createRelations(architecture, relations):
    services = architecture.getServices()
    for rel in relations:
        relx = Relation(services[rel[0]])
        relx.addDest(services[rel[1]])
        relx.addTraffic(rel[2])
        architecture.addRelation(relx)


#Fonctions relatives aux graphes
#Fonction permettant de creer les noeuds des graphes
def createNode(G, services):
    for svc in services:
        G.add_node(svc[0], purpose=svc[1], service=svc[2])

#Fonction permettant de creer les noeuds entre les graphes
#Ici, il faut trouver un moyens de modifier le tableau relations pour que chaque lien s'affiche a la ligne
def createEdge(G, relations):
    G.add_edges_from(relations)

#Fonction qui permet de dessiner le graphe avec l'architecture en paramètres
def drawGraph(architecture):

    #Creation du graphe
    G = nx.DiGraph()
    #Creation des noeuds
    createNode(G, architecture.getServicesTab())
    #Creation des relations entre les noeuds
    createEdge(G, architecture.getRelationsTab())

    nodes_labels = nx.get_node_attributes(G, 'service')
    edges_labels = nx.get_edge_attributes(G, 'link')

    pos = nx.spring_layout(G, k=10)
    fig= plt.figure()
    ax=fig.add_axes([0,0,1,1])

    color_map = []

    storage = ['DATABASE', 'SCHEMA', 'TABLE', 'TABLES', 'EVENT_BUS', 'AMQP', 'COLLECTION']

    for nb in range(G.number_of_nodes()):
        if G.nodes[nb]['purpose'] in storage :
            color_map.append('green')
        else:
            color_map.append('#1f78b4')


    nx.draw_networkx(G, pos, node_color=color_map, labels=nodes_labels, with_labels=True, font_size=10, node_size=5000, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.6, edge_labels=edges_labels, font_size=8)

    plt.show()
