import pickle
from assets.functions.open_account import open_account
from assets.functions.account_create import account_create
from assets.functions.choose_character import choose_character
from assets.Class.character import Character

def pre_start():

    user = {
        'username': '',
        'account':  False
    }

    if input("Avez-vous un compte? o/n\n") == "o":
        user['username'] = user['account'] = open_account()
    else:
        if input("Voulez vous en créer un? o/n \n") == "o":
            user['username'] = user['account'] = account_create()
        else:
            user['username'] = input("Saisissez un pseudonyme alors!\n")

    character = choose_character(user)

    character_file = open(f"assets/character/{character}.txt", "rb")
    character_data = pickle.load(character_file)
    character_file.close()

    return Character(character_data, user)


