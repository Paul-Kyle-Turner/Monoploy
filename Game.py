from Board import Board
from Player import Player

DEFAULT_RULES = {
    ""
}


def main():
    print("")


class Game:

    def __init__(self, num_players=4):
        self.board = Board.__init__()
        self.players = self.create_players(num_players)

    @staticmethod
    def create_players(num_players):
        players = []
        for i in range(num_players):
            player = Player()
            players.append(player)
        return players

    def game_round(self):
        for player in self.players:
            space = self.board.change_position_dice(player)

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)


main()
