
from Space import Space

DEFAULT_CHANCE_DECK = True
DEFAULT_COMMUNITY_CHEST_DECK = False


class Drawspace(Space):

    def __init__(self, name, deck):
        Space.__init__(name=name)
        self.deck = deck

    def draw_card(self):
        if DEFAULT_CHANCE_DECK:



