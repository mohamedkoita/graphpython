import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import csv

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

    #Retourner les relations sous forme d'objets
    def getServices(self):
        return self.services

    #Pour retourner les services sous forme de tableau
    def getServicesTab(self):
        tab = []
        for sv in self.services:
            tb = [sv.id, sv.type, sv.summary]
            tab.append(tb)
        return tab

    #Retourner les relations sous forme d'objets
    def getRelations(self):
        return self.relations

    #Pour retouner les relations sous forme de tableau
    def getRelationsTab(self):
        tab = []
        for rl in self.relations:
            rl.traffic['link'] = '\n'.join(rl.traffic['link'])
            tb = [rl.source.id, rl.dest.id, rl.traffic]
            tab.append(tb)
        return tab

    #Fonction pour exporter les données de l'architecture sous forme de csv
    def toCSV(self):

        tab = []
        for rl in self.relations:
            tb = [rl.source.summary, rl.dest.summary, rl.traffic['link']]
            tab.append(tb)

        with open('archi'+self.name+'.csv', mode='w') as archi_file:
            archi_writer = csv.writer(archi_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            archi_writer.writerow(['Source', 'Destination', 'Trafic'])
            for tb in tab:
                archi_writer.writerow(tb)



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
        G.add_node(svc[0], service=svc[2])

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

    nx.draw_networkx(G, pos, labels=nodes_labels, with_labels=True, font_size=10, node_size=5000, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.6, edge_labels=edges_labels, font_size=8)

    plt.show()
