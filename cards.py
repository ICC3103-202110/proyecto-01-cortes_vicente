# Importa la clase deck

from deck import Deck

# Definimos la clase Cartas para almacenar las cartas de los jugadores

class Cards(Deck):

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, Jcards):
        self.__Jcards = Jcards   # Jcards (list)

    # ---------------------------  Private methods  -------------------------- #  
    @property
    def Jcards(self):
        return self.__Jcards

    @Jcards.setter
    def Jcards(self, Jcards):
        self.__Jcards = Jcards
    # ---------------------------  Public methods  --------------------------- #

    # Da la carta de la baraja a un jugador
    

# ---------------------------------------------------------------------------- #