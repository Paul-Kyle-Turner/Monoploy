
from Space import Space


class Buyablespace(Space):

    def __init__(self, cost, mortgage):
        self.cost = cost
        self.mortgage = mortgage
        self.mortgaged = False

    def get_rent(self):
        return self.rent

    def get_mortgage(self):
        return self.mortgage

    def get_mortgaged(self):
        return self.mortgaged

    def get_cost(self):
        return self.cost

    def fix(self):
        self.mortgaged = False

    def mortgaged(self):
        self.mortgaged = True
