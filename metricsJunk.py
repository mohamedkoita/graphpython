#OK
#Database Type Utilization
#Ici on va considérer seulement les services qui ont leur propre base de données JUSTE EUX
def DTUmetrics(architecture):

    relations = architecture.getServicesRelationsTab()
    db_per_service_links = []
    full_database_links = []
    nb_full_database_links = 0
    nb_db_per_service_links = 0
    total_service_to_db_links = 0

    for val in relations:
        if 'FULL_DATABASE' in val[2]['link'] or 'SCHEMA' in val[2]['link'] or 'COLLECTION' in val[2]['link'] or 'TABLE' in val[2]['link']:
            total_service_to_db_links += 1

    for rel in relations:
        if 'FULL_DATABASE' in rel[2]['link']:
            full_database_links.append(rel[2]['link'])
            nb_full_database_links += 1

    for x in full_database_links:
        if full_database_links.count(x) == 1:
            nb_db_per_service_links += 1

    db_type_utilization = nb_db_per_service_links / total_service_to_db_links

    return db_type_utilization

#OK
#Shared Database Interactions
#Ici on cible les services qui partagent une base de données et qui partage les données. Les services ayant leur propre schema ou collection ou tout autre structure pareille ne sont pas concernés
def SDBImetrics(architecture):


    Gr = arc.createGraph(architecture, 1)
    G = Gr[0]
    relations = Gr[1]
    components = Gr[2]
    total_service_to_db_links = []
    nb_total_service_to_db_links = 0
    nb_shared_db_interconnexions = 0
    nb_total_service_interconnections = 0
    nb_service_to_facade_link = 0
    facade_links = 0
    facade_id = 0

    for val in relations:
        if 'FULL_DATABASE' in val[2]['link'] or 'SCHEMA' in val[2]['link'] or 'COLLECTION' in val[2]['link'] or 'TABLE' in val[2]['link']:
            total_service_to_db_links.append(val[2]['link'])
            nb_total_service_to_db_links += 1

    for rel in total_service_to_db_links:
        if 'FULL_DATABASE' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'SCHEMA' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'COLLECTION' in rel and total_service_to_db_links.count(rel) > 1:
            nb_shared_db_interconnexions += 1
        elif 'TABLE' in rel:
            nb_shared_db_interconnexions += 1
    # print(components)
    for comp in components:
        if comp[1] == "FACADE":
            facade_id = comp[0]
            facade_links = G.out_edges(facade_id)
            nb_service_to_facade_link = len(facade_links)


    nb_total_service_interconnections = len(relations) - nb_total_service_to_db_links - nb_service_to_facade_link + nb_shared_db_interconnexions

    if nb_total_service_interconnections == 0:
        shared_db_interactions = 0
        return shared_db_interactions

    shared_db_interactions = nb_shared_db_interconnexions / nb_total_service_interconnections
    print(len(relations))
    print(nb_service_to_facade_link)
    print(nb_shared_db_interconnexions)
    print(nb_total_service_to_db_links)
    print(nb_total_service_interconnections)


    return shared_db_interactions

#OK
#Service Interaction via Intermediary Component
#Ici on va rechercher toutes les transactions d'événements et de message que les services vont transmettre via message broker | pub/sub | stream
def SICmetrics(architecture):

    #Uniquement pub/sub et message brokers
    #Lien services vers message_broker
    #Les relations impliqunt les EVENT_BUS et les MESSAGE_BROKER
    nb_service_inter_via_mb_pb_st = 0
    Gr = arc.createGraph(architecture, 1)
    G = Gr[0]
    relations = Gr[1]
    components = Gr[2]

    for comp in components:
        if comp[1] == "MESSAGE_BROKER" or comp[1] == "EVENT_BUS":
            mb_pb_st_id = comp[0]
            FromMB = G.out_edges(mb_pb_st_id)
            ToMB = G.in_edges(mb_pb_st_id)
            nb_service_inter_via_mb_pb_st += len(FromMB) + len(ToMB)
            print(FromMB)
            print(ToMB)


    return nb_service_inter_via_mb_pb_st

#Asynchronous Communication Utilization
#Non applicable car tous les appels asynchrones de tous les projets sont fait via message broker | pub/sub | stream non [API | Polling |DirectCalls | SharedDB]
def ACUmetrics(architecture):

    #ACU = (numberAsynchInterconnectionsviaAPI + numberAsynchronousLinks + numberSharedDBInterconnections)/numberServicesInterconnections
    #Donc ici on va prendre nb_shared_db_interconnexions pour calculer

    return "Non applicable"

