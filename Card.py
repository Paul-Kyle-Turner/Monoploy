
DEFAULT_COMMUNITY_HOUSE_REPAIR = 40
DEFAULT_COMMUNITY_HOTEL_REPAIR = 115
DEFAULT_CHANCE_HOUSE_REPAIR = 25
DEFAULT_CHANCE_HOTEL_REPAIR = 100


class Card:

    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def action(self, player, game):
        return

    def __str__(self):
        return self.description


class Collect(Card):

    def __init__(self, description, collect_amount):
        Card.__init__(self, description=description)
        self.collect_amount = collect_amount

    def action(self, player, game):
        player.add_funds(self.collect_amount)


class Collectmultiple(Collect):

    def action(self, player, game):
        player.add_funds(self.collect_amount * (game.get_num_players() - 1))
        for person in game.get_players():
            person.remove_funds(self.collect_amount)


class Pay(Card):

    def __init__(self, description, pay_amount):
        Card.__init__(self, description=description)
        self.pay_amount = pay_amount

    def action(self, player, game):
        player.remove_funds(self.pay_amount)


class PayMultiple(Pay):

    def action(self, player, game):
        player.remove_funds(self.pay_amount * (game.get_num_players() - 1))
        for person in game.get_players():
            person.add_funds(self.pay_amount)


class PayRepairs(Card):

    def __init__(self, description, chance):
        Card.__init__(self, description=description)
        self.chance = chance

    def action(self, player, game):
        houses, hotels = player.get_num_houses_hotels()
        if self.chance:
            player.remove_funds((houses * DEFAULT_COMMUNITY_HOUSE_REPAIR) + (hotels * DEFAULT_COMMUNITY_HOTEL_REPAIR))
        else:
            player.remove_funds((houses * DEFAULT_CHANCE_HOUSE_REPAIR) + (hotels * DEFAULT_CHANCE_HOTEL_REPAIR))


class GoBackThree(Card):

    def __init__(self, description):
        Card.__init__(self, description=description)

    def action(self, player, game):
        player.change_position_to(player.position - 3)


class Goto(Card):

    def __init__(self, description, position):
        Card.__init__(self, description=description)
        self.position = position

    def action(self, player, game):
        player.change_position_to(self.position)


class GotoNearestRailroad(Card):

    def __init__(self, description):
        Card.__init__(self, description=description)

    def action(self, player, game):
        if player.position == 7:
            position = 15
        elif player.position == 22:
            position = 26
        else:
            player.add_funds(200)
            position = 5
        player.change_position_to(position)


class GotoNearestUtility(Card):

    def __init__(self, description):
        Card.__init__(self, description=description)

    def action(self, player, game):
        if player.position < 13 or player.position > 29:
            position = 12
        else:
            position = 28
        player.change_position_to(position)


class GotoPassGo(Goto):

    def __init__(self, description, position):
        Goto.__init__(self, description=description, position=position)

    def action(self, player, game):
        if player.get_position() > self.position:
            player.add_funds(200)
        player.change_position_to(self.position)


class GotoJail(Goto):

    def __init__(self, description, position=11):
        Goto.__init__(self, description=description, position=position)

    def action(self, player, game):
        game.board.jail_space.jail(player)
        player.change_position_to(10)


class GetOutOfJail(Card):

    def __init__(self, chance, description="Get Out of Jail Free"):
        Card.__init__(self, description=description)
        self.chance = chance

    def get_chance(self):
        return self.chance

    def action(self, player, game):
        player.add_go_free_card(self, chance=self.get_chance())
