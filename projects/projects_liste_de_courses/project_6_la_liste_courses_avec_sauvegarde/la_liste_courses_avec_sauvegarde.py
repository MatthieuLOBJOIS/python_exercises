import sys, os, json

COMMAND_CHOICES = ["1", "2", "3", "4", "5"]
COMMAND_MODE = f"""
    {"-" * 50 }
    Liste des commandes : 

    1 - Ajouter un élément à la liste de courses
    2 - Retirer un élément de la liste de courses
    3 - Afficher les éléments de la liste de courses
    4 - Vider la liste de courses
    5 - Quitter le programme
    {"-" * 50 }
"""
CUR_DIR = os.path.dirname(__file__)
LIST_PATH = os.path.join(CUR_DIR, "list.json")

if os.path.exists(LIST_PATH) :
    with open("list.json", "r") as f:
        SHOPPING_LIST = json.load(f)
else :
    SHOPPING_LIST = []

while (True) : 
    print(COMMAND_MODE)

    list_command =  input("Votre choix : ")
    if list_command not in COMMAND_CHOICES : 
        print("Entrer une commande valide")
        continue

    if list_command == "1" :
        add_element = input("Ajouter un élément à la liste de courses : ")
        SHOPPING_LIST.append(add_element)
        print(f"{ add_element } ajoutée")
    elif list_command == "2" : 
        delete_element = input("Retirer un élément de la liste de courses : ")
        if delete_element in SHOPPING_LIST :
            SHOPPING_LIST.remove(delete_element)
            print(f"{ delete_element } supprimée")
        else :
            print("L'élement à supprimer ne se trouve pas dans la liste.")
    elif list_command == "3" : 
        if SHOPPING_LIST : 
            print("Voici la liste de course : ")
            for i, item in enumerate(SHOPPING_LIST, 1) : 
                print(f"{i} : {item}")
        else : 
            print("Liste de course vide.")
    elif list_command == "4" :
        SHOPPING_LIST.clear()
        print("Liste de course vidée.")
    elif list_command == "5" :
        print("Fin du programme, liste de courses sauvegardé.")

        with open("list.json", "w") as f:
            json.dump(SHOPPING_LIST, f, indent=4)

        sys.exit()