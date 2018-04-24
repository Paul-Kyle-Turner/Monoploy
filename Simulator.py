
from Game import Game
from time import time

def main():
    time_start = time()
    sim = Simulator()
    sim.simulate_for(1000)
    time_final = time()
    print(time_final-time_start)


class Simulator:

    def __init__(self):
        self.game = Game()

    def create_game(self):
        self.game = Game()

    def simulate(self):
        self.game.game_play()

    def simulate_for(self, num_games=100):
        for i in range(num_games):
            self.create_game()
            self.simulate()

main()

