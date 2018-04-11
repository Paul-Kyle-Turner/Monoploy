import random


DEFAULT_STARTING_MONEY = 1500


class Player:

    def __init__(self):
        self.jailed = False
        self.money = DEFAULT_STARTING_MONEY

    @staticmethod
    def roll_dice():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1 + dice2

    def jail(self):
        self.jailed = True

    def release(self):
        self.jailed = False

