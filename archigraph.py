import regex
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
from archi import *
from examples import *
from metrics import *


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
def createServicesRelations(architecture, relations):
    services = architecture.getServices()
    for rel in relations:
        relx = ServiceRelation(services[rel[0]])
        relx.addDest(services[rel[1]])
        relx.addTraffic(rel[2])
        architecture.addServicesRelation(relx)

#Ici on entre comme parametres le tableau contenant la persistence et l'architecture
def createPersistences(architecture, persistences):
    for svc in persistences:
        persistence = Persistence(svc[0], svc[1], svc[2])
        architecture.addPersistence(persistence)
        persistence.addArchi(architecture)

#Ici on entre le tableau initial contenant les relations de la persistence et le tableau issus de la fonction createService
def createPersistencesRelations(architecture, relations):
    persistences = architecture.getPersistences()
    for rel in relations:
        relx = PersistenceRelation(persistences[rel[0]])
        relx.addDest(persistences[rel[1]])
        relx.addTraffic(rel[2])
        architecture.addPersistenceRelation(relx)


#Fonctions relatives aux graphes
#Fonction permettant de creer les noeuds des graphes
def createNode(G, services):
    for svc in services:
        G.add_node(svc[0], purpose=svc[1], service=svc[2])

#Fonction permettant de creer les noeuds entre les graphes
#Ici, il faut trouver un moyens de modifier le tableau relations pour que chaque lien s'affiche a la ligne
def createEdge(G, relations):
    G.add_edges_from(relations)

#Fonction pour créer le graphe sans le dessiner et retourne le graphe
def createGraph(architecture, purpose):

    #Creation du graphe
    G = nx.DiGraph()
    relations = architecture.getServicesRelationsTab()
    components = architecture.getServicesTab()

    if purpose == 1:
        #Creation des noeuds
        createNode(G, components)
        #Creation des relations entre les noeuds
        createEdge(G, relations)
    elif purpose == 2:
        #Creation des noeuds
        createNode(G, architecture.getPersistencesTab())
        #Creation des relations entre les noeuds
        createEdge(G, architecture.getPersistencesRelationsTab())



    nodes_labels = nx.get_node_attributes(G, 'service')
    edges_labels = nx.get_edge_attributes(G, 'link')

    return [G, relations, components]

#Fonction qui permet de dessiner le graphe avec l'architecture en paramètres
def drawGraph(G):

    # #Creation du graphe
    # G = nx.DiGraph()
    #
    # if purpose == 1:
    #     #Creation des noeuds
    #     createNode(G, architecture.getServicesTab())
    #     #Creation des relations entre les noeuds
    #     createEdge(G, architecture.getServicesRelationsTab())
    # elif purpose == 2:
    #     #Creation des noeuds
    #     createNode(G, architecture.getPersistencesTab())
    #     #Creation des relations entre les noeuds
    #     createEdge(G, architecture.getPersistencesRelationsTab())
    #
    #
    #
    nodes_labels = nx.get_node_attributes(G, 'service')
    edges_labels = nx.get_edge_attributes(G, 'link')

    pos = nx.spring_layout(G, k=10)
    fig= plt.figure()
    ax=fig.add_axes([0,0,1,1])

    color_map = []

    storage = ['DATABASE', 'SCHEMA', 'TABLE', 'TABLES', 'COLLECTION']
    facade = ['FACADE']
    event = [ 'EVENT_BUS', 'MESSAGE_BROKER']

    for nb in range(G.number_of_nodes()):
        if G.nodes[nb]['purpose'] in storage :
            color_map.append('green')
        elif G.nodes[nb]['purpose'] in facade :
            color_map.append('red')
        elif G.nodes[nb]['purpose'] in event :
            color_map.append('brown')
        else:
            color_map.append('#1f78b4')


    nx.draw_networkx(G, pos, node_color=color_map, labels=nodes_labels, with_labels=True, font_size=10, node_size=5000, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.6, edge_labels=edges_labels, font_size=8)

    plt.show()

#Fonction qui permet de retouner toutes les metriques de tous les projets dans un fichier CSV
def AllInCsvFile():
    #récupérer tous les projets et les ajouter un a un dans le CSV des métriques
    tab = []

    for option in range(1, 13):

        project = createArchi(globals()[f"projet{option}"]["name"])

        createServices(project, globals()[f"projet{option}"]["services"])

        createServicesRelations(project, globals()[f"projet{option}"]["relations"])

        metrics = calculateMetrics(project)


        #tb Nom du projet, DTU, SDBI, SIC, DSS, TSS, CDD
        tb = [project.getName(), metrics[0]['dtu'] , metrics[1]['sdbi'], metrics[2]['sic'], metrics[3]['acu'], metrics[4]['dss'], metrics[5]['tss'], metrics[6]['cdd']]
        tab.append(tb)

    with open('Metrics.csv', mode='w+') as metrics_file:
        metrics_writer = csv.writer(metrics_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        metrics_writer.writerow(['Nom du projet', 'DTU', 'SDBI', 'SIC', 'ACU', 'DSS', 'TSS', 'CDD'])
        for tb in tab:
            metrics_writer.writerow(tb)
