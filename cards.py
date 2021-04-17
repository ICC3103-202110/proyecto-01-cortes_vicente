import random as rd

class Cards():

    # -------------------------------  Builder  ------------------------------ #
    def __init__(self, deck, Jcards):
        self.__deck = deck
        self.__Jcards = Jcards

    # ---------------------------  Private methods  -------------------------- #  
    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, deck):
        self.__deck = deck
    
    @property
    def Jcards(self):
        return self.__Jcards

    @Jcards.setter
    def Jcards(self, Jcards):
        self.__Jcards = Jcards

    # ---------------------------  Public methods  --------------------------- #
    def Shuff_deck(self):
        rd.shuffle(self.deck)
        return ""

    def Share_card(self):
        self.Jcards.append(self.deck[0])
        self.deck.pop(0)
        return ""

    def Show_hand(self):
        print(self.Jcards)
        return ""

# ---------------------------------------------------------------------------- #