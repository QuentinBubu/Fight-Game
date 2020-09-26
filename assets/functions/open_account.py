import os
from assets.functions.clean import clean

def open_account():
    if not os.path.exists("assets/accounts/"):
        os.makedirs("assets/accounts/")
    while True:
        clean()
        account = input(f"Quel est ton compte?\n{''.join(map(str, os.listdir('assets/accounts/'))).replace('.txt', ', ')}\n")
        if os.path.isfile(f"assets/accounts/{account}.txt"):
            return account
        print("Erreur")