# Global modules importation
import os, time, random, pickle

# Personals modules importation
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start
from assets.functions.settings import *
from assets.functions.save_game import save_game

# Define list of action. First list, this she is which printed. The lastes, this she is which name test
action_list = ["attaque", "esquive", "soin", "charge", "attaque spéciale", "sauvegarder"]
action_list2 = ["attaque", "esquive", "soin", "charge", "attaque spéciale", "sauvegarder", "attaque speciale"]

# List of prime if players would to be add there
prime_list = [
    ("heart", ("Bravo, vous avez gagné 20 points de vie!", 20)),
    ("dodge", ("Bravo, vous avez gagné une esquive!", 1)),
    ("treatment_number", ("Bravo, vous avez gagné une potion de soin!", 1)),
    ("heart", ("Oh non, vous avez perdu 5 points de vie!", -5)),
    ("dodge", ("Oh non, vous avez perdu une esquive!", -1))
]

# Variable initialization
error = None
turn = 0

# Program start
print("Bienvenue dans Fight Game, un super jeu de combat!")
time.sleep(2)

# Ask if they want to open settings
if input("Voulez vous ouvrir les paramètres? o/n ") == "o":
    # If settings return somthing, this is because a game has been open
    if game_date := settings():
        # We create character for players with data of open game
        player1 = Character(game_date['player1'], game_date['player1'])
        player2 = Character(game_date['player2'], game_date['player2'])
        turn = game_date['turn']
        prime = game_date['prime']

# If prime isn't define
if not 'prime' in globals():
    print("Pour commencer, choisissez qui sera le premier joureur et le second")

    print("Joueur 1, à toi!")
    player1 = pre_start()
    clean()

    print("Joueur 2, à toi!")
    player2 = pre_start()
    clean()

    # Add prime round if players would prime. Else, prime variable take False value
    prime = random.randint(10, 30) if input("Voulez vous activer les bonus/malus? o/n ") == "o" else False
    clean()

input("Êtes vous prêts? Appuyez sur \"Entrée\" pour commencer!")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("C'est parti!")
time.sleep(1)

# As long as player1 or player2 has heart points
while player1.heart > 0 and player2.heart > 0:
    # We set the while turn to 0
    i = 0

    # As long as while turn is inferior to 2 or player1 and player2 has heart points
    while i < 2 and (player1.heart > 0 and player2.heart > 0):
        clean()
        if i == 0:
            player = player1
            opponent = player2
        elif i == 1:
            player = player2
            opponent = player1

        # If is prime moment
        if prime != False and turn == prime:
            # Took random prime
            random_prime = random.randint(0, len(prime_list)-1)
            # And attribute this lastest
            player1.f_prime(prime_list[random_prime])
            player2.f_prime(prime_list[random_prime])
            clean()
            input(prime_list[random_prime][1][0])
            clean()
            # Generate an other turn
            prime = random.randint(turn, turn+20)

        # If hasn't error
        input(f"{player.username} c'est à toi, appuis sur \"Entrée\"") if not error else 0

        # We set player dodge to False
        player.dodge_is_charge = False

        action = None

        # As long as action isn't in action2 list
        while not action in action_list2:
            clean()
            print(f"Dernier événement: {player.event}\n")
            print(f"Vies restantes: {player.heart}\nAttaque: {player.attack}\nNombre d'esquives restantes: {player.dodge}\nNombre de potion de soin restantes: {player.treatment_number}\nVies regagnées lors d'un soin: {player.treatment}\nNombres de coup spéciaux restants: {player.special_number}\nPoints de vies retirés lors d'une attaque spécial: {player.special_attack}\nAttaque spécial chargée: {player.special_attack_is_charge}\n\nVies restantes de l'adversaire: {opponent.heart}")
            print(f"Liste des actions: {str(action_list).replace('[', '').replace(']', '')}")
            action = input("Que voulez-vous faire?\n").lower()

        player.event = "Aucun événement"

        # We test action writting
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
    input(f"Fin du jeu!!\nBravo à {winner} qui a gagné! En {turn} tours!")
    player1.f_add_stats()
    player2.f_add_stats()