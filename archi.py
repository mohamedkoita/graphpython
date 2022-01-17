import csv

class Archi:
    services = []
    relations = []

    def __init__(self, name):
        self.name = name
        self.services = []
        self.relations = []

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

        with open('archi'+self.name+'.csv', mode='w+') as archi_file:
            archi_writer = csv.writer(archi_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            archi_writer.writerow(['Source', 'Destination', 'Trafic'])
            for tb in tab:
                archi_writer.writerow(tb)
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
