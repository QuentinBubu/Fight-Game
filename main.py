import os
import time
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start
from assets.functions.settings import settings

action_list = ["attaque", "esquive", "soin", "charge", "attaque spéciale"]
error = 0

#try:

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

while player1.heart > 0 or player2.heart > 0:
    i = 0
    while i < 2:
        clean()
        if i == 0:
            player = player1
            opponent = player2
        elif i == 1:
            player = player2
            opponent = player1

        input(f"{player.username} c'est à toi, appuis sur \"Entrée\"") if not error else 0

        print(f"Dernier événement:\n{player.event}")
        player.event = "Aucun événement"

        action = 0
        while not action in action_list:
            clean()
            print(f"Vies restantes: {player.heart}\nAttaque: {player.attack}\nNombre d'esquives restantes: {player.dodge}\nNombre de potion de soin restantes: {player.treatment_number}\nVies regagnées lors d'un soin: {player.treatment}\nNombres de coup spéciaux restants: {player.special_number}\nPoints de vies retirés lors d'une attaque spécial: {player.special_attack}\nAttaque spécial chargée: {player.special_attack_is_charge}\n\nVies restantes de l'adversaire: {opponent.heart}")
            print(f"Liste des actions: {str(action_list).replace('[', '').replace(']', '')}")
            action = input("Que voulez-vous faire?\n")

        if action == "treatment":
            error = player.f_treatment()
            if error:
                input(error)
                continue

        elif action == "charge":
            error = player.f_dodge_charge()
            if error:
                input(error)
                continue

        elif action == "attaque":
            player.f_attack(opponent)

        elif action == "attaque spéciale":
            error = player.f_special_attack(opponent)
            if error:
                input(error)
                continue

        if player1.heart < 0 or player2.heart < 0:
            break

        i += 1

else:
    pass

"""
except Exception as erreur:
    Rapport_Bug = str(Rapport_Bug) + repr(erreur) + "fin"
    print("Nous sommes désolé mais une erreur que nous n'avons pas pu traitée est surenue! Veuillez relancer le jeu! Toutes nos excuses,")
    a = input("Voulez vous crée un rapport bug et l'envoyer par mail? o/n")
    if a == "o":
        if not os.path.exists("Rapport/"):
            os.makedirs("Rapport/")
        fichier = open("Rapport/Rapport_bug.txt", "w+")
        fichier.write(str(Rapport_Bug))
        fichier.close
        print("Merci! le rapport a été créer dans le dossier Rapport dans les fichiers de l'appli! Veuillez l'envoyer à anagamesprint@gmail.com; Merci!")
"""