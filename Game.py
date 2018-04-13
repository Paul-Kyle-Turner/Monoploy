import Board

DEFAULT_RULES = {
    ""
}


def main():
    print("")


class Game:

    def __init__(self, num_players):
        self.board = Board.__init__()
        self.players = self.create_player()

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)


main()
