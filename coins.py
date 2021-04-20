# Importa la clase cards
from cards import Cards

# Definimos la clase Coins para almacenar las monedas
# Heredamos Cards unicamente para usarlo luego en la clase Person, ya que 
# heredaremos Coins en Person y asi nos ahorraremos codigo usando POO
class Coins(Cards):

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, Jcoins):
        super().__init__(deck, Jcards = [])
        self.__Jcoins = Jcoins #Jcoins (int)

    # ---------------------------  Private methods  -------------------------- #    
    @property
    def Jcoins(self):
        return self.__Jcoins

    @Jcoins.setter
    def Jcoins(self, Jcoins):
        self.__Jcoins = Jcoins

    # ---------------------------  Public methods  --------------------------- #  

    # Sumar una moneda
    def Award_coin(self):
        self.Jcoins.append("o")
        return ""

    # Quitar una moneda
    def Remove_coin(self):
        self.Jcoins.pop()
        return ""

# Prueba

# Jcoins = 0
# Jco = Coins(Jcoins)
# Jco.Award_coin()
# print(Jcoins)