import os
from assets.functions.clean import clean
def file_remove(dist):
    while True:
        clean()
        # On récupère tous les fichiers, on supprime le .txt ainsi que le fichier character_list de la liste
        file_list =  ' '.join(map(str, os.listdir(dist))).replace(".txt", "").replace("character_list", "")
        file_to_remove = input(f"Quel fichier souhaitez-vous supprimer?\n{file_list}\n")
        if os.path.isfile(dist + file_to_remove + ".txt"):
            if input(f"Êtes vous sur de vouloir supprimer: {file_to_remove}? o/n: ") == "o":
                if dist == "assets/character/":
                    # Ouverture du fichier en mode lecture
                    file = open("assets/character/character_list.txt", "r")
                    # Lecture de la ligne en créant une liste, utilisant la virgule comme séparateur
                    character_list = file.readline().split(",")
                    file.close()
                    # Si c'est le dernier personnage
                    if len(character_list) <= 1:
                        input("Vous ne pouvez pas supprimer le dernier personnage!")
                        # Redémarre la boucle
                        continue
                    character_list.remove(file_to_remove)
                    # Ouverture du fichier en mode écriture
                    file = open("assets/character/character_list.txt", "w")
                    # Suppression des quotes et création de la liste
                    chaine = character_list[0].replace("'", "", 2)
                    for i in range(1,len(character_list)):
                        # Concaténation de la liste et suppression des quotes
                        chaine += "," + character_list[i].replace("'", "", 2)
                    # Ecriture dans le fichier
                    file.write(chaine)
                    file.close()
                # Suppression du fichier
                os.remove(dist + file_to_remove + ".txt")
            break