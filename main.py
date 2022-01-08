import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

class Archi:
    services = []
    relations = []

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def addService(self, service):
        self.services.append(service)
        service.addArchi(self)

    def addRelation(self, relation):
        self.relations.append(relation)

    def getServices(self):
        return self.services

    def getRelations(self):
        return self.relations

class Service:
    def __init__(self, id, type, summary):
        self.id = id
        self.type = type
        self.summary = summary

    def addType(self, type):
        self.type = type

    def addSummary(self, summary):
        self.summary = summary

    def addArchi(self, archi):
        self.archi = archi

class Relation:
    def __init__(self, source):
        self.source = source

    def addSource(self, source):
        self.source = addSource

    def addDest(self, dest):
        if self.source.archi == dest.archi:
            self.dest = dest

    def addTraffic(self, traffic):
        self.traffic = traffic

#Fonctions relatives a la classe aux classes Architecture, Service et Relation
#Ici on entre le nom de l'architecture pour créer une nouvelle architecture
def createArchi(name):
    return Archi(name)

#Ici on entre comme parametres le tableau contenant les services et l'architecture
def createServices(architecture, services):
    services_ = []
    for svc in services:
        service = Service(svc[0], svc[1], svc[2])
        teastore.addService(service)
        service.addArchi(architecture)
        services_.append(service)
    return services_

#Ici on entre le tableau initial contenant les relations et le tableau issus de la fonction createService
def createRelations(services, relations):
    for rel in relations:
        relx = Relation(services[rel[0]])
        relx.addDest(services[rel[1]])
        relx.addTraffic(rel[2])
        teastore.addRelation(relx)


#Fonctions relatives aux graphes
#Fonction permettant de creer les noeuds des graphes
def createNode(G, services):
    for svc in services:
        G.add_node(svc[0], service=svc[2])

#Fonction permettant de creer les noeuds entre les graphes
#Ici, il faut trouver un moyens de modifier le tableau relations pour que chaque lien s'affiche a la ligne
def createEdge(G, relations):
    G.add_edges_from(relations)


#Fonction pour dessiner un graphe
def drawGraph(G):
    nodes_labels = nx.get_node_attributes(G, 'service')
    edges_labels = nx.get_edge_attributes(G, 'link')

    pos = nx.spring_layout(G)
    fig= plt.figure()
    ax=fig.add_axes([0,0,1,1])

    nx.draw_networkx(G, pos, labels=nodes_labels, with_labels=True, node_size=5000)
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.5, font_size=8, edge_labels=edges_labels)

    plt.show()
