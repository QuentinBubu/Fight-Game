import multiprocessing

def online_game():
    if input("1: Créer un serveur \n2: Rejoindre un serveur\n") == "1":
        multiprocessing.Process(exec(open("./online_game/server.py").read()))

    while True:
        print("ok")

    """
    serveur_ip = input("Veuillez saisir l'adresse IP de la personne hébergeante le serveur (fonctionne en local uniquement): ")
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