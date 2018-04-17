
# Author Paul Turner

from Board import Board
from Player import Player
from Space import *

DEFAULT_ROUNDS_RULE = 1000


class Game:

    def __init__(self, num_players=4):
        self.round_count = 0
        self.board = Board(game=self)
        self.players = self.create_players(num_players)
        self.game_end = False

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
            if self.game_end:
                return

    def game_round(self):
        self.round_count += 1
        if len(self.players) > 1:
            for player in self.players:
                self.game_turn(player=player)
        else:
            print("The winner is")
            print(self.players)
            self.game_end = True

    def game_turn(self, player):
        print("PLAYER " + str(player.get_player_number()) + " TURN")
        print(player.get_position())
        print(self.board.jail_space.get_jail_list())
        if player.get_jailed():
            if player.get_jail_roll() > 2:
                print("It is the last day in jail, better pay up!")
                if player.has_get_out_of_jail_free():
                    print("You had this card the entire time?")
                    self.board.jail_space.get_out_of_jail_free_release(player)
                else:
                    print("Thanks for paying")
                    self.board.jail_space.pay_release()
            else:
                player_release = player.does_player_release()
                if player_release == 0:
                    print("Rolling the dice are you?")
                    player.roll_dice()
                    if player.get_doubles():
                        print("Congrats... this time")
                        self.board.jail_space.release(player)
                    else:
                        print("Stay in there")
                elif player_release == 1:
                    print("Paying your way out?")
                    self.board.jail_space.pay_release(player)
                elif player_release == 2:
                    print("I thought I gave you one of these cards")
                    self.board.jail_space.get_out_of_jail_free_release(player, board=self.board, game=self)
        else:
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
                        # this is where auction should go
                        print("That's ok")
            elif isinstance(space, Drawspace):
                print("indraw")
                print(space)
                print(space.get_last_card())
            else:
                print(space)
        if player.get_funds() < 0:
            self.players.remove(player)
            print("Player " + str(player.get_player_number()) + " has been eliminated.")
        print(player.get_position())
        print("PLAYER TURN END")

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)
