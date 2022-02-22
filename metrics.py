import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
from archi import *
from examples import *

#On va faire une boucle sur chaque service, et pour chaque service, on va compter le nombre de fois ou il appatait comme premier parametre dans les tableaux des relations

#Chaque fonction de ce fichier calculera une metrique precise
#OK
#Fan in fan out des services
def fanInFanOut(architecture):

    services = architecture.getServices()
    relations = architecture.getServicesRelations()

    # tab = ['Service', 'FanIn', 'FanOut']
    tab = []

    for service in services:
        fanIn = 0
        fanOut = 0

        for relation in relations:

            if service.id == relation.source.id:
                #augmenter la valeur du fanOut
                fanOut += 1

            if service.id == relation.dest.id:
                #augmenter la valeur du fanIn
                fanIn += 1

        #Une fois on fini de parcourir toutes les relations pour un service donné, on fait le append sur le tableau
        tb = [service.summary, fanIn, fanOut]
        tab.append(tb)

    return tab

#OK
#Database Type Utilization
def DTUmetrics(architecture):

    persistencesRel = architecture.getPersistencesRelationsTab()
    db_per_service_links = 0
    total_service_to_db_links = len(persistencesRel)

    for val in persistencesRel:
        if val[2]['link'] == 'DATABASE_SERVER_BY_SERVICE':
            db_per_service_links += 1

    db_type_utilization = db_per_service_links / total_service_to_db_links

    return db_type_utilization

#OK
#Shared Database Interactions
def SDBImetrics(architecture):

    service_inter_shared_db = 0
    total_service_inter = 0
    shared_db_interactions = 0

    persistencesRel = architecture.getPersistencesRelationsTab()
    total_service_to_db_links = len(persistencesRel)

    servicesRel = architecture.getServicesRelationsTab()
    total_service_inter = len(servicesRel)

    for val in persistencesRel:
        if val[2]['link'] == 'SHARED_DATABASE':
            service_inter_shared_db += 1

    shared_db_interactions = service_inter_shared_db / total_service_inter

    return shared_db_interactions

#OK
#Service Interaction via Intermediary Component
#Ici on va rechercher toutes les transactions d'événements et de message que les services vont transmettre via message broker | pub/sub | stream
def SICmetrics(architecture):

    service_inter_via_mb_pb_st = 0
    service_interaction_component = 0
    total_service_inter = 0

    servicesRel = architecture.getServicesRelationsTab()
    total_service_inter = len(servicesRel)
    # print(total_service_inter)

    #service connections via messages brokers | pub/sub | stream - Pas de grpc car grpc c'est appel direct, on peut le mettre dans asynchrone mais pas via un composant
    for val in servicesRel:
        if "EVENT" in val[2]['link']:
            service_inter_via_mb_pb_st += 1

    print(service_inter_via_mb_pb_st)
    print(total_service_inter)

    service_interaction_component = service_inter_via_mb_pb_st / total_service_inter

    return service_interaction_component

#Asynchronous Communication Utilization
#Non applicable car tous les appels asynchrones de tous les projets sont fait via message broker | pub/sub | stream non [API | Polling |DirectCalls | SharedDB]
def ACUmetrics(architecture):

    #La proportion des interconnections de service asynchrones

    return "Non applicable"

#OK
#Direct Service Sharing
def DSSmetrics(architecture):
    #Ecrire un algorithme pour decouvrir les services directement partages
    #un service directement partagé est un microservice qui est directement lié à et requis par plus d'un autre service

    shared_services = 0
    shared_services_connectors = 0
    total_services = len(architecture.getServicesTab())
    total_services_inter = len(architecture.getServicesRelationsTab())
    direct_service_sharing = 0

    #On recupere tous les services
    services = architecture.getServices()

    #On recupere toutes les relations entre les services
    relations = architecture.getServicesRelations()

    #Pour chaque service on récupère les services avec lesquels il est en relation
    for service in services:
        for relation in relations:
            if service == relation.getSource():
                service2 = relation.getDest()
                #On verifie si chacun de ces services emet une requete vers le premier service
                for rel in relations:
                    if rel.getSource() == service2 and rel.getDest() == service:
                        shared_services += 1
                        shared_services_connectors += 2

    direct_service_sharing = (shared_services/total_services + shared_services_connectors/total_services_inter)/2


    return direct_service_sharing

#OK
#Transitevely Shared Services
def TSSmetrics(architecture):
    #Ecrire un algorithme pour decouvrir un algorithme partage de maniere transitive
    #un service partagé de manière transitive est un microservice qui est lié à d'autres services via au moins un service intermédiaire

    #Un niveau supérieur par rapport a DSS
    transit_services = 0
    transit_services_connectors = 0
    total_services = len(architecture.getServicesTab())
    total_services_inter = len(architecture.getServicesRelationsTab())
    transitively_service_sharing = 0
    tab = []
    rels = []

    #On recupere tous les services
    services = architecture.getServices()

    #On recupere toutes les relations entre les services
    relations = architecture.getServicesRelations()

    #Pour chaque service on récupère les services avec lesquels il est en relation
    for service in services:
        for relation in relations:
            if service == relation.getSource():
                service2 = relation.getDest()
                #On verifie si chacun de ces services emet une requete vers le premier service
                for rel in relations:
                    if rel.getSource() == service2:
                        service3 = rel.getDest()
                        for relx in relations:
                            if relx.getDest() == service and service not in tab:
                                tab.append(service)
                                transit_services += 1

                                if relation not in rels:
                                    rels.append(relation)
                                    transit_services_connectors +=1

                                if rel not in rels:
                                    rels.append(rel)
                                    transit_services_connectors +=1

                                if relx not in rels:
                                    rels.append(relx)
                                    transit_services_connectors +=1

    return transitively_service_sharing

#OK
#Cyclic dependencies detection
def CDDmetrics(G):
    try:
        cycle = nx.find_cycle(G, orientation="original")
        return 1
    except Exception as e:
        return 0
