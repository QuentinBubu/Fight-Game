import os, pickle

def character_create():
    # If folder doesn't exist
    if not os.path.exists("assets/character/"):
        os.makedirs("assets/character/")

    print("Assistance de création d'un personnage")

    # We creat list where the character data set
    elements = {
        'name': '',
        'start_heart': 0,
        'heart': 0,
        'attack': 0,
        'dodge': 0,
        'dodge_is_charge': False,
        'treatment_number': 0,
        'treatment': 0,
        'special_number': 0,
        'special_attack': 0,
        'special_attack_is_charge': False,
        'event': 'Aucun evenement'
    }

    # We ask character data
    elements['name'] = input("Saisissez un nom: ")
    elements['start_heart'] = elements['heart'] = int(input("Saisissez ses points de vies: "))
    elements['attack'] = int(input("Saisissez ses points d'attaque: "))
    elements['dodge'] = int(input("Saisissez le nombre d'esquives possible: "))
    elements['treatment_number'] = int(input("Saisissez le nombre de soin qui lui sera possible d'utiliser: "))
    elements['treatment'] = int(input("Saisissez le nombre de points de vie regagnés lors du soin: "))
    elements['special_number'] = int(input("Saisissez le nombre de coup spécial qu'il lui sera possible d'utiliser: "))
    elements['special_attack'] = int(input("Saisissez les points de vies qui seront retirés lors du coup spécial : "))

    # And we writte this into file
    file = open(f"assets/character/{elements['name']}.txt", "wb")
    pickle.dump(elements, file)
    file.close()

    # And add character at the end of file which contain list of lastest
    character_file = open("assets/character/character_list.txt", "a")
    character_file.write(',' + elements['name'])
    character_file.close()
    input("Votre personnage à bien été créer!")