"""
Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.

Le jeu comporte deux joueurs : vous et un ennemi.

Vous commencez tous les deux avec 50 points de vie.

Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.

L'ennemi ne dispose d'aucune potion.

Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.

Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.

L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
Lorsque vous utilisez une potion, vous passez le prochain tour.

👉 Déroulé de la partie
Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion :

"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "

Cette phrase sera demandée à l'utilisateur au début de chaque tour.

?  Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.

Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.

?  Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.

Les points de vie que la potion vous donne doivent être compris entre 15 et 50 et générés aléatoirement par le programme Python.

Vous devez vérifier que l'utilisateur dispose de suffisamment de potion et décrémenter le nombre de potions qu'il a dans son inventaire lorsqu'il en boit une. Si l'utilisateur n'a plus de potions, vous devez lui indiquer et lui proposer de nouveau de faire un choix (attaquer ou prendre une potion).

Quand le joueur prend une potion, il passe le prochain tour.

Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, il vous attaque. Si l'ennemi est mort, vous pouvez terminer le jeu et indiqué à l'utilisateur qu'il a gagné ?

L'attaque de l'ennemi inflige des dégâts au joueur compris entre 5 et 15, là encore déterminés aléatoirement par le script.

Si vous n'avez plus de points de vie, le jeu se termine et vous avez perdu la partie.

À la fin du tour, vous devez afficher le nombre de points de vie restants du joueur et de l'ennemi.

Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.

À chaque tour, vous attaquez en premier. Il ne peut donc pas y avoir de match nul. Si lorsque vous attaquez, votre attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0, vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.
"""

import emoji
from random import randint

life_point_player = 50
life_point_enemy = 50

potions = 3

round_game = 1
icon_player = emoji.emojize(":green_square:")
icon_enemy = emoji.emojize(":red_square:")
icon_attack = emoji.emojize(":crossed_swords:")

heart_player = emoji.emojize(":green_heart:")
heart_enemy = emoji.emojize(":orange_heart:")


while True : 
    potions_value = randint(15, 50)
    attack_player = randint(5, 10)
    attack_enemy = randint(5, 15)

    print(f"C'est le Tours {round_game}!")
    player_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if player_choice != '1' and player_choice != '2':
        print("Entrée une commande valide.")
        continue
    elif player_choice == "1" :
        life_point_enemy -= attack_player
        print(f"{icon_player} Vous avez infligé {attack_player} points de dégats à l'ennemi {icon_attack}")
    elif player_choice == "2" :
        if potions > 0 : 
            potions -= 1
            life_point_player += potions_value
            print(f"{icon_player} Vous récupérez {potions_value} point de vie {heart_player} ({potions} potions restantes)")
        else :
            print(f"{icon_player} Vous n'avez plus de potion...")
            continue

    life_point_player -= attack_enemy
    print(f"{icon_enemy} L'ennemi vous a infligé {attack_enemy} points de dégats {icon_attack}")
    print(f"{icon_player} Il vous reste {life_point_player} {heart_player} PV")
    print(f"{icon_enemy} Il reste {life_point_enemy} {heart_enemy} PV à l'ennemi")
    print(50 * "-")

    if life_point_enemy <= 0 : 
        print("Tu as gagné.\nFin du jeu.")
        break
    elif life_point_player <= 0 : 
        print("Tu as perdu.\nFin du jeu.")
        break

    round_game += 1