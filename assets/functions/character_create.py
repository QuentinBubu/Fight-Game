import os
import pickle

def character_create():  # creation assistée d'un personnage
    if not os.path.exists("assets/character/"): # si le dossier personnages a été supprimé
        os.makedirs("assets/character/") # on le recréé

    print("Assistance de création d'un personnage")

    elements = {
        'name': '',
        'start_heart': 0,
        'heart': 0,
        'attack': 0,
        'dodge': 0,
        'dodge_is_charge': 0,
        'treatment_number': 0,
        'treatment': 0,
        'special_number': 0,
        'special_attack': 0,
        'special_attack_is_charge': 0,
        'event': 'Aucun evenement'
    }

    elements['name'] = input("Saisissez un nom: ")
    elements['start_heart'] = elements['heart'] = int(input("Saisissez ses points de vies: "))
    elements['attack'] = int(input("Saisissez ses points d'attaque: "))
    elements['dodge'] = int(input("Saisissez le nombre d'esquives possible: "))
    elements['traitement_number'] = int(input("Saisissez le nombre de soin qui lui sera possible d'utiliser: "))
    elements['traitement'] = int(input("Saisissez le nombre de points de vie regagnés lors du soin: "))
    elements['special_number'] = int(input("Saisissez le nombre de coup spécial qu'il lui sera possible d'utiliser: "))
    elements['special_attack'] = int(input("Saisissez les points de vies qui seront retirés lors du coup spécial : "))

    file = open(f"assets/character/{elements['name']}.txt", "wb")
    pickle.dump(elements, file)
    file.close()

    character_file = open("assets/character/character_list.txt", "a")
    character_file.write(',' + elements['name'])
    character_file.close()
    input("Votre personnage à bien été créer!")