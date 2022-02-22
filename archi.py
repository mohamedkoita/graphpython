import csv

class Archi:
    services = []
    servicesRelations = []
    persistences = []
    persistencesRelations = []

    def __init__(self, name):
        self.name = name
        self.services = []
        self.servicesRelations = []
        self.persistences = []
        self.persistencesRelations = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addService(self, service):
        self.services.append(service)
        service.addArchi(self)

    def addServicesRelation(self, relation):
        self.servicesRelations.append(relation)

    def addPersistence(self, persistence):
        self.persistences.append(persistence)
        persistence.addArchi(self)

    def addPersistenceRelation(self, persistenceRelation):
        self.persistencesRelations.append(persistenceRelation)

    #Retourner les services sous forme d'objets
    def getServices(self):
        return self.services

    #Pour retourner les services sous forme de tableau
    def getServicesTab(self):
        tab = []
        for sv in self.services:
            tb = [sv.id, sv.type, sv.summary]
            tab.append(tb)
        return tab

    #Retourner les formes de persistence sous forme d'objets
    def getPersistences(self):
        return self.persistences

    #Pour retourner les formes de persistence sous forme de tableau
    def getPersistencesTab(self):
        tab = []
        for sv in self.persistences:
            tb = [sv.id, sv.type, sv.summary]
            tab.append(tb)
        return tab

    #Retourner les relations de services sous forme d'objets
    def getServicesRelations(self):
        return self.servicesRelations

    #Pour retouner les relations de services sous forme de tableau
    def getServicesRelationsTab(self):
        tab = []
        for rl in self.servicesRelations:
            rl.traffic['link'] = '\n'.join(rl.traffic['link'])
            tb = [rl.source.id, rl.dest.id, rl.traffic]
            tab.append(tb)
        return tab

    #Retourner les relations de persistences sous forme d'objets
    def getPersistencesRelations(self):
        return self.persistencesRelations

    #Pour retouner les relations de persistences sous forme de tableau
    def getPersistencesRelationsTab(self):
        tab = []
        for rl in self.persistencesRelations:
            rl.traffic['link'] = '\n'.join(rl.traffic['link'])
            tb = [rl.source.id, rl.dest.id, rl.traffic]
            tab.append(tb)
        return tab

    #Fonction pour exporter les données de l'architecture sous forme de csv
    def toCSV(self):

        tab = []
        for rl in self.servicesRelations:
            tb = [rl.source.summary, rl.dest.summary, rl.traffic['link']]
            tab.append(tb)

        with open('archi'+self.name+'.csv', mode='w+') as archi_file:
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

class Persistence:
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


class ServiceRelation:
    def __init__(self, source):
        self.source = source

    def addSource(self, source):
        self.source = addSource

    def getSource(self):
        return self.source

    def addDest(self, dest):
        if self.source.archi == dest.archi:
            self.dest = dest

    def getDest(self):
        return self.dest

    def addTraffic(self, traffic):
        self.traffic = traffic

class PersistenceRelation:
    def __init__(self, source):
        self.source = source

    def addSource(self, source):
        self.source = addSource

    def getSource(self):
        return self.source

    def addDest(self, dest):
        self.dest = dest

    def getDest(self):
        return self.dest

    def addTraffic(self, traffic):
        self.traffic = traffic
