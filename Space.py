
# Author Paul Turner

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
DEFAULT_MONOPOLY_MULTIPLIER = 2


class Space:

    def __init__(self, name):
        self.name = name
        self.num_landed_on = 0

    def land_on(self, board, player, game):
        self.land()
        return self

    def get_times_landed(self):
        return self.num_landed_on

    def get_name(self):
        return self.name

    def land(self):
        self.num_landed_on += 1

    def __str__(self):
        return "This message should not appear"


class GoToJail(Space):

    def __init__(self, name="Go to Jail"):
        Space.__init__(self, name=name)

    def land_on(self, board, player, game):
        self.land()
        game.board.jail_space.jail(player)
        return self

    def __str__(self):
        return "You have been sent to jail <( *_* )>"


class FreeParking(Space):

    def __init__(self, name="Free Parking"):
        Space.__init__(self, name=name)

    def land_on(self, board, player, game):
        if DEFAULT_FREE_PARKING:
            return self
        else:
            player.add_funds(board.get_free_parking())
            return self

    def __str__(self):
        return "You have got a free ride this time"


class Jail(Space):

    def __init__(self, name="Jail"):
        Space.__init__(self, name=name)
        self.jail_list = []

    def get_jail_list(self):
        return self.jail_list

    def jail(self, player):
        player.jail()
        player.change_position_to(10)
        print("JAIL JAIL JAIL")
        self.jail_list.append(player)
        print(player.get_jailed())

    def release(self, player):
        player.release()
        self.jail_list.remove(player)

    def get_out_of_jail_free_release(self, player, board, game):
        player.return_go_free_card(board=board, game=game)
        self.release(player)

    def pay_release(self, player):
        player.remove_funds(50)
        self.release(player)

    def land_on(self, board, player, game):
        self.land()
        if player.get_jailed():
            self.jail_list.append(player)
            return self
        if DEFAULT_VISITING:
            return self
        else:
            self.jail(player)
            return self

    def __str__(self):
        jailed_players = ""
        if len(self.jail_list) > 0:
            for player in self.jail_list:
                jailed_players += str(player.get_player_number()) + " "
            return "The following players are in jail" + jailed_players
        else:
            return "Have a good stay at jail."



class Go(Space):

    def __init__(self, name="Go"):
        Space.__init__(self, name=name)

    def land_on(self, board, player, game):
        self.land()
        player.add_funds(DEFAULT_GO_FUNDS)
        return self

    def __str__(self):
        return "You landed on GO"


# buyable spaces need to be able to be purchased if unowned.
# land on needs to change to check owned.
class Buyablespace(Space):

    def __init__(self, name, cost, mortgage):
        Space.__init__(self, name=name)
        self.cost = cost
        self.mortgage = mortgage
        self.mortgaged = False
        self.owned = False
        self.owner = None

    def prop_cost(self):
        if self.mortgaged:
            return self.cost
        else:
            return self.mortgage

    def land_on(self, board, player, game):
        self.land()
        if self.get_ownership(player):
            return self
        elif self.owned:
            player.remove_funds(self.rent(player=player))
            return self
        else:
            return self

    def rent(self, player):
        return 0

    # make this able to do the monoploy
    def purchase(self, player):
        player.remove_funds(self.cost)
        player.add_owned_space(self)
        self.owner = player
        self.owned = True

    def get_mortgage(self):
        return self.mortgage

    def get_mortgaged(self):
        return self.mortgaged

    def get_cost(self):
        return self.cost

    def get_ownership(self, player):
        if self.owner is None:
            return self.owned
        elif player.is_equal(self.owner):
            return self.owned
        else:
            return False

    def get_owner(self):
        return self.owner

    def change_owner(self, player):
        self.owner = player

    def fix(self):
        self.mortgaged = False

    def set_mortgaged(self):
        self.mortgaged = True
        return self.mortgage

    def __str__(self):
        if self.owned:
            return "The owner of the property is " + str(self.owner.get_player_number()) + "."
        else:
            return "Hope you have a good stay!"


