
from Buyablespace import Buyablespace

DEFAULT_UTILITY_MULTIPLIER = 4
UTILITY_TWO_OWNED = 10


class Utility(Buyablespace):

    def __init__(self, name, cost, mortgage, two_owned):
        Buyablespace.__init__(name, cost, mortgage)
        self.two_owned = False

    def rent(self, dice_roll):
        if self.two_owned:
            return UTILITY_TWO_OWNED * dice_roll
        else:
            return DEFAULT_UTILITY_MULTIPLIER * dice_roll

    def two_owned(self):
        self.two_owned = True

    def one_owned(self):
        self.two_owned = False

