
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
                if player.jailed():
                    self.jail_turn(player=player)
                else:
                    doubles = self.game_turn(player=player)
                    if doubles:
                        doubles = self.game_turn(player=player)
                        if doubles:
                            self.board.get_jail_space().jail(player=player)
        else:
            print("The winner is")
            print(self.players)
            self.game_end = True

    def jail_turn(self, player):
        if player.get_jail_roll() > 2:
            print("It is the last day in jail, better pay up!")
            if player.has_get_out_of_jail_free():
                print("You had this card the entire time?")
                self.board.get_jail_space().get_out_of_jail_free_release(player)
            else:
                print("Thanks for paying")
                self.board.get_jail_space().pay_release()
        else:
            player_release = player.does_player_release()
            if player_release == 0:
                print("Rolling the dice are you?")
                player.roll_dice()
                if player.get_doubles():
                    print("Congrats... this time")
                    self.board.get_jail_space().release(player)
                else:
                    print("Stay in there")
            elif player_release == 1:
                print("Paying your way out?")
                self.board.get_jail_space().pay_release(player)
            elif player_release == 2:
                print("I thought I gave you one of these cards")
                self.board.get_jail_space().get_out_of_jail_free_release(player, board=self.board, game=self)

    def game_turn(self, player):
        print("PLAYER " + str(player.get_player_number()) + " TURN")
        print(self.board.get_jail_space().get_jail_list())
        position = player.get_position()
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
                    if isinstance(space, Property):
                        if player.has_monopoly(space=space):
                            print("You bought a monoploy, great job!")
                else:
                    # this is where auction should go
                    print("That's ok")
        elif isinstance(space, Drawspace):
            print(space)
            print(space.get_last_card())
        else:
            print(space)
        funds = player.get_funds()
        if len(player.get_monoploys()) > 0:
            if player.player_random_move():
                color = player.get_random_monoploy()
        if funds <= 0:
            difference = abs(funds)
            choice = player.does_player_mortgage_or_sell_house()
            if choice is None :
                self.players.remove(player)
                print("Player " + str(player.get_player_number()) + " has been eliminated.")
            elif choice:
                player.mortgage_till_value(difference)
            else:

        print("PLAYER TURN END")
        return player.get_doubles()

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)
