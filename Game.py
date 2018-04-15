from Board import Board
from Player import Player
from Space import *

DEFAULT_ROUNDS_RULE = 20


def main():
    game = Game()
    game.game_play()


class Game:

    def __init__(self, num_players=4):
        self.round_count = 0
        self.board = Board(game=self)
        self.players = self.create_players(num_players)

    @staticmethod
    def create_players(num_players):
        players = []
        for i in range(num_players):
            player = Player(i)
            players.append(player)
        return players

    def game_play(self):
        for round in range(DEFAULT_ROUNDS_RULE):
            self.game_round()

    def game_round(self):
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
            elif isinstance(space, Drawspace):
                print("indraw")
                print(space.get_last_card())
            else:
                print(space)
            print(player.get_player_number())
            if player.get_funds() < 0:
                self.players.remove(player)
                print("Player " + str(player.get_player_number()) + " has been eliminated.")



    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)


main()
