import os
import time
from assets.functions.clean import clean
from assets.functions.pre_start import pre_start
from assets.functions.character_create import character_create

#try:

print("Bienvenue dans Fight Game, un super jeu de combat!")
time.sleep(2)
print("Pour commencer, choisissez qui sera le premier joureur et le second")

print("Joueur 1, à toi!")
player1 = pre_start()

print("Joueur 2, à toi!")
player2 = pre_start()

input("Êtes vous prêts? Appuyez sur \"Entrée\" pour commencer!")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("C'est parti!")

while player1.heart > 0 or player2.heart > 0:
    for i in range(2):
        pass

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