
# Author Paul Turner

from Board import Board
from Player import Player
from Space import *
import random

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
            if len(self.players) > 1:
                self.game_round()
            else:
                print("The winner is")
                print(self.players)
                self.game_end = True
            if self.game_end:
                return

    def game_round(self):
        self.round_count += 1
        for player in self.players:
            for player2 in self.players:
                if player != player2:
                    self.trade(player, player2)
            if player.jailed:
                self.jail_turn(player=player)
            else:
                doubles = self.game_turn(player=player)
                if doubles:
                    print("You got doubles, have another turn")
                    doubles = self.game_turn(player=player)
                    if doubles:
                        print("We clocked him going 26 in a 25")
                        self.board.get_jail_space().jail(player=player)


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
        print("PLAYER " + str(player.get_player_number()) + " TURN $" + str(player.get_funds()))
        print(self.board.get_jail_space().get_jail_list())
        position = player.get_position()
        space = self.board.change_position_dice(player=player)
        if isinstance(space, Buyablespace):
            print(space)
            if space.get_ownership(player=player):
                print("Thanks for visiting sir")
            elif space.owned:
                rent = space.rent(player)
                player.remove_funds(rent)
                space.get_owner().add_funds(rent)
                print("You have been charged" + str(rent))
            else:
                print("Would you like to purchase?")
                if player.funds > space.get_cost():
                    space.purchase(player=player)
                    print("Thanks for buying")
                    if isinstance(space, Property):
                        if player.has_monopoly_from_space(space=space):
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
        if funds <= 0:
            difference = abs(funds)
            choice = player.does_player_mortgage_or_sell_house()
            if choice is None :
                self.players.remove(player)
                print("Player " + str(player.get_player_number()) + " has been eliminated.")
                return False
            elif choice:
                if not player.mortgage_till_value(difference):
                    if not player.sell_house_till_value(difference, self.board):
                        self.players.remove(player)
                        print("Player " + str(player.get_player_number()) + " has been eliminated.")
                        return False
            else:
                if not player.sell_house_till_value(difference, self.board):
                    if not player.mortgage_till_value(difference):
                        self.players.remove(player)
                        print("Player " + str(player.get_player_number()) + " has been eliminated.")
                        return False
        elif player.does_player_purchase_house():
            self.board.purchase_house(player.random_house_purchase())
        print("PLAYER TURN END")
        return player.get_doubles()

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)

    def trade(self, player1, player2):
        print("Would you like to trade with PLAYER " + str(player2.get_player_number()))
        if len(player1.get_owned_spaces()) > 0 and len(player2.get_owned_spaces()) > 0:
            spacesWanted = []
            colors = []
            for space1 in player1.get_owned_spaces():
                for space2 in player2.get_owned_spaces():
                    check = True
                    for color in colors:
                        if isinstance(space1, Property) and color.equals(space1.get_color()):
                            check = False
                    if check:
                        if isinstance(space1, Property) and isinstance(space2, Property):
                            if(space1.get_color() == space2.get_color()):
                                spacesWanted.append(space2)
                            colors.append(space1.get_color())
            numColors = random.randint(0, len(colors))
            for color in colors:
                if random.randint(0, len(colors)) < numColors:
                    colors.remove(color)
            for space in spacesWanted:
                keep = False
                for color in colors:
                    if space.get_color().equals(color):
                        keep = True
                if not keep:
                    spacesWanted.remove(space)
            spacesOffered = []
            for space1 in player1.get_owned_spaces():
                for space2 in spacesWanted:
                    if not isinstance(space1, Property) or space1.get_color() != space2.get_color():
                        spacesOffered.append(space1)
            if len(spacesOffered) > 0 and len(spacesWanted) > 0:
                wantedAmount = 0
                for space in spacesWanted:
                    wantedAmount += space.get_mortgage()
                offeredAmount = 0
                for space in spacesOffered:
                    offeredAmount += space.get_mortgage()
                if player1.get_funds() > 0:
                    moneyOffered = random.randint(0, player1.get_funds())
                else:
                    moneyOffered = 0
                offeredAmount += moneyOffered
                offeredAmount = random.randint(0, offeredAmount)
                wantedAmount = random.randint(0, wantedAmount)
                if wantedAmount > offeredAmount:
                    if player1.get_funds() > 0:
                        moneyOffered = random.randint(0, player1.get_funds())
                    else:
                        moneyOffered = 0
                    offeredAmount += moneyOffered
                    if offeredAmount > wantedAmount:
                        highest = spacesOffered[0]
                        for space in spacesOffered:
                            if space.get_mortgage() > highest.get_mortgage():
                                highest = space
                        spacesOffered.remove(highest)
                    elif wantedAmount > offeredAmount:
                        highest = spacesWanted[0]
                        for space in spacesWanted:
                            if space.get_mortgage() > highest.get_mortgage():
                                highest = space
                        spacesWanted.remove(highest)
                if offeredAmount > wantedAmount:
                    count = 0
                    while offeredAmount > wantedAmount and len(spacesOffered) > 0 and count < 5:
                        highest = spacesOffered[0]
                        if random.randint(0, 1) == 0:
                            for space in spacesOffered:
                                if space.get_mortgage() > highest.get_mortgage():
                                    highest = space
                            spacesOffered.remove(highest)
                        else:
                            wanted = True
                            count2 = 0
                            space = player2.get_property_of_lowest_value()
                            while wanted and count2 < 5:
                                space = player2.get_owned_spaces()[random.randint(0, len(player2.get_owned_spaces()) - 1)]
                                wanted = False
                                for space2 in spacesWanted:
                                    if space == space2:
                                        wanted = True
                                count2 += 1
                            if not wanted:
                                spacesWanted.append(space)
                        wantedAmount = 0
                        for space in spacesWanted:
                            wantedAmount += space.get_mortgage()
                        offeredAmount = 0
                        for space in spacesOffered:
                            offeredAmount += space.get_mortgage()
                        if player1.get_funds() > 0:
                            moneyOffered = random.randint(0, player1.get_funds())
                        else:
                            moneyOffered = 0
                        offeredAmount += moneyOffered
                        offeredAmount = random.randint(0, offeredAmount)
                        wantedAmount = random.randint(0, wantedAmount)
                        count += 1
                if player2.trade(spacesWanted, spacesOffered, moneyOffered):
                    print("PLAYER " + str(player1.get_player_number()) + " recieves")
                    for space in spacesWanted:
                        player2.remove_space(space)
                        player1.add_owned_space(space)
                        space.change_owner(player1)
                        print(space)
                        if isinstance(space, Property):
                            player1.has_monopoly_from_space(space)
                            print("You bought a monoploy, great job!")
                    print("PLAYER " + str(player2.get_player_number()) + " recieves")
                    for space in spacesOffered:
                        player1.remove_space(space)
                        player2.add_owned_space(space)
                        space.change_owner(player2)
                        print(space)
                        if isinstance(space, Property):
                            player2.has_monopoly_from_space(space)
                            print("You bought a monoploy, great job!")
                    print("PLAYER " + str(player2.get_player_number()) + " recieves $" + str(moneyOffered))
                    player2.add_funds(moneyOffered)
                    player1.remove_funds(moneyOffered)