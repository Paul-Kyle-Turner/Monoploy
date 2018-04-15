from Board import Board
from Player import Player

DEFAULT_RULES = {
    ""
}


def main():
    game = Game()
    game.game_round()


class Game:

    def __init__(self, num_players=4):
        self.board = Board(game=self)
        self.players = self.create_players(num_players)

    @staticmethod
    def create_players(num_players):
        players = []
        for i in range(num_players):
            player = Player(i)
            players.append(player)
        return players

    def game_round(self):
        for player in self.players:
            space = self.board.change_position_dice(player=player)


    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)


main()
