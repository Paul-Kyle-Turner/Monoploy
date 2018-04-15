from Board import Board
from Player import Player
from Space import Buyablespace

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
        print(self.players)
        for player in self.players:
            space = self.board.change_position_dice(player=player)
            if isinstance(space, Buyablespace):
                print(space)
                if space.get_ownership(player=player):
                    print("Thanks for visiting sir")
                elif space.owned:
                    print("You have been charged" + str(space.rent(player=player)))
                else:
                    print("Would you like to purchase?")
                    if player.funds > space.get_cost():
                        space.purchase(player=player)
                        print("Thanks for buying")
                    else:
                        #this is where auction should go
                        print("That's ok")
            else:
                print(space)
            print(player.get_player_number())


    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)


main()
