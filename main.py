import os
import time
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start

try:

    print("Bienvenue dans Fight Game, un super jeu de combat!")
    time.sleep(2)
    print("Pour commencer, choisissez qui sera le premier joureur et le second")

    print("Joueur 1, à toi!")
    player1 = pre_start

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