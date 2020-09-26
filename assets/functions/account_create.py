import os
import pickle

def account_create():
    if not os.path.exists("assets/accounts/"):
        os.makedirs("assets/accounts/")
    while True:
        account_name = input("Quel sera votre pseudo?")
        if not os.path.isfile(f"assets/accounts/{account_name}.txt"):
            file = open(f"assets/accounts/{account_name}.txt", "wb")
            account_data = {
                'name': account_name,
                'games_played': 0,
                'games_won': 0,
                'games_loose': 0,
                'win_percent': 0
            }
            pickle.dump(account_data, file)
            file.close()
            return account_name
        else:
            print("Saisissez un autre pseudo")