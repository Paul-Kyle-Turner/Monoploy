from Property import Property
from Railroad import Railroad
from Utility import Utility
from Buyablespace import Buyablespace

DEFAULT_BOARD_LENGTH = 28

class Board:

    def __init__(self):
        self.houses = 32
        self.hotels = 12
        self.chance = self.create_chance()
        self.community_chest = self.create_community_chest()
        self.spaces = self.create_properties()

    def create_properties(self):
        spaces = []
        mediterranean = Property.__init__(name="mediterranean", cost=60, house0=2, house1=10, house2=30,
                                          house3=90, house4=160, hotel=250, mortgage=30)
        spaces.append(mediterranean)
        baltic = Property.__init__(name="baltic", cost=60, house0=4, house1=20, house2=60,
                                   house3=180, house4=320, hotel=450, mortgage=30)
        spaces.append(baltic)
        reading_railroad = Railroad.__init__(name="reading_railroad")
        oriental = Property.__init__(name="oriental", cost=100, house0=6, house1=30, house2=90,
                                     house3=270, house4=400, hotel=550, mortgage=50)
        vermont = Property.__init__(name="vermont", cost=100, house0=6, house1=30, house2=90,
                                    house3=270, house4=400, hotel=550, mortgage=50)
        connectiut = Property.__init__(name="connectiut", cost=120, house0=8, house1=40, house2=100,
                                       house3=300, house4=450, hotel=600, mortgage=60)
        st_charles = Property.__init__(name="st_charles", cost=140, house0=10, house1=50, house2=150,
                                       house3=450, house4=625, hotel=750, mortgage=70)
        states_ave = Property.__init__(name="states_ave", cost=140, house0=10, house1=50, house2=150,
                                       house3=450, house4=625, hotel=750, mortgage=70)
        virginia = Property.__init__(name="virginia", cost=160, house0=12, house1=60, house2=180,
                                     house3=500, house4=700, hotel=900, mortgage=80)
        st_james = Property.__init__(name="st_james", cost=180, house0=14, house1=70, house2=200,
                                     house3=550, house4=750, hotel=950, mortgage=90)
        tennessee = Property.__init__(name="tennessee", cost=180, house0=14, house1=70, house2=200,
                                      house3=550, house4=750, hotel=950, mortgage=90)
        new_york = Property.__init__(name="new_york", cost=200, house0=16, house1=80, house2=220,
                                     house3=600, house4=800, hotel=1000, mortgage=100)
        kentucky = Property.__init__(name="kentucky", cost=220, house0=18, house1=90, house2=250,
                                     house3=700, house4=875, hotel=1050, mortgage=110)
        indiana = Property.__init__(name="kentucky", cost=220, house0=18, house1=90, house2=250,
                                    house3=700, house4=875, hotel=1050, mortgage=110)
        illinois = Property.__init__(name="illinois", cost=240, house0=20, house1=100, house2=300,
                                     house3=750, house4=925, hotel=1100, mortgage=120)
        atlantic = Property.__init__(name="atlantic", cost=260, house0=22, house1=110, house2=330,
                                     house3=800, house4=975, hotel=1150, mortgage=130)
        ventnor = Property.__init__(name="ventnor", cost=260, house0=22, house1=110, house2=330,
                                    house3=800, house4=975, hotel=1150, mortgage=130)
        marvin_gardens = Property.__init__(name="marvin_gardens", cost=280, house0=24, house1=120, house2=360,
                                           house3=850, house4=1025, hotel=1200, mortgage=140)
        pacific_ave = Property.__init__(name="pacific_ave", cost=300, house0=26, house1=130, house2=390,
                                        house3=900, house4=1100, hotel=1275, mortgage=150)
        north_carolina = Property.__init__(name="north_carolina", cost=300, house0=26, house1=130, house2=390,
                                           house3=900, house4=1100, hotel=1275, mortgage=150)
        pennsylvania_ave = Property.__init__(name="pennsylvania_ave", cost=320, house0=28, house1=150, house2=450,
                                             house3=1000, house4=1200, hotel=1400, mortgage=160)
        park_place = Property.__init__(name="park_place", cost=350, house0=35, house1=175, house2=500,
                                       house3=1100, house4=1300, hotel=1500, mortgage=175)
        boardwalk = Property.__init__(name="boardwalk", cost=400, house0=50, house1=200, house2=600,
                                      house3=1400, house4=1700, hotel=2000, mortgage=200)

    def create_chance(self):
        return []