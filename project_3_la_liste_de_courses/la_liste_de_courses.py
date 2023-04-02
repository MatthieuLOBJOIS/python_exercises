"""
Dans ce projet, tu vas devoir créer un programme en ligne de commande qui permet de manipuler une liste de courses.

👉 Déroulé du script
Le programme doit permettre de réaliser 5 actions :
- Ajouter un élément à la liste de courses
- Retirer un élément de la liste de courses
- Afficher les éléments de la liste de courses
- Vider la liste de courses
- Quitter le programme

Tu dois donc demander à l'utilisateur de choisir parmi une de ces action en entrant un nombre de 1 à 5.

Tu dois gérer le cas de figure où l'utilisateur ne rentre pas un nombre compris entre 1 et 5 ou s'il rentre par exemple des lettres ou un autre symbole invalide. Dans ce cas, tu dois afficher de nouveau le menu avec les options disponibles, jusqu'à ce que l'utilisateur choisisse une option valide.

Dans ce projet, tu ne dois pas sauvegarder la liste dans un fichier ou une base de donnée.

Le but ici est juste d'interagir avec l'utilisateur et de manipuler une liste en fonction de son choix.

Bonne chance pour cet exercice ?

Prends le temps de bien décrire toutes les étapes en français avant de te lancer dans le code !


Quelques éléments pour t'aider :

Pour boucler sur un itérable et récupérer en même temps l'indice de l'itération, tu peux utiliser la fonction enumerate :

>>> for i, element in enumerate("Python"):
>>>     print(i, element)
0 "P"
1 "y"
2 "t"
3 "h"
4 "o"
5 "n"
Pour sortir d'un script en ligne de commande, tu peux utiliser le module sys et la fonction exit :

import sys
sys.exit()
Cela aura pour effet de mettre fin au script en cours d'exécution.
"""

import sys

shopping_list  = []
command_choices = ["1", "2", "3", "4", "5"]

while (True) : 
    print(f"""
    {"-" * 50 }
    Liste des commandes : 

    1 - Ajouter un élément à la liste de courses
    2 - Retirer un élément de la liste de courses
    3 - Afficher les éléments de la liste de courses
    4 - Vider la liste de courses
    5 - Quitter le programme
    {"-" * 50 }
    """)

    list_command =  input("Votre choix : ")
    if list_command not in command_choices : 
        print("Entrer une commande valide")
        continue

    if list_command == "1" :
        add_element = input("Ajouter un élément à la liste de courses : ")
        shopping_list.append(add_element)
        print(f"{ add_element } ajoutée")
    elif list_command == "2" : 
        delete_element = input("Retirer un élément de la liste de courses : ")
        if delete_element in shopping_list :
            shopping_list.remove(delete_element)
            print(f"{ delete_element } supprimée")
        else :
            print("L'élement à supprimer ne se trouve pas dans la liste.")
    elif list_command == "3" : 
        if shopping_list : 
            print("Voici la liste de course : ")
            for i, item in enumerate(shopping_list, 1) : 
                print(f"{i} : {item}")
        else : 
            print("Liste de course vide.")
    elif list_command == "4" :
        shopping_list.clear()
        print("Liste de course vidée.")
    elif list_command == "5" :
        print("Fin du programme")
        sys.exit()