from archi import *
from archigraph import *
from examples import projet1


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

print("\n")
print(70 * "#")
while True:
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
    elif option == 1:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet1["name"])

                createServices(project, projet1["services"])

                createRelations(project, projet1["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence1["name"])

                createServices(project, persistence1["services"])

                createRelations(project, persistence1["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")



    elif option == 2:
        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                projectx = createArchi(projet2["name"])

                for svvc in projectx.getServices():
                    pprint(vars(svvc))
                    print('----------------------------------------------------------------------------------')
                    print('----------------------------------------------------------------------------------')

                createServices(projectx, projet2["services"])

                createRelations(projectx, projet2["relations"])

                # print(projet2["relations"])
                projectx.toCSV()

                drawGraph(projectx)

            elif option == 2:

                project = createArchi(persistence2["name"])

                createServices(project, persistence2["services"])

                createRelations(project, persistence2["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 3:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet3["name"])

                createServices(project, projet3["services"])

                createRelations(project, projet3["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence3["name"])

                createServices(project, persistence3["services"])

                createRelations(project, persistence3["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 4:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet4["name"])

                createServices(project, projet4["services"])

                createRelations(project, projet4["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence4["name"])

                createServices(project, persistence4["services"])

                createRelations(project, persistence4["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 5:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet5["name"])

                createServices(project, projet5["services"])

                createRelations(project, projet5["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence5["name"])

                createServices(project, persistence5["services"])

                createRelations(project, persistence5["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 6:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet6["name"])

                createServices(project, projet6["services"])

                createRelations(project, projet6["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence6["name"])

                createServices(project, persistence6["services"])

                createRelations(project, persistence6["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 7:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet7["name"])

                createServices(project, projet7["services"])

                createRelations(project, projet7["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence7["name"])

                createServices(project, persistence7["services"])

                createRelations(project, persistence7["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 8:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet8["name"])

                createServices(project, projet8["services"])

                createRelations(project, projet8["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence8["name"])

                createServices(project, persistence8["services"])

                createRelations(project, persistence8["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 9:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet9["name"])

                createServices(project, projet9["services"])

                createRelations(project, projet9["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence9["name"])

                createServices(project, persistence9["services"])

                createRelations(project, persistence9["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 10:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet10["name"])

                createServices(project, projet10["services"])

                createRelations(project, projet10["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence10["name"])

                createServices(project, persistence10["services"])

                createRelations(project, persistence10["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 11:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet11["name"])

                createServices(project, projet11["services"])

                createRelations(project, projet11["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence11["name"])

                createServices(project, persistence11["services"])

                createRelations(project, persistence11["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 12:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet12["name"])

                createServices(project, projet12["services"])

                createRelations(project, projet12["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence12["name"])

                createServices(project, persistence12["services"])

                createRelations(project, persistence12["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    elif option == 13:

        print(20 * " ", "Choisir le graphe a dessiner", 10 * " ")
        print(30 * " ", "", 15 * " ")
        print(8 * " ", "1 - Architecture du système")
        print(8 * " ", "2 - Modèle de persistance des données")

        while True:
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

                project = createArchi(projet13["name"])

                createServices(project, projet13["services"])

                createRelations(project, projet13["relations"])

                project.toCSV()

                drawGraph(project)

            elif option == 2:

                project = createArchi(persistence13["name"])

                createServices(project, persistence13["services"])

                createRelations(project, persistence13["relations"])

                project.toCSV()

                drawGraph(project)

            else:
                # selection ivalide, ressaisir
                print("Selection invalide")
                print(50 * "#")


    else:
        # selection ivalide, ressaisir
        print("Selection invalide")
        print(50 * "#")
