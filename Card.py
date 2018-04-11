
from Player import Player
from Game import Game
from Deck import Deck

class Card:

    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def action(self, player):
        return


class Collect(Card):

    def __init__(self, description, collect_amount):
        Card.__init__(description=description)
        self.collect_amount = collect_amount

    def action(self, player):
        player.add_funds(self.collect_amount)

class Collectmultiple(Collect)

    def action(self, player):
        player.add_funds(self.collect_amount * (Game.get_num_players() - 1))
        for person in Game.players:
            person.remove_funds(self.collect_amount)


class Pay(Card):

    def __init__(self, description, pay_amount):
        Card.__init__(description=description)
        self.pay_amount = pay_amount

    def action(self, player):
        player.remove_funds(self.pay_amount)

DEFAULT_HOUSE_REPAIR = 40
DEFAULT_HOTEL_REPAIR = 115


class PayRepairs(Card):

    def action(self, player):
        houses, hotels = player.get_num_houses_hotels()
        player.remove_funds((houses * DEFAULT_HOUSE_REPAIR) + (hotels * DEFAULT_HOTEL_REPAIR))


class Goto(Card):

    def __init__(self, description, position):
        Card.__init__(description=description)
        self.position = position

    def action(self, player):
        player.change_position_to(self.position)


class GotoNearestRailroad(Goto):

    def __init__(self, description, position, player):
        if player.position == 8:
            position = 16
        elif player.position == 23
            position = 26
        else:
            player.
            position = 6
        Goto.__init__(description=description, position=position)


class GotoNearestUtility(Goto):

    def __init__(self, description, position, player):
        if player.position < 13 or player.position > 29:
            position = 12
        else:
            position = 28
        Goto.__init__(description=description, position=position)


class GotoPassGo(Goto):

    def __init__(self, description, position):
        Goto.__init__(description=description, position=position)

    def action(self, player):
        if player.get_position() > self.position():
            player.add_funds(200)
        player.change_position_to(self.position)


class GotoJail(Goto):

    def __init__(self, description, position=11):
        Goto.__init__(description=description, position=position)

    def action(self, player):
        player.jailed()
        player.change_position_to(11)

class Get_Out_Of_Jail(Card):

    def __init__(self, description):
        Card.__init__(description=description)

    def action(self, player):
        player.release()
