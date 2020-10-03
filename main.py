import os
import time
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start
from assets.functions.settings import settings

action_list = ["attaque", "esquive", "soin", "charge", "attaque spéciale"]
action_list2 = ["attaque", "esquive", "soin", "charge", "attaque spéciale", "attaque speciale"]
error = 0

print("Bienvenue dans Fight Game, un super jeu de combat!")
time.sleep(2)

if input("Voulez vous ouvrir les paramètres? o/n ") == "o":
    settings()

print("Pour commencer, choisissez qui sera le premier joureur et le second")

print("Joueur 1, à toi!")
player1 = pre_start()

clean()

print("Joueur 2, à toi!")
player2 = pre_start()

clean()

input("Êtes vous prêts? Appuyez sur \"Entrée\" pour commencer!")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("C'est parti!")
time.sleep(1)

player1.heart = player2.heart = 25

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

        print(player1.heart, "...", player2.heart)

        input(f"{player.username} c'est à toi, appuis sur \"Entrée\"") if not error else 0

        player.dodge_is_charge = False

        action = 0
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

        elif action == "attaque spéciale" or "attaque speciale":
            error = player.f_special_attack(opponent)
            if error:
                input(error)
                continue

        i += 1

else:
    clean()
    winner = player2.username if player1.heart <= 0 else player1.username
    input(f"Fin du jeu!!\nBravo à {winner} qui a gagné!")