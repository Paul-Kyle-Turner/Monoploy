
DEFAULT_HOUSE_LEVEL = 0


class Property:

    def __init__(self, name, rent, house1, house2, house3, house4, hotel, mortgage):
        self.name = name
        self.rent = rent
        self.house1 = house1
        self.house2 = house2
        self.house3 = house3
        self.house4 = house4
        self.hotel = hotel
        self.mortgage = mortgage
        self.house_level = DEFAULT_HOUSE_LEVEL

    def rent(self):
        if self.house_level == 0:
            return self.get_rent()
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

    def get_name(self):
        return self.name

    def get_rent(self):
        return self.rent

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

    def get_mortgage(self):
        return self.mortgage

