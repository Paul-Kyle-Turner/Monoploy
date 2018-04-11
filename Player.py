import random


DEFAULT_STARTING_MONEY = 1500
DEFAULT_BOARD_SIZE = 40


class Player:

    def __init__(self):
        self.jailed = False
        self.money = DEFAULT_STARTING_MONEY
        self.owned_spaces = []
        self.position = 0
        self.get_out_free_cards = []

    def get_num_houses_hotels(self):
        houses = 0
        hotels = 0
        for property_temp in self.owned_spaces:
            house_level = property_temp.get_house_level()
            if house_level <= 4:
                houses += 1
            else:
                hotels += 1

        return [houses, hotels]

    def add_go_free_card(self, card):
        self.get_out_free_cards.append(card)

    def return_go_free_card(self,board):


    def get_num_go_free_cards(self):
        return len(self.get_out_free_cards)

    def get_position(self):
        return self.position

    def change_position_to(self, position):
        self.position = position

    def change_position_dice(self):
        self.position = ((self.position + self.roll_dice()) % DEFAULT_BOARD_SIZE)

    def worth(self):
        worth = self.money
        for property_temp in self.owned_spaces:
            worth = worth + property_temp.prop_cost()
        return worth

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

