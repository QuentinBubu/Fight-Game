import os, pickle
from assets.functions.clean import clean
from assets.functions.file_remove import file_remove
from assets.functions.character_create import character_create
from assets.functions.open_account import open_account
from assets.functions.account_create import account_create
from assets.functions.open_game import *

def settings():
    clean()
    while True:
        print("Paramètres:")
        print("1: Comptes")
        print("2: Personnages")
        print("3: Couleur")
        print("4: Sauvegarde")
        print("5: Mode en ligne")
        print("Fin: Quitter")
        setting_number = input()
        clean()
        if setting_number == "1":
            account_settings = input("1: Ouvrir les statistiques d'un compte\n2: Créer un compte\n3: Supprimer un compte\n")
            if account_settings == "1":
                account = open_account()
                clean()
                account_file = open(f"assets/accounts/{account}.txt", "rb")
                account_stats = pickle.load(account_file)
                account_file.close()
                input(f"Nom: {account_stats['name']}\nParties jouées: {account_stats['games_played']}\nParties gagnées: {account_stats['games_won']}\nParties perdues: {account_stats['games_loose']}\nTaux de réussite: {account_stats['win_percent']}%\n")

            elif account_settings == "2":
                account_create()

            elif account_settings == "3":
                file_remove("assets/accounts/")

        elif setting_number == "2":
            setting_number = input("Que faire? \n1: Ajouter un personnage \n2: Supprimer un personnage\n")
            if setting_number == "1":
                character_create()

            elif setting_number == "2":
                file_remove("assets/character/")

        elif setting_number == "3":
            print("Quelle Couleur?(ref: couleur->tap 'color')(ex: fc -> rouge sur blanc)(défaut:07)")
            os.system(f"color {input()}")

        elif setting_number == "fin" or setting_number == "Fin" or setting_number == "Quitter":
            break

        elif setting_number == "4":
            setting_number = input("Que faire? \n1: Ouvrir une sauvegarde \n2: Supprimer une sauvegarde\n")
            if setting_number == "1":
                return open_game()

            elif setting_number == "2":
                file_remove("assets/game_saved/")
            """
        elif setting_number == "5":
            if input("1 pour créer le serveur \n2 pour rejoindre un serveur\n") == "1":
                creer_serveur()

            else:
                serveur_ip = input("Veuillez saisir l'addresse IP donné par la partie serveur (fonctionne en local uniquement): ")
                cote_client.connect((serveur_ip, port))
                #test de connexion
                time.sleep(1)
                print("Démarrage du test de connexion...")
                print("Envoie du packet 1")
                cote_client.send("test1".encode('utf-8'))
                msg = cote_client.recv(1024).decode('utf-8')
                if msg == "test2":
                    cote_client.send("ok".encode('utf-8'))
                    input("Test réussi, appuyez sur \"Entrée\"")
                    mode_de_jeu = "en ligne, client"
                    jeu_client()

                else:
                    print("Echec")
            """
        else:
            input("Erreur, veuillez saisir un chiffre valide!")
        clean()