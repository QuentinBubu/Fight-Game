import os
from assets.functions.clean import clean
def file_remove(dist):
    while True:
        clean()
        file_list =  ' '.join(map(str, os.listdir(dist))).replace(".txt", "").replace("character_list", "")
        file_to_remove = input(f"Quel fichier souhaitez-vous supprimer?\n{file_list}\n")
        if os.path.isfile(dist + file_to_remove + ".txt"):
            if input(f"Êtes vous sur de vouloir supprimer: {file_to_remove}? o/n: ") == "o":
                if dist == "assets/character/":
                    file = open("assets/character/character_list.txt", "r")
                    character_list = file.readline().split(",")
                    file.close()
                    if len(character_list) <= 1:
                        input("Vous ne pouvez pas supprimer le dernier personnage!")
                        continue
                    character_list.remove(file_to_remove)
                    file = open("assets/character/character_list.txt", "w")
                    chaine = character_list[0].replace("'", "", 2) #on l'initialise en supprimant les ' des stings
                    for i in range(1,len(character_list)):
                        chaine += "," + character_list[i].replace("'", "", 2) #on concatenere
                    file.write(chaine)
                    file.close()
                os.remove(dist + file_to_remove + ".txt")
            break