#OK
#Direct Service Sharing
def DSSmetrics(architecture):
    #Ecrire un algorithme pour decouvrir les services directement partages
    #un service directement partagé est un microservice qui est directement lié à et requis par plus d'un autre service

    # shared_services = 0
    # shared_services_connectors = 0
    # total_services = len(architecture.getServicesTab())
    # total_services_inter = len(architecture.getServicesRelationsTab())
    # direct_service_sharing = 0
    #
    # #On recupere tous les services
    # services = architecture.getServices()
    #
    # #On recupere toutes les relations entre les services
    # relations = architecture.getServicesRelations()
    #
    # #Pour chaque service on récupère les services avec lesquels il est en relation
    # for service in services:
    #     for relation in relations:
    #         if service == relation.getSource():
    #             service2 = relation.getDest()
    #             #On verifie si chacun de ces services emet une requete vers le premier service
    #             for rel in relations:
    #                 if rel.getSource() == service2 and rel.getDest() == service:
    #                     shared_services += 1
    #                     shared_services_connectors += 2
    #
    # direct_service_sharing = (shared_services/total_services + shared_services_connectors/total_services_inter)/2
    #
    #
    # return direct_service_sharing
    Gr = arc.createGraph(architecture, 1)
    G = Gr[0]
    relations = Gr[1]
    components = Gr[2]
    total_service_to_db_links = []
    nb_total_service_to_db_links = 0
    nb_shared_db_interconnexions = 0
    nb_total_service_interconnections = 0
    nb_service_to_facade_link = 0
    facade_links = 0
    facade_id = 0
    service_interaction_with_inter_comp = 0

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
            facade_id = comp[0]
            facade_links = G.out_edges(facade_id)
            nb_service_to_facade_link = len(facade_links)

    #Calcul du nombre total d'interconnexions entre services
    nb_total_service_interconnections = len(relations) - nb_total_service_to_db_links - nb_service_to_facade_link + nb_shared_db_interconnexions

    nodes = G.nodes()
    edges = G.edges()
    in_comp = []
    out_comp = []


    for rel in G.out_edges:
        in_comp.append(rel[0])
        out_comp.append(rel[1])
    #get service to services relations without service to db and service to facade
    sv_to_sv = []
    for val in relations:
        if 'FULL_DATABASE' not in val[2]['link'] and 'SCHEMA' not in val[2]['link'] and 'COLLECTION' not in val[2]['link'] and 'TABLE' not in val[2]['link'] and facade_id != val[0] :
            sv_to_sv.append(val)

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

    print(numberSharedService)
    print(sharedServicesLinks)

    return services_cible

#OK
#Transitevely Shared Services
def TSSmetrics(architecture):
    #Ecrire un algorithme pour decouvrir un algorithme partage de maniere transitive
    #un service partagé de manière transitive est un microservice qui est lié à d'autres services via au moins un service intermédiaire

    #Un niveau supérieur par rapport a DSS
    # transit_services = 0
    # transit_services_connectors = 0
    # total_services = len(architecture.getServicesTab())
    # total_services_inter = len(architecture.getServicesRelationsTab())
    # transitively_service_sharing = 0
    # tab = []
    # rels = []

    #On recupere tous les services
    # services = architecture.getServices()

    #On recupere toutes les relations entre les services
    # relations = architecture.getServicesRelations()

    #Pour chaque service on récupère les services avec lesquels il est en relation
    # for service in services:
    #     for relation in relations:
    #         if service == relation.getSource():
    #             service2 = relation.getDest()
    #             #On verifie si chacun de ces services emet une requete vers le premier service
    #             for rel in relations:
    #                 if rel.getSource() == service2:
    #                     service3 = rel.getDest()
    #                     for relx in relations:
    #                         if relx.getDest() == service and service not in tab:
    #                             tab.append(service)
    #                             transit_services += 1
    #
    #                             if relation not in rels:
    #                                 rels.append(relation)
    #                                 transit_services_connectors +=1
    #
    #                             if rel not in rels:
    #                                 rels.append(rel)
    #                                 transit_services_connectors +=1
    #
    #                             if relx not in rels:
    #                                 rels.append(relx)
    #                                 transit_services_connectors +=1
    Gr = arc.createGraph(architecture, 1)
    G = Gr[0]
    relations = Gr[1]
    components = Gr[2]
    total_service_to_db_links = []
    nb_total_service_to_db_links = 0
    nb_shared_db_interconnexions = 0
    nb_total_service_interconnections = 0
    nb_service_to_facade_link = 0
    facade_links = 0
    facade_id = 0
    service_interaction_with_inter_comp = 0

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
            facade_id = comp[0]
            facade_links = G.out_edges(facade_id)
            nb_service_to_facade_link = len(facade_links)

    #Calcul du nombre total d'interconnexions entre services
    nb_total_service_interconnections = len(relations) - nb_total_service_to_db_links - nb_service_to_facade_link + nb_shared_db_interconnexions

    nodes = G.nodes()
    edges = G.edges()
    in_comp = []
    out_comp = []


    for rel in G.out_edges:
        in_comp.append(rel[0])
        out_comp.append(rel[1])
    #get service to services relations without service to db and service to facade
    sv_to_sv = []
    for val in relations:
        if 'FULL_DATABASE' not in val[2]['link'] and 'SCHEMA' not in val[2]['link'] and 'COLLECTION' not in val[2]['link'] and 'TABLE' not in val[2]['link'] and facade_id != val[0] :
            sv_to_sv.append(val)

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






    # print(services_source)
    # print(services_cible)
    print(TransSharedServices)
    print(TransSharedServicesLinks)
    print(numberTransSharedService)


    return 1

#OK
#Cyclic dependencies detection
def CDDmetrics(G):
    try:
        cycle = nx.find_cycle(G, orientation="original")
        return 1
    except Exception as e:
        return 0
