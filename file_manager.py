import json
import os
def save_game(position, player, filename="text_checkers.txt"):                ##allows the user to save his game in both gamemodes in order to continue later
    data = {
        "position": position,
        "player": player
    }
    with open(filename, "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load_game(filename="text_checkers.txt"):                              ##allows the user to load the saved game
    if not os.path.exists(filename):
        print("No saved game found.")
        return None, None
    with open(filename, "r") as f:
        data = json.load(f)
    print("Game loaded.")
    return data["position"], data["player"]
