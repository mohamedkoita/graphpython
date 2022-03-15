from archi import *
from archigraph import *
from examples import projet1
from metrics import *
from tabulate import tabulate

print("\n")
print(70 * "#")
while True:
    print(70 * "#")
    print(20 * " ", "LISTE DES PROJETS", 10 * " ")
    print(30 * " ", "", 15 * " ")
    print(8 * " ", "1 - Teastore")
    print(8 * " ", "2 - Sitewhere")
    print(8 * " ", "3 - Petclinic")
    print(8 * " ", "4 - eShop on containers")
    print(8 * " ", "5 - GoogleCloudPlatform Demo")
    print(8 * " ", "6 - Mspnp microservices implementation")
    print(8 * " ", "7 - Piggymetrics")
    print(8 * " ", "8 - PitStop")
    print(8 * " ", "9 - RobotShop")
    print(8 * " ", "10 - Digota")
    print(8 * " ", "11 - PartsUnlimited mrp microservices")
    print(8 * " ", "12 - Blueprint microservices")
    print(8 * " ", "13 - Microservices Demo")
    print(70 * "*", "", 15 * " ")
    print(8 * " ", "14 - Exporter toutes les métriques des projets dans un fichier CSV")
    option = input("Entrer votre choix ou '0' fermer le programme : ")
    try:
        option = int(option)
    except ValueError:
        # Handle the exception
        print('Please enter an integer')

    print(50 * "_")
    if option == 0:
        print(50 * "*")
        print(5 * "*", "FERMETURE DU PROGRAMME", 12 * "*")
        print(50 * "*")
        break

    elif option in range(1, 14):

        project = createArchi(globals()[f"projet{option}"]["name"])

        createServices(project, globals()[f"projet{option}"]["services"])

        createServicesRelations(project, globals()[f"projet{option}"]["relations"])

        metrics = calculateMetrics(project)

        project.toCSV()

        while True:
            print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
            print(30 * " ", "", 15 * " ")
            print(8 * " ", "1 - Architecture du système")
            print(8 * " ", "2 - Asynchronous Communication Utilization - Utilisation de Communication Asynchrone")
            print(8 * " ", "3 - Afficher le fanIn et le fanOut des services")
            print(8 * " ", "4 - Data Type Utilization - Utilisation du type de données")
            print(8 * " ", "5 - Shared Database Interaction - Interactions avec base de données partagée")
            print(8 * " ", "6 - Service Interaction via Intedrmediary Component - Interactions par composant intermédiaire")
            print(8 * " ", "7 - Direct Service Sharing - Services partagés directement")
            print(8 * " ", "8 - Transitevely Shared Services - Services partagés en transit")
            print(8 * " ", "9 - Cyclic Dependencies Detection - Détection de dépendances cycliques")
            option = input("Entrer votre choix ou '0' pour revenir au menu principal: ")
            try:
                option = int(option)
            except ValueError:
                # Handle the exception
                print('Please enter an integer')

            if option == 0:
                print(50 * "*")
                print(5 * "*", "RETOUR AU MENU PRINCIPAL", 12 * "*")
                print(50 * "*")
                break

            elif option == 1:

                drawGraph(metrics[7]['gr'])

            elif option == 2:

                print(metrics[3]['acu'])

            elif option == 3:

                print(tabulate(fanInFanOut(project), headers = ['Service', 'FanIn', 'FanOut']))

            elif option == 4:

                print(metrics[0]['dtu'])

            elif option == 5:

                print(metrics[1]['sdbi'])

            elif option == 6:

                print(metrics[2]['sic'])

            elif option == 7:

                print(metrics[4]['dss'])

            elif option == 8:

                print(metrics[5]['tss'])

            elif option == 9:

                print(metrics[6]['cdd'])

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")

    elif option == 14:

        AllInCsvFile()
        print("Fichier exporté dans le repertoire courant")

    else:
        # selection ivalide, ressaisir
        print("Selection invalide")
        print(50 * "#")
