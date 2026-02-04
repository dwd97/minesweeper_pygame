import configuration as config

SUCCESSFUL_GAMES = []
SELECTED_DIFFICULTY = 1

def save_successful_game(time):
    global SUCCESSFUL_GAMES
    SUCCESSFUL_GAMES.append(time)
    print(f"saved: {time} s")

def get_best_time():
    if(SUCCESSFUL_GAMES == []):
        return None
    else:
        return min(SUCCESSFUL_GAMES)