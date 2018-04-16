
class Color:

    def __init__(self, color):
        self.color = color
        self.color_set = []

    def get_color(self):
        return self.color

    def get_color_set(self):
        return self.color_set

    def set_color_set(self, color_set):
        self.color_set = color_set

    def add_property_to_color_set(self, property):
        self.color_set.append(property)
