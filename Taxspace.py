
from Space import Space
from Player import Player

DEFAULT_LUX_TAX = 100
DEFAULT_INCOME_TAX = 200


class LuxTax(Space):

    def __init__(self, name="Luxury_tax"):
        Space.__init__(name=name)

    @staticmethod
    def charge_player(player):
        player.remove_funds(DEFAULT_LUX_TAX)


class IncomeTax(Space):

    def __init__(self, name="Income_tax"):
        Space.__init__(name=name)

    @staticmethod
    def charge_player(percent, player):
        if percent:
            player.remove_funds(player.worth() / 5)
        else:
            player.remove_funds(DEFAULT_INCOME_TAX)
