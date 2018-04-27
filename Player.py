
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
        self.player_random = random.random()
        self.monoploys = []

    def does_player_purchase_house(self):
        if self.has_monoploy():
            if self.player_random_move():
                return True
            else:
                return False

    def random_house_purchase(self):
        if self.get_num_monolpolys() > 0:
            monoploy = self.monoploys[random.randint(0, self.get_num_monolpolys() - 1)]
            high = monoploy.get_property(0).get_house_level()
            second = monoploy.get_property(1).get_house_level()
            third = None
            if len(monoploy.get_color_set()) > 2:
                third = monoploy.get_property(2).get_house_level()
            if third is not None:
                if high <= second or high <= third:
                    return monoploy.get_property(0)
                else:
                    return monoploy.get_property(random.randint(1, 2))
            else:
                if high <= second:
                    return monoploy.get_property(0)
                else:
                    return monoploy.get_property(1)

    def sell_house_till_value(self, value, board):
        house_total = 0
        numHouses = self.get_num_houses_hotels()
        for space in self.owned_spaces:
            if isinstance(space, Property) and space.get_house_level() > 0:
                while house_total < value and numHouses[0] > 0 and numHouses[1] > 0:
                    board.sell_house(space)
                    house_total += space.get_house_cost()
                    numHouses = self.get_num_houses_hotels()
        if house_total > value:
            self.add_funds(house_total)
            return True
        else:
            return False

        return None # Still working

    def player_random_move(self):
        if self.player_random >= random.random():
            return True
        else:
            return False

    def mortgage_till_value(self, value):
        mortgage = 0
        while value > mortgage:
            space = self.get_property_of_lowest_value()
            if space is not None:
                mortgage += space.set_mortgaged()
                for color in self.monoploys:
                    if color.has_property(space=space):
                        self.monoploys.remove(color)
            else:
                return False
        self.add_funds(mortgage)
        return True

    def does_player_mortgage_or_sell_house(self):
        if len(self.owned_spaces) > 0:
            if self.get_total_house_value() > 0:
                if self.player_random_move(): # player mortgages the lowest value house or houses that match the value
                    return False # sell house
                else:
                    return True # mortgage property
            else:
                return True
        else:
            return None

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
        if len(self.get_out_free_cards) > 0:
            return True
        else:
            return False

    def does_player_roll_or_pay(self):
        if self.player_random > random.random():
            self.jail_roll += 1
            return True
        else:
            return False

    def is_equal(self, player): # LOL __eq__ <( 'x' )>
        if self.get_player_number() == player.get_player_number():
            return True
        else:
            return False

    def has_space(self, space):
        if space in self.owned_spaces:
            return True
        else:
            return False

    def has_monoploy(self):
        return len(self.monoploys) > 0

    def has_monopoly_from_space(self, space):
        color = space.get_color()
        spaces = color.get_color_set()
        for space in spaces:
            if not self.has_space(space):
                return False
        for space in spaces:
            space.to_monoploy()
        self.monoploys.append(color)
        return True

    def has_get_out_of_jail_free(self):
        if self.get_num_go_free_cards() > 0:
            return True
        else:
            return False

    def get_total_house_value(self):
        total_house_value = 0
        for space in self.owned_spaces:
            if isinstance(space, Property):
                total_house_value += space.get_house_level()
        return total_house_value

    def get_random_monoploy(self):
        return self.monoploys[random.randint(0, len(self.monoploys))]

    def get_property_of_lowest_value(self):
        lowest_value_space = self.owned_spaces[0]
        for space in self.owned_spaces:
            if not space.get_mortgaged():
                if lowest_value_space.get_mortgage() > space.get_mortgage():
                    lowest_value_space = space
        return lowest_value_space

    def get_property_of_highest_value(self):
        lowest_value_space = None
        for space in self.owned_spaces:
            if not space.get_mortgaged():
                if lowest_value_space.get_mortgage() < space.get_mortgage():
                    lowest_value_space = space
        return lowest_value_space

    def get_monoploys(self):
        return self.monoploys

    def get_num_monolpolys(self):
        return len(self.monoploys)

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

    def change_position_to_pass_go(self, position):
        if self.position > position:
            self.add_funds(200)
        self.position = position

    def change_position_dice(self):
        position = self.position
        self.position = ((self.position + self.roll_dice()) % DEFAULT_BOARD_SIZE)
        if position > self.position:
            self.add_funds(200)

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

    def remove_space(self, space):
        self.owned_spaces.remove(space)

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

    def get_owned_spaces(self):
        return self.owned_spaces

    def trade(self, spacesIn, spacesOut, moneyOffered):
        amountOffered = moneyOffered
        for space in spacesIn:
            amountOffered =+ space.get_mortgage()
        amountAsked = 0
        for space in spacesOut:
            amountAsked += space.get_mortgage()
        amountAsked = random.randint(0, amountAsked)
        amountOffered = random.randint(0, amountOffered)
        if amountAsked < amountOffered:
            return False
        else:
            return True