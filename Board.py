import Property

class Board:

    def __init__(self):
        self.houses = 32
        self.hotels = 12
        self.chance = self.create_chance()
        self.community_chest = self.create_community_chest()
        self.properties = self.create_properties()

    def create_properties(self):
        self.properties = []

    def create_chance(self):
        return []