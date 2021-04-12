import random as rd

class Cards():
    pass

    # -------------------------------  Builder  ------------------------------ #
    def __init__(self, deck, Jcards):
        self.deck = deck
        self.Jcards = Jcards

    # -------------------------------  Methods  ------------------------------ #
    def Shuff_deck(self):
        rd.shuffle(self.deck)
        return ""

    def Share_cards(self):
        self.Jcards.append(self.deck[0])
        self.deck.pop(0)
        self.Jcards.append(self.deck[0])
        self.deck.pop(0)
        return ""
   

# ---------------------------------------------------------------------------- #