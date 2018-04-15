import random


DEFAULT_STARTING_FUNDS = 1500
DEFAULT_BOARD_SIZE = 40


class Player:

    def __init__(self, number):
        self.jailed = False
        self.funds = DEFAULT_STARTING_FUNDS
        self.owned_spaces = []
        self.position = 0
        self.get_out_free_cards = []
        self.player_number = number
        self.last_roll = 0

    def is_equal(self, player):
        if self.get_player_number() == player.get_player_number():
            return True
        else:
            return False

    def get_player_number(self):
        return self.player_number

    def get_num_go_free_cards(self):
        return len(self.get_out_free_cards)

    def get_position(self):
        return self.position

    def get_jailed(self):
        return self.jailed

    def get_last_roll(self):
        return self.last_roll

    def get_funds(self):
        return self.funds

    def change_position_to(self, position):
        self.position = position

    def change_position_dice(self):
        self.position = ((self.position + self.roll_dice()) % DEFAULT_BOARD_SIZE)

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

    def add_go_free_card(self, card, chance):
        self.get_out_free_cards.append([card, chance])

    def return_go_free_card(self, board):
        if len(self.get_out_free_cards) > 0:
            card = self.get_out_free_cards.pop(0)
            card.action(self)
            if card.get_chance():
                board.get_chance_deck().add_get_out_of_jail()
            else:
                board.get_community_chest().add_get_out_of_jail()

    def worth(self):
        worth = self.funds
        for property_temp in self.owned_spaces:
            worth = worth + property_temp.prop_cost()
        return worth

    def add_funds(self, funds):
        self.funds = self.funds + funds

    def remove_funds(self, funds):
        self.funds = self.funds - funds

    def remove_space(self, space):
        del self.owned_spaces[space]

    def add_owned_space(self, space):
        self.owned_spaces.append(space)

    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.last_roll = dice1 + dice2
        return dice1 + dice2

    def jail(self):
        self.jailed = True

    def release(self):
        self.jailed = False

