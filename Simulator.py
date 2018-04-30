from Board import Board
from Game import Game
from time import time
import matplotlib.pyplot as plt

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
    sim.simulate_for(100, num_space, num_turns, player_win, space_elim, players_left, win_spaces)
    time_final = time()
    print(time_final-time_start)
    print_setting = False

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
        s = "Turn " + str(key)
        for key2, val in players_left.get(key).items():
            s += ", Players " + str(key2) + ": " + str(val)
        print(s)
    print("Spaces owned by winning player:")
    for key, val in win_spaces.items():
        print(key + ": " + str(val))

    board = Board()
    spaces = board.get_board()
    temp = []
    for space in spaces:
        temp.append(space.get_name())

    total = 0
    for i in num_space:
        total += i

    print("Space percentage:")
    for i in range(len(num_space)):
        tempnum = (num_space[i] / total)
        print(temp[i] + " " + str(tempnum))

    plt.figure(1)

    plt.subplot(221)
    plt.title("Number of times space has been landed on")
    plt.plot(num_space)

    plt.subplot(222)
    plt.title("Number of times each space eliminated a player")
    plt.plot(space_elim)

    plt.subplot(223)
    plt.title("Player number of wins")
    plt.plot(player_win)

    temp = []
    dict = []
    for key, value in win_spaces.items():
        temp.append(key)
        dict.append(value)

    plt.subplot(224)
    plt.title("Space and frequency of landing")
    plt.plot(dict)

    plt.show()


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

