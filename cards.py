# Importa librería random

import random as rd

# Definimos la clase Cartas para almacenar las cartas de los jugadores

class Cards():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, deck, Jcards):
        self.__deck = deck   # deck (list)
        self.__Jcards = Jcards   # Jcards (list)

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

    # Revolver la baraja
    def Shuff_deck(self):
        rd.shuffle(self.deck)
        return ""

    # Da la carta de la baraja a un jugador
    def Share_card(self):
        self.Jcards.append(self.deck[0])
        self.deck.pop(0)
        return ""

    # Muestra las cartas de los jugadores
    def Show_hand(self):
        print(self.Jcards)
        return ""

# ---------------------------------------------------------------------------- #