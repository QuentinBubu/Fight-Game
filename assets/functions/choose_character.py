import time, pickle
from assets.functions.clean import clean

def choose_character(user):
    clean()
    character_file = open("assets/character/character_list.txt", "r")
    character_list  = list(character_file.readline().split(","))
    character_file.close()
    character_choose = 0

    while not character_choose in character_list:
        clean()
        print(f"{user['username']}, choisis ton personnage: {str(character_list).replace('[', '').replace(']', '').replace(',', ', ')}")
        time.sleep(2)
        for i in range(len(character_list)):
            file = open(f"assets/character/{character_list[i]}.txt", "rb")
            character_data = pickle.load(file)
            print("--------------------------------")
            print(f"Nom: {character_data['name']}\nVies: {character_data['heart']}\nAttaque: {character_data['attack']}\nNombre d'esquives: {character_data['dodge']}\nNombre de potion de soin: {character_data['treatment_number']}\nVies regagnées lors d'un soin: {character_data['treatment']}\nNombres de coup spéciaux: {character_data['special_number']}\nPoints de vies retirés lors d'une attaque spécial: {character_data['special_attack']}")
            file.close()
        character_choose = input()
    return character_choose 