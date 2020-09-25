import os
from assets.functions.clean import clean

def open_account():
    if not os.path.exists("assets/accounts/"):
        os.makedirs("assets/accounts/")
    while True:
        clean()
        account = input(f"Quel est ton compte?\n{os.listdir('assets/accounts/')}")
        if os.path.isfile(f"assets/accounts/{account}.txt"):
            return account
        print("Erreur")