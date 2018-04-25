
# Author Paul Turner

from Color import Color
from Space import *
from Deck import CommunityChest, Chance

DEFAULT_BOARD_LENGTH = 28
DEFAULT_NUM_HOUSES = 32
DEFAULT_NUM_HOTELS = 12


class Board:

    def __init__(self, game):
        self.houses = 32
        self.hotels = 12
        self.chance = Chance()
        self.community_chest = CommunityChest()
        self.spaces = self.create_board()
        self.free_parking = 0
        self.game = game
        self.jail_space = self.spaces[10]

    # problems can occur
    def sell_house(self, space):
        house_level = space.get_house_level()
        if house_level > 0:
            space.decrease_house_level()
            if house_level == 5:
                self.houses -= 4
                self.hotels += 1
            else:
                self.houses += 1

    def purchase_house(self, space):
        if self.houses > 0:
            space.increase_house_level()
            if space.get_house_level == 5:
                self.houses += 4
                self.hotels -= 1
            else:
                self.houses -= 1
        return space.get_house_level()

    def change_position(self, player, position):
        player.change_position_to(position=position)
        self.spaces[position].land_on(self, player, self.game)

    # this is jank we can use observer but im lazy right now
    def change_position_dice(self, player):
        player.change_position_dice()
        location = player.get_position
        space = self.spaces[player.get_position()].land_on(board=self, player=player, game=self.game)
        location2 = player.get_position
        if location == location2:
            return space
        else:
            space = self.spaces[player.get_position()].land_on(board=self, player=player)
            return space

    def get_free_parking(self):
        return self.free_parking

    def get_jail_space(self):
        return self.jail_space

    def get_chance_deck(self):
        return self.chance

    def get_community_chest(self):
        return self.community_chest

    def set_chance_deck(self, chance):
        self.chance = chance

    def set_community_chest(self, community):
        self.community_chest = community

    def create_board(self):
        spaces = []

        # color creation
        brown = Color("brown")
        light_blue = Color("light_blue")
        purple = Color("purple")
        orange = Color("orange")
        red = Color("red")
        yellow = Color("yellow")
        green = Color("green")
        blue = Color("blue")

        # board creation
        go = Go()
        spaces.append(go)
        mediterranean = Property(name="mediterranean", cost=60, house0=2, house1=10, house2=30,
                                          house3=90, house4=160, hotel=250, mortgage=30, house_cost=50, color=brown)
        spaces.append(mediterranean)
        chest1 = Drawspace(name="Community Chest", chance=False)
        spaces.append(chest1)
        baltic = Property(name="baltic", cost=60, house0=4, house1=20, house2=60,
                                   house3=180, house4=320, hotel=450, mortgage=30, house_cost=50, color=brown)
        spaces.append(baltic)
        income_tax = IncomeTax()
        spaces.append(income_tax)
        reading_railroad = Railroad(name="reading_railroad")
        spaces.append(reading_railroad)
        oriental = Property(name="oriental", cost=100, house0=6, house1=30, house2=90,
                                     house3=270, house4=400, hotel=550, mortgage=50, house_cost=50, color=light_blue)
        spaces.append(oriental)
        chance1 = Drawspace(name="Chance", chance=True)
        spaces.append(chance1)
        vermont = Property(name="vermont", cost=100, house0=6, house1=30, house2=90,
                                    house3=270, house4=400, hotel=550, mortgage=50, house_cost=50, color=light_blue)
        spaces.append(vermont)
        connectiut = Property(name="connectiut", cost=120, house0=8, house1=40, house2=100,
                                       house3=300, house4=450, hotel=600, mortgage=60, house_cost=50, color=light_blue)
        spaces.append(connectiut)
        jail = Jail()
        spaces.append(jail)
        st_charles = Property(name="st_charles", cost=140, house0=10, house1=50, house2=150,
                                       house3=450, house4=625, hotel=750, mortgage=70, house_cost=100, color=purple)
        spaces.append(st_charles)
        electric_company = Utility(name="electric_company")
        spaces.append(electric_company)
        states_ave = Property(name="states_ave", cost=140, house0=10, house1=50, house2=150,
                                       house3=450, house4=625, hotel=750, mortgage=70, house_cost=100, color= purple)
        spaces.append(states_ave)
        virginia = Property(name="virginia", cost=160, house0=12, house1=60, house2=180,
                                     house3=500, house4=700, hotel=900, mortgage=80, house_cost=100, color=purple)
        spaces.append(virginia)
        pennsylvania_railroad = Railroad(name="pennsylvania_railroad")
        spaces.append(pennsylvania_railroad)
        st_james = Property(name="st_james", cost=180, house0=14, house1=70, house2=200,
                                     house3=550, house4=750, hotel=950, mortgage=90, house_cost=100, color=orange)
        spaces.append(st_james)
        spaces.append(chest1)
        tennessee = Property(name="tennessee", cost=180, house0=14, house1=70, house2=200,
                                      house3=550, house4=750, hotel=950, mortgage=90, house_cost=100, color=orange)
        spaces.append(tennessee)
        new_york = Property(name="new_york", cost=200, house0=16, house1=80, house2=220,
                                     house3=600, house4=800, hotel=1000, mortgage=100, house_cost=100, color=orange)
        spaces.append(new_york)
        free_parking = FreeParking()
        spaces.append(free_parking)
        kentucky = Property(name="kentucky", cost=220, house0=18, house1=90, house2=250,
                                     house3=700, house4=875, hotel=1050, mortgage=110, house_cost=150, color=red)
        spaces.append(kentucky)
        spaces.append(chance1)
        indiana = Property(name="kentucky", cost=220, house0=18, house1=90, house2=250,
                                    house3=700, house4=875, hotel=1050, mortgage=110, house_cost=150, color=red)
        spaces.append(indiana)
        illinois = Property(name="illinois", cost=240, house0=20, house1=100, house2=300,
                                     house3=750, house4=925, hotel=1100, mortgage=120, house_cost=150, color=red)
        spaces.append(illinois)
        bando_railroad = Railroad(name="BandO_railroad")
        spaces.append(bando_railroad)
        atlantic = Property(name="atlantic", cost=260, house0=22, house1=110, house2=330,
                                     house3=800, house4=975, hotel=1150, mortgage=130, house_cost=150, color=yellow)
        spaces.append(atlantic)
        ventnor = Property(name="ventnor", cost=260, house0=22, house1=110, house2=330,
                                    house3=800, house4=975, hotel=1150, mortgage=130, house_cost=150, color=yellow)
        spaces.append(ventnor)
        water_works = Utility(name="water_works")
        spaces.append(water_works)
        marvin_gardens = Property(name="marvin_gardens", cost=280, house0=24, house1=120, house2=360,
                                  house3=850, house4=1025, hotel=1200, mortgage=140, house_cost=150, color=yellow)
        spaces.append(marvin_gardens)
        go_to_jail = GoToJail()
        spaces.append(go_to_jail)
        pacific_ave = Property(name="pacific_ave", cost=300, house0=26, house1=130, house2=390,
                                        house3=900, house4=1100, hotel=1275, mortgage=150, house_cost=200, color=green)
        spaces.append(pacific_ave)
        north_carolina = Property(name="north_carolina", cost=300, house0=26, house1=130, house2=390,
                                    house3=900, house4=1100, hotel=1275, mortgage=150, house_cost=200, color=green)
        spaces.append(north_carolina)
        spaces.append(chest1)
        pennsylvania_ave = Property(name="pennsylvania_ave", cost=320, house0=28, house1=150, house2=450,
                                    house3=1000, house4=1200, hotel=1400, mortgage=160, house_cost=200, color=green)
        spaces.append(pennsylvania_ave)
        short_line = Railroad(name="short_line")
        spaces.append(short_line)
        spaces.append(chance1)
        park_place = Property(name="park_place", cost=350, house0=35, house1=175, house2=500,
                                       house3=1100, house4=1300, hotel=1500, mortgage=175, house_cost=200, color=blue)
        spaces.append(park_place)
        lux_tax = LuxTax()
        spaces.append(lux_tax)
        boardwalk = Property(name="boardwalk", cost=400, house0=50, house1=200, house2=600,
                                      house3=1400, house4=1700, hotel=2000, mortgage=200, house_cost=200, color=blue)
        spaces.append(boardwalk)

        # color creation
        brown.set_color_set([baltic, mediterranean])
        light_blue.set_color_set([connectiut, oriental, vermont])
        purple.set_color_set([virginia, st_charles, states_ave])
        orange.set_color_set([new_york, st_james, tennessee])
        red.set_color_set([illinois, indiana, kentucky])
        yellow.set_color_set([marvin_gardens, atlantic, ventnor])
        green.set_color_set([pennsylvania_ave, pacific_ave, north_carolina])
        blue.set_color_set([boardwalk, park_place])

        return spaces
