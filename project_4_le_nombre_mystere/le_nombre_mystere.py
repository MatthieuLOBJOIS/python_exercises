"""
Le but de ce projet est de permettre à un joueur d'essayer de deviner un nombre mystère généré aléatoirement par l'ordinateur, en 5 essais ou moins.

👉 Déroulé du script
Au début du script, vous devez générer un nombre aléatoire compris entre 0 et 100 (vous pouvez agrandir ou réduire cet intervalle pour simplifier ou complexifier le jeu).

Le joueur dispose alors de 5 essais (là encore, libre à vous de changer cette valeur) pour trouver le nombre mystère.

À chaque essai, vous devez indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.

Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.

Dans le cas d'une victoire, vous devez indiquer au joueur combien d'essais lui ont été nécessaire pour gagner.

Si le joueur ne trouve pas le nombre mystère avec les 5 essais disponibles, il perd la partie.
"""

import random

trials_number = 5
mystery_number = random.randint(0, 100)

while trials_number > 0 : 
    print(f"Il reste {trials_number} essai{'s' if trials_number > 1 else ''}")
    number_guess = input("Devine le nombre mystère : ")
    if not number_guess.isdigit() : 
        print("Entrée un nombre valide")
        continue
    number_guess = int(number_guess)
    
    if mystery_number == number_guess : 
        print(f"""
        Tu as trouvé le nombre en {6 - trials_number} essai{"s" if trials_number != 1 else ""}
        Fin du jeu.
        """)
        break
    elif trials_number <= 1 :
        print(f"Dommage le nombre mystère était {mystery_number}")
    elif mystery_number < number_guess : 
        print(f"Le nombre mystère est plus petit que {number_guess}")
    elif mystery_number > number_guess :
        print(f"Le nombre mystère est plus grand que {number_guess}")
    trials_number -= 1