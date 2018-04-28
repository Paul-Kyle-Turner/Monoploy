from Game import Game
from time import time

def main():
    time_start = time()
    num_space = []
    space_elim = []
    num_turns = {}
    player_win = []
    players_left = {}
    win_spaces = {}
    i = 0
    while i < 40:
        num_space.append(0)
        space_elim.append(0)
        i += 1
    j = 0
    while j < 4:
        player_win.append(0)
        j += 1
    sim = Simulator(num_space, num_turns, player_win, space_elim, players_left, win_spaces)
    sim.simulate_for(2000000, num_space, num_turns, player_win, space_elim, players_left, win_spaces)
    time_final = time()
    print(time_final-time_start)
    print("Number of times each space was landed on:")
    k = 0
    while k < 40:
        print("Space " + str(k) + ": " + str(num_space[k]))
        k += 1
    print("Number of Times Each Player Won:")
    m = 0
    while m < 4:
        print("Player " + str(m) + " won " + str(player_win[m]) + " times")
        m += 1
    print("Length of Games:")
    for key, val in num_turns.items():
        print("Turn " + str(key) + ": " + str(val))
    print("Number of times each space eliminated a player:")
    n = 0
    while n < 40:
        print("Space " + str(n) + ": " + str(space_elim[n]))
        n += 1
    print("Number of players left on a given turn:")
    for key in players_left:
        print("Turn " + str(key))
        for key2, val in players_left.get(key).items():
            print("Players " + str(key2) + ": " + str(val))
    print("Spaces owned by winning player:")
    for key, val in win_spaces.items():
        print(key + ": " + str(val))


class Simulator:
    def __init__(self, num_space, num_turns, player_win, space_elim, players_left, win_spaces):
        self.game = Game(num_space, num_turns, player_win, space_elim, players_left, win_spaces)

    def create_game(self, num_space, num_turns, player_win, space_elim, players_left, win_spaces):
        self.game = Game(num_space, num_turns, player_win, space_elim, players_left, win_spaces)

    def simulate(self):
        self.game.game_play()

    def simulate_for(self, num_games, num_space, num_turns, player_win, space_elim, players_left, win_spaces):
        for i in range(num_games):
            self.create_game(num_space, num_turns, player_win, space_elim, players_left, win_spaces)
            self.simulate()

main()

