import networkx as nx
import matplotlib.pyplot as plt
import archigraph as arc
from pprint import pprint
from archi import *
from examples import *


def calculateMetrics(architecture):

    Gr = arc.createGraph(architecture, 1)
    G = Gr[0]
    relations = Gr[1]
    components = Gr[2]
    total_service_to_db_links = []
    nb_total_service_to_db_links = 0
    nb_shared_db_interconnexions = 0
    nb_total_service_interconnections = 0
    nb_service_to_facade_link = 0
    facade_links = []
    ##Peut etre problematique si aucune facade
    facade_ids = []
    service_interaction_with_inter_comp = 0
    total_services = []
    nb_total_services = 0


    #Calcul du nombre de connecteurs service a base de données
    for val in relations:
        if 'FULL_DATABASE' in val[2]['link'] or 'SCHEMA' in val[2]['link'] or 'COLLECTION' in val[2]['link'] or 'TABLE' in val[2]['link']:
            total_service_to_db_links.append(val[2]['link'])
            nb_total_service_to_db_links += 1

    #Calcul du nombre de services interconnexions avec base de données partagée
    for rel in total_service_to_db_links:
        if 'FULL_DATABASE' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'SCHEMA' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'COLLECTION' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'TABLE' in rel:
            nb_shared_db_interconnexions += 1

    # Calculs du nombre de connecteurs facade à service
    for comp in components:
        if comp[1] == "FACADE":
            facade_ids.append(comp[0])


    for fac_id in facade_ids:
        facade_links += list(G.out_edges(fac_id))
        nb_service_to_facade_link = len(facade_links)


    # Calcul du nombre de composants service
    for comp in components:
        if comp[1] == "SERVICE":
            total_services.append(comp)
            nb_total_services += 1

    #Calcul du nombre total d'interconnexions entre services
    nb_total_service_interconnections = len(relations) - nb_total_service_to_db_links - nb_service_to_facade_link + nb_shared_db_interconnexions

    #Calcul du DTU
    #Ici on recupere tous les connecteurs qui lie un service à une base de données en full_database
    full_database_links = []
    nb_full_database_links = 0
    for rel in relations:
        # if 'FULL_DATABASE' in rel[2]['link'] or 'COLLECTION' in rel[2]['link']or 'SCHEMA' in rel[2]['link']:
        if 'FULL_DATABASE' in rel[2]['link']:
            full_database_links.append(rel[2]['link'])
            nb_full_database_links += 1

    nb_db_per_service_links = 0
    for x in full_database_links:
        if full_database_links.count(x) == 1:
            nb_db_per_service_links += 1
    # print(nb_db_per_service_links)
    # print(nb_total_service_to_db_links)

    db_type_utilization = nb_db_per_service_links / nb_total_service_to_db_links

    #Calcul du SDBI
    if nb_total_service_interconnections == 0:
        shared_db_interactions = 0
    else:
        shared_db_interactions = nb_shared_db_interconnexions / nb_total_service_interconnections

    #Calcul du SIC
    nb_service_inter_via_mb_pb_st = 0
    for comp in components:
        if comp[1] == "MESSAGE_BROKER" or comp[1] == "EVENT_BUS":
            mb_pb_st_id = comp[0]
            FromMB = G.out_edges(mb_pb_st_id)
            ToMB = G.in_edges(mb_pb_st_id)
            nb_service_inter_via_mb_pb_st += len(FromMB) + len(ToMB)
            # print(FromMB)
            # print(ToMB)

    if nb_total_service_interconnections == 0:
        service_interaction_with_inter_comp = 0
    else:
        service_interaction_with_inter_comp = nb_service_inter_via_mb_pb_st / nb_total_service_interconnections


    #Calcul du ACU
    #Rechercher les component asynchrones
    if nb_total_service_interconnections == 0:
        asynchronous_service_utilization = 0
    else:
        asynchronous_service_utilization = nb_shared_db_interconnexions / nb_total_service_interconnections


    #Calcul du DSS
    #get service to services relations without service to db and service to facade
    sv_to_sv = []
    for val in relations:
        if 'FULL_DATABASE' not in val[2]['link'] and 'SCHEMA' not in val[2]['link'] and 'COLLECTION' not in val[2]['link'] and 'TABLE' not in val[2]['link'] and val[0] not in facade_ids :
            sv_to_sv.append(val)

    ##Test
    # print(sv_to_sv)

    #Les services cible de toutes les relations
    services_cible = []
    for ser in sv_to_sv:
        services_cible.append(ser[1])

    #recherche des services partagés qui sont cible plusieurs fois et le nombre de leurs relations
    sharedServices = []
    numberSharedService = 0
    sharedServicesLinks = 0


    for y in set(services_cible):
        sumSharedServices = services_cible.count(y)
        if sumSharedServices > 1:
            serviceSharedLinks = True
            sharedServices.append(sumSharedServices)
            numberSharedService = len(sharedServices)
            sharedServicesLinks = sum(sharedServices)

    # print(sharedServices)
    # print(sharedServicesLinks)

    if nb_total_service_interconnections != 0:
        directly_shared_services = ((numberSharedService/nb_total_services) + (sharedServicesLinks/nb_total_service_interconnections))/2
    else :
        directly_shared_services = 0


    #Calcul du TSS
    #Les services cible de toutes les relations
    services_cible = []
    services_source = []
    for ser in sv_to_sv:
        services_cible.append(ser[1])
        services_source.append(ser[0])

    #recherche des services partagés qui sont cible plusieurs fois et le nombre de leurs relations

    TransSharedServices = []
    numberTransSharedService = 0
    TransSharedServicesLinks = 0
    #Si une source est aussi target et que sa source n'est pas une facade, alors il est un TSS
    for x in set(services_source):
        if x in services_cible:
            TransSharedServices.append(x)
            TransSharedServicesLinks += services_cible.count(x)

    numberTransSharedService = len(TransSharedServices)

    if nb_total_service_interconnections != 0:
        trans_shared_services = ((numberTransSharedService/nb_total_services)+(TransSharedServicesLinks/nb_total_service_interconnections))/2
    else:
        trans_shared_services = 0

    #Calcul du CDD
    try:
        cycle = nx.find_cycle(G, orientation="original")
        cyclic_dependencies_detection = 1
    except Exception as e:
        cyclic_dependencies_detection = 0

    #dtu, sdbi, sic, acu, dss, tss, cdd
    return [{'dtu' : db_type_utilization}, {'sdbi' : shared_db_interactions}, {'sic' : service_interaction_with_inter_comp}, {'acu' : asynchronous_service_utilization}, {'dss' : directly_shared_services}, {'tss' : trans_shared_services}, {'cdd' : cyclic_dependencies_detection}]


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
