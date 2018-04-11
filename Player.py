import random


DEFAULT_STARTING_MONEY = 1500


class Player:

    def __init__(self):
        self.jailed = False
        self.money = DEFAULT_STARTING_MONEY
        self.owned_spaces = []

    def add_funds(self, money):
        self.money = self.money + money

    def remove_funds(self, money):
        self.money = self.money - money

    def remove_space(self, space):
        del self.owned_spaces[space]

    def add_owned_space(self, space):
        self.owned_spaces.append(space)

    @staticmethod
    def roll_dice():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1 + dice2

    def jail(self):
        self.jailed = True

    def release(self):
        self.jailed = False

