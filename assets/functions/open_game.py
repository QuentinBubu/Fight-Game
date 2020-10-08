import pickle, os
from assets.Class.character import Character

player1 = None
player2 = None
turn = None
prime = None
game_already_open = False

def open_game():
    global player1, player2, turn, game_already_open

    print("Quel partie voulez vous ouvrir?")
    game_to_open = input(f"{str(os.listdir('assets.game_saved')).replace('[', '').replace(']', '').replace(',', ', ')}")
    file = open(game_to_open, "rb")
    game_date = pickle.load(file)
    file.close()

    player1 = Character(game_date['player1'], game_date['player1'])
    player2 = Character(game_date['player2'], game_date['player2'])
    turn = game_date['turn']
    prime = game_date['prime']
    game_already_open = True