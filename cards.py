# Importa librería random

import random as rd

# Definimos la clase Cartas para almacenar las cartas de los jugadores

class Cards():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, deck):
        self.__deck = deck   # deck (list)

    # ---------------------------  Private methods  -------------------------- #  
    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, deck):
        self.__deck = deck

    # ---------------------------  Public methods  --------------------------- #

    # Revolver la baraja
    def Shuff_deck(self):
        rd.shuffle(self.__deck)
        return

    # Da la carta de la baraja a un jugador
    def Take_card(self):
        cardChosen = self.__deck.pop(0)
        return cardChosen

# ---------------------------------------------------------------------------- #