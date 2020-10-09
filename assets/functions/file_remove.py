import os
from assets.functions.clean import clean
def file_remove(dist):
    while True:
        clean()
        # We takes all files and del .txt of the end of file name and character list from list
        file_list =  ' '.join(map(str, os.listdir(dist))).replace(".txt", "").replace("character_list", "")
        file_to_remove = input(f"Quel fichier souhaitez-vous supprimer?\n{file_list}\n")
        if os.path.isfile(dist + file_to_remove + ".txt"):
            if input(f"Êtes vous sur de vouloir supprimer: {file_to_remove}? o/n: ") == "o":
                if dist == "assets/character/":
                    file = open("assets/character/character_list.txt", "r")
                    # Create a list with , to separt values
                    character_list = file.readline().split(",")
                    file.close()
                    # If is the lastest character
                    if len(character_list) <= 1:
                        input("Vous ne pouvez pas supprimer le dernier personnage!")
                        # Restart while
                        continue
                    character_list.remove(file_to_remove)
                    file = open("assets/character/character_list.txt", "w")
                    # Delete '
                    chaine = character_list[0].replace("'", "", 2)
                    for i in range(1,len(character_list)):
                        chaine += "," + character_list[i].replace("'", "", 2)
                    file.write(chaine)
                    file.close()
                # Remove file
                os.remove(dist + file_to_remove + ".txt")
            break