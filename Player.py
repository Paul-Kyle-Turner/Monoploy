
# Author Paul Turner
import random
from Space import Property, Railroad, Utility


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
        self.doubles = False
        self.jail_roll = 0

    def does_player_release(self):
        release_state = 0
        if self.has_get_out_of_jail_free():
            release_state = 3
        else:
            release_state = 2
        states = []
        for i in range(release_state):
            states.append(i)
        return random.choice(states)

    def does_player_use_get_out_of_jail(self):
        if self.get_out_free_cards.count() > 0:
            return True
        else:
            return False

    def does_player_roll_or_pay(self):
        if random.random > .5:
            self.jail_roll += 1
            return True
        else:
            return False

    def is_equal(self, player):
        if self.get_player_number() == player.get_player_number():
            return True
        else:
            return False

    def has_space(self, space):
        if space in self.owned_spaces:
            return True
        else:
            return False

    def has_monopoly(self, space):
        color = space.get_color()
        spaces = color.get_color_set()
        for space in spaces:
            if not self.has_space(space):
                return False
        for space in spaces:
            space.to_monoploy()
        return True

    def has_get_out_of_jail_free(self):
        if self.get_num_go_free_cards() > 0:
            return True
        else:
            return False

    def get_owned_utilities(self):
        utilities = []
        for prop in self.owned_spaces:
            if isinstance(prop, Utility):
                utilities.append(prop)
        return utilities

    def get_owned_railroads(self):
        railroads = []
        for prop in self.owned_spaces:
            if isinstance(prop, Railroad):
                railroads.append(prop)
        return railroads

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

    def get_doubles(self):
        return self.doubles

    def get_jail_roll(self):
        return self.jail_roll

    def change_position_to(self, position):
        self.position = position

    def change_position_dice(self):
        self.position = ((self.position + self.roll_dice()) % DEFAULT_BOARD_SIZE)

    def get_num_houses_hotels(self):
        houses = 0
        hotels = 0
        for property_temp in self.owned_spaces:
            if isinstance(property_temp, Property):
                house_level = property_temp.get_house_level()
                if house_level <= 4:
                    houses += 1
                else:
                    hotels += 1
        return [houses, hotels]

    def add_go_free_card(self, card, chance):
        self.get_out_free_cards.append([card, chance])

    def return_go_free_card(self, board, game):
        print("RETURNING CARD")
        if len(self.get_out_free_cards) > 0:
            card = self.get_out_free_cards.pop(0)
            card[0].action(self, game)
            if card[1]:
                board.get_chance_deck().add_get_out_of_jail(chance=True)
            else:
                board.get_community_chest().add_get_out_of_jail(chance=False)

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
        if dice1 == dice2:
            self.doubles = True
        else:
            self.doubles = False
        self.last_roll = dice1 + dice2
        return dice1 + dice2

    def jail(self):
        print("jailing")
        self.jailed = True

    def release(self):
        self.jail_roll = 0
        self.jailed = False

