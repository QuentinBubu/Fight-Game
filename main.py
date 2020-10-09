import os, time, random, pickle
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start
from assets.functions.settings import *
from assets.functions.save_game import save_game

action_list = ["attaque", "esquive", "soin", "charge", "attaque spéciale", "sauvegarder"]
action_list2 = ["attaque", "esquive", "soin", "charge", "attaque spéciale", "sauvegarder", "attaque speciale"]

prime_list = [
    ("heart", ("Bravo, vous avez gagné 20 points de vie!", 20)),
    ("dodge", ("Bravo, vous avez gagné une esquive!", 1)),
    ("treatment_number", ("Bravo, vous avez gagné une potion de soin!", 1)),
    ("heart", ("Oh non, vous avez perdu 5 points de vie!", -5)),
    ("dodge", ("Oh non, vous avez perdu une esquive!", -1))
]

error = None
turn = 0

print("Bienvenue dans Fight Game, un super jeu de combat!")
time.sleep(2)

if input("Voulez vous ouvrir les paramètres? o/n ") == "o":
    if game_date := settings():
        player1 = Character(game_date['player1'], game_date['player1'])
        player2 = Character(game_date['player2'], game_date['player2'])
        turn = game_date['turn']
        prime = game_date['prime']

if not 'prime' in globals():
    print("Pour commencer, choisissez qui sera le premier joureur et le second")

    print("Joueur 1, à toi!")
    player1 = pre_start()
    clean()

    print("Joueur 2, à toi!")
    player2 = pre_start()
    clean()

    prime = random.randint(10, 30) if input("Voulez vous activer les bonus/malus? o/n ") == "o" else False
    clean()

input("Êtes vous prêts? Appuyez sur \"Entrée\" pour commencer!")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("C'est parti!")
time.sleep(1)

while player1.heart > 0 and player2.heart > 0:
    i = 0
    while i < 2 and (player1.heart > 0 and player2.heart > 0):
        clean()
        if i == 0:
            player = player1
            opponent = player2
        elif i == 1:
            player = player2
            opponent = player1

        if prime != False and turn == prime:
            random_prime = random.randint(0, len(prime_list)-1)
            player1.f_prime(prime_list[random_prime])
            player2.f_prime(prime_list[random_prime])
            clean()
            input(prime_list[random_prime][1][0])
            clean()
            prime = random.randint(turn, turn+20)

        input(f"{player.username} c'est à toi, appuis sur \"Entrée\"") if not error else 0

        player.dodge_is_charge = False

        action = None
        while not action in action_list2:
            clean()
            print(f"Dernier événement: {player.event}\n")
            print(f"Vies restantes: {player.heart}\nAttaque: {player.attack}\nNombre d'esquives restantes: {player.dodge}\nNombre de potion de soin restantes: {player.treatment_number}\nVies regagnées lors d'un soin: {player.treatment}\nNombres de coup spéciaux restants: {player.special_number}\nPoints de vies retirés lors d'une attaque spécial: {player.special_attack}\nAttaque spécial chargée: {player.special_attack_is_charge}\n\nVies restantes de l'adversaire: {opponent.heart}")
            print(f"Liste des actions: {str(action_list).replace('[', '').replace(']', '')}")
            action = input("Que voulez-vous faire?\n").lower()

        player.event = "Aucun événement"

        if action == "soin":
            error = player.f_treatment()
            if error:
                input(error)
                continue

        elif action == "esquive":
            error = player.f_dodge_charge()
            if error:
                input(error)
                continue

        elif action == "attaque":
            player.f_attack(opponent)

        elif action == "charge":
            error = player.f_special_attack_charge()
            if error:
                input(error)
                continue

        elif action == "attaque spéciale" or action == "attaque speciale":
            error = player.f_special_attack(opponent)
            if error:
                input(error)
                continue

        elif action == "sauvegarder" and i == 0:
            save_game(player1, player2, turn, prime)
        elif action == "sauvegarder":
            input("Impossible de sauvegarder, demander à votre adversaire!")

        i += 1
        turn += 1

else:
    clean()
    winner = player2.username if player1.heart <= 0 else player1.username
    input(f"Fin du jeu!!\nBravo à {winner} qui a gagné!")
    player1.f_add_stats()
    player2.f_add_stats()