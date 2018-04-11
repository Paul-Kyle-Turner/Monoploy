
from Card import Collect, Pay, Goto, GotoJail, Get_Out_Of_Jail, Collectmultiple, PayRepairs, GotoPassGo
from Card import GotoNearestUtility, GotoNearestRailroad, GoBackThree, PayMultiple
import random


class Deck:

    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards = cards


class CommunityChest(Deck):

    def __init__(self):
        self.cards = self.create_community_chest_cards()

    @staticmethod
    def create_community_chest_cards():
        card01 = Goto(description="Advance to Go", position=0)
        card02 = Collect(description="Bank error in your favor", collect_amount=200)
        card03 = Pay(description="Doctor's fees – Pay $50", pay_amount=50)
        card04 = Collect(description="From sale of stock you get $50", collect_amount=50)
        card05 = Get_Out_Of_Jail(description="Get Out of Jail Free")
        card06 = GotoJail(description="Go to Jail", position=11)
        card07 = Collectmultiple(description="Grand Opera Night - Collect $50 "
                                             "from every player for opening night seats", collect_amount=50)
        card08 = Collect(description="Holiday Fund matures - Receive $100 ", collect_amount=100)
        card09 = Collect(description="Income tax refund – Collect $20", collect_amount=20)
        card10 = Collect(description="It is your birthday - Collect $10", collect_amount=10)
        card11 = Collect(description="Life insurance matures – Collect $100", collect_amount=100)
        card12 = Pay(description="Pay hospital fees of $100", pay_amount=100)
        card13 = Pay(description="Pay school fees of $150", pay_amount=150)
        card14 = Collect(description="Receive $25 consultancy fee", collect_amount=25)
        card15 = PayRepairs(description="You are assessed for street repairs – $40 per house"
                                        " – $115 per hotel ", chance=False)
        card16 = Collect(description="You have won second prize in a beauty contest – Collect $10", collect_amount=10)
        card17 = Collect(description="You inherit $100", collect_amount=100)

        return random.shuffle([card01, card02, card03, card04, card05, card06, card07, card08,
                card09, card10, card11, card12, card13, card14, card15, card16, card17])


class Chance(Deck):

    def __init__(self):
        self.cards = self.create_chance_cards()

    @staticmethod
    def create_chance_cards():
        card01 = Goto(description="Advance to Go", position=0)
        card02 = GotoPassGo(description="Advance to Illinois Ave. - If you pass Go, collect $200", position=25)
        card03 = GotoPassGo(description="Advance to St. Charles Place – If you pass Go, collect $200", position=12)
        card04 = GotoNearestUtility(description="Advance token to nearest Utility."
                                                " If unowned, you may buy it from the Bank."
                                        " If owned, throw dice and pay owner a total ten times the amount shown.")
        card05 = GotoNearestRailroad(description="Advance token to the nearest Railroad")
        card06 = Collect(description="Bank pays you dividend of $50", collect_amount=50)
        card07 = Get_Out_Of_Jail(description="Get out of Jail Free")
        card08 = GoBackThree(description="Go Back 3 Spaces")
        card09 = GotoJail(description="Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200")
        card10 = PayRepairs(description="Make general repairs on all your property – "
                                        "For each house pay $25 – For each hotel $100", chance=True)
        card11 = Pay(description="Pay poor tax of $15 ", pay_amount=15)
        card12 = GotoPassGo(description="Take a trip to Reading Railroad", position=5)
        card13 = Goto(description="Take a walk on the Boardwalk", position=39)
        card14 = PayMultiple(description="You have been elected Chairman of the Board"
                                         " – Pay each player $50", pay_amount=50)
        card15 = Collect(description="Your building {and} loan matures – Collect $150 ", collect_amount=150)
        card16 = Collect(description="You have won a crossword competition - Collect $100", collect_amount=100)

        return random.shuffle([card01, card02, card03, card04, card05, card06, card07, card08,
                               card09, card10, card11, card12, card13, card14, card15, card16])