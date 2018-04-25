
# Author Paul Turner

class Color:

    def __init__(self, color):
        self.color = color
        self.color_set = []

    def has_property(self, space):
        for spacet in self.color_set:
            if spacet == space:
                return True
        return False

    def get_property(self, num):
        return self.color_set[num]

    def get_color(self):
        return self.color

    def get_color_set(self):
        return self.color_set

    def set_color_set(self, color_set):
        self.color_set = color_set

    def add_property_to_color_set(self, property):
        self.color_set.append(property)
