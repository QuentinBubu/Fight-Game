import pickle

def player_data_set(player):
    elements = {
        'name': player.username,
        'account': player.account,
        'start_heart': player.start_heart,
        'heart': player.heart,
        'attack': player.attack,
        'dodge': player.dodge,
        'dodge_is_charge': player.dodge_is_charge,
        'treatment_number': player.treatment_number,
        'treatment': player.treatment,
        'special_number': player.special_number,
        'special_attack': player.special_attack,
        'special_attack_is_charge': player.special_attack_is_charge,
        'event': player.event
    }
    return elements

def save_game(player1, player2, turn, prime):
    game_name = input("Saisissez le nom de la partie, si une partie existe déjà avec ce nom, elle sera écrasée.\n")
    file = open(f"assets/game_saved/{game_name}.txt", "wb")

    game_data = {
        "player1": player_data_set(player1),
        "player2": player_data_set(player2),
        "turn": turn,
        "prime": prime
    }
    pickle.dump(game_data, file)
    file.close()