import pickle
import os
def save_game(position, player, filename = "checkers_save.pkl"):
    with open(filename, "wb") as f:
        pickle.dump({"position": position, "player": player}, f)
    print("Game saved.")

def load_game(filename = "checkers_save.pkl"):
    if not os.path.exists(filename):
        print("No saved game found.")
        return None, None
    with open(filename, "rb") as f:
        data = pickle.load(f)
    print("Game loaded.")
    return data["position"], data["player"]