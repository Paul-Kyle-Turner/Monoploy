
from Buyablespace import Buyablespace

DEFAULT_OWNED = 1
DEFAULT_STARTING_RENT = 25
DEFAULT_RAILROAD_MULTIPLIER = 2


class Railroad(Buyablespace):

    def __init__(self, name, cost=200, mortgage=100):
        Buyablespace.__init__(name, cost, mortgage)
        self.owned = DEFAULT_OWNED

    def rent(self):
        rent = DEFAULT_STARTING_RENT
        for i in range(self.owned):
            rent = rent * DEFAULT_RAILROAD_MULTIPLIER
        return rent

    def add_stop(self):
        self.owned = self.owned + 1

    def lose_stop(self):
        self.owned = self.owned - 1