class LuxTax(Space):

    def __init__(self, name="Luxury_tax"):
        Space.__init__(self, name=name)

    def land_on(self, board, player, game):
        self.land()
        self.charge_player(player=player)
        return self

    @staticmethod
    def charge_player(player):
        player.remove_funds(DEFAULT_LUX_TAX)

    def __str__(self):
        return "You have been taxed because you like nice things"


class IncomeTax(Space):

    def __init__(self, name="Income_tax"):
        Space.__init__(self, name=name)

    def land_on(self, board, player, game):
        self.land()
        self.charge_player(player=player)
        return self

    @staticmethod
    def charge_player(player):
        player_worth = player.worth()
        if player_worth < DEFAULT_INCOME_TAX:
            player.remove_funds(player_worth / 5)
        else:
            player.remove_funds(DEFAULT_INCOME_TAX)

    def __str__(self):
        return "You have been charged some taxes, the lower amount"


class Drawspace(Space):

    def __init__(self, name, chance):
        Space.__init__(self, name=name)
        self.chance = chance
        self.last_card = None

    def get_last_card(self):
        return self.last_card

    def land_on(self, board, player, game):
        self.land()
        self.draw_card(player=player, board=board, game=game)
        return self

    def draw_card(self, player, board, game):
        if self.chance:
            deck = board.get_chance_deck()
        else:
            deck = board.get_community_chest()
        card = deck.pop_card()
        card.action(player=player, game=game)
        self.last_card = card
        return card

    def __str__(self):
        return "You draw a card and it is "


class Railroad(Buyablespace):

    def __init__(self, name, cost=200, mortgage=100):
        Buyablespace.__init__(self, name, cost, mortgage)

    def purchase(self, player):
        super().purchase(player=player)
        railroads = player.get_owned_railroads()
        for railroad in railroads:
            railroad.set_stop(len(railroads))

    def rent(self, player):
        rent = DEFAULT_STARTING_RENT
        for i in range(self.owned):
            rent = rent * DEFAULT_RAILROAD_MULTIPLIER
        return rent

    def set_stop(self, num_stops):
        self.owned = num_stops

    def add_stop(self):
        self.owned = self.owned + 1

    def lose_stop(self):
        self.owned = self.owned - 1

    def __str__(self):
        return "CHOO CHOO, take a ride on the " + self.get_name() + ". " + super().__str__()


class Property(Buyablespace):
    def __init__(self, name, cost, house0, house1, house2, house3, house4, hotel, mortgage, house_cost, color):
        Buyablespace.__init__(self, name, cost, mortgage)
        self.color = color
        self.house0 = house0
        self.house1 = house1
        self.house2 = house2
        self.house3 = house3
        self.house4 = house4
        self.hotel = hotel
        self.house_cost = house_cost
        self.house_level = DEFAULT_HOUSE_LEVEL

    def to_monoploy(self):
        self.house0 = self.house0 * DEFAULT_MONOPOLY_MULTIPLIER

    def prop_cost(self):
        if self.mortgaged:
            return self.cost + (self.house_cost * self.house_level)
        else:
            return self.mortgage

    def rent(self, player):
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

    def increase_house_level(self):
        if self.house_level < 5:
            self.house_level += 1

    def decrease_house_level(self):
        if self.house_level > 0:
            self.house_level -= 1

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

    def get_color(self):
        return self.color

    def get_house_cost(self):
        return self.house_cost

    def __str__(self):
        return "Nice property here in " + self.get_name() + ". " + super().__str__()


class Utility(Buyablespace):

    def __init__(self, name, cost=150, mortgage=75):
        Buyablespace.__init__(self, name, cost, mortgage)
        self.two_owned = False

    def purchase(self, player):
        super().purchase(player=player)
        utilities = player.get_owned_utilities()
        for utility in utilities:
            utility.make_two_owned()

    def rent(self, player):
        if self.two_owned:
            return UTILITY_TWO_OWNED * player.get_last_roll()
        else:
            return DEFAULT_UTILITY_MULTIPLIER * player.get_last_roll()

    def make_two_owned(self):
        self.two_owned = True

    def make_one_owned(self):
        self.two_owned = False

    def __str__(self):
        return "Water or electric, why not both? " + self.get_name() + ". " + super().__str__()
