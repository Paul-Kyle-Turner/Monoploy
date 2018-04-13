
DEFAULT_LUX_TAX = 100
DEFAULT_INCOME_TAX = 200
DEFAULT_HOUSE_LEVEL = 0
DEFAULT_OWNED = 1
DEFAULT_STARTING_RENT = 25
DEFAULT_RAILROAD_MULTIPLIER = 2
DEFAULT_UTILITY_MULTIPLIER = 4
UTILITY_TWO_OWNED = 10
DEFAULT_CHANCE_DECK = True
DEFAULT_COMMUNITY_CHEST_DECK = False
DEFAULT_GO_FUNDS = 200
DEFAULT_VISITING = True
DEFAULT_FREE_PARKING = True


class Space:

    def __init__(self, name):
        self.name = name

    def land_on(self, board, player):
        return

    def get_name(self):
        return self.name


class GoToJail(Space):

    def __init__(self, name="Go to Jail"):
        Space.__init__(name=name)

    def land_on(self, board, player):
        board.change_position(player=player, position=11)


class FreeParking(Space):

    def __init__(self, name="Free Parking"):
        Space.__init__(name=name)

    def land_on(self, board, player):
        if DEFAULT_FREE_PARKING:
            return
        else:
            return board.get_free_parking()


class Jail(Space):

    def __init__(self, name="Jail"):
        Space.__init__(name=name)
        self.jail_list = []

    def jail(self, player):
        player.jailed()
        self.jail_list.append(player)

    def release(self, player):
        player.release()
        del self.jail_list[player]

    def land_on(self, board, player):
        if DEFAULT_VISITING:
            return
        else:
            self.jail(player)


class Go(Space):

    def __init__(self, name="Go"):
        Space.__init__(name=name)

    def land_on(self, board, player):
        player.add_funds(DEFAULT_GO_FUNDS)


class Buyablespace(Space):

    def __init__(self, name, cost, mortgage):
        Space.__init__(name=name)
        self.cost = cost
        self.mortgage = mortgage
        self.mortgaged = False

    def prop_cost(self):
        if self.mortgaged:
            return self.cost
        else:
            return self.mortgage

    def land_on(self, board, player):
        self.rent()

    def rent(self):
        return 0

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


class Drawspace(Space):

    def __init__(self, name, chance):
        Space.__init__(name=name)
        self.chance = chance

    def draw_card(self, player, board):
        if self.chance:
            deck = board.get_chance_deck()
        else:
            deck = board.get_community_chest()
        card = deck.pop_card()
        card.action(player)


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


class Property(Buyablespace):
    def __init__(self, name, cost, house0, house1, house2, house3, house4, hotel, mortgage, house_cost):
        Buyablespace.__init__(name, cost, mortgage)
        self.house0 = house0
        self.house1 = house1
        self.house2 = house2
        self.house3 = house3
        self.house4 = house4
        self.hotel = hotel
        self.house_cost = house_cost
        self.house_level = DEFAULT_HOUSE_LEVEL

    def prop_cost(self):
        if self.mortgaged:
            return self.cost + (self.house_cost * self.house_level)
        else:
            return self.mortgage

    def rent(self):
        if self.house_level == 0:
            return self.get_house0()
        elif self.house_level == 1:
            return self.house1
        elif self.house_level == 2:
            return self.house2
        elif self.house_level == 3:
            return self.house3
        elif self.house_level == 4:
            return self.house4
        elif self.house_level == 5:
            return self.hotel

    def change_house_level(self, house_level):
        self.house_level = house_level

    def get_house_level(self):
        return self.house_level

    def get_house0(self):
        return self.house0

    def get_house1(self):
        return self.house1

    def get_house2(self):
        return self.house2

    def get_house3(self):
        return self.house3

    def get_house4(self):
        return self.house4

    def get_hotel(self):
        return self.hotel


class Utility(Buyablespace):

    def __init__(self, name, cost=150, mortgage=75):
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