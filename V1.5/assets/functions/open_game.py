import pickle, os
from assets.Class.character import Character

def open_game():
    print("Quel partie voulez vous ouvrir?")
    game_to_open = input(f"{str(os.listdir('assets/game_saved/')).replace('[', '').replace(']', '').replace(',', ', ').replace('.txt', '')}\n")
    file = open(f"assets/game_saved/{game_to_open}.txt", "rb")
    game_date = pickle.load(file)
    file.close()
    return game_date