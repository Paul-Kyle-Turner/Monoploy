
from Game import Game


def main():
    sim = Simulator()
    sim.simulate_for(100)


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

