import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
from archi import *
from examples import *
#On va faire une boucle sur chaque service, et pour chaque service, on va compter le nombre de fois ou il appatait comme premier parametre dans les tableaux des relations

#Chaque fonction de ce fichier calculera une metrique precise

def fanInFanOut(architecture):

    services = architecture.getServices()
    relations = architecture.getRelations()

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
