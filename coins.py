# Definimos la clase Coins para almacenar las monedas

class Coins():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, Jcoins):
        self.__Jcoins = int(Jcoins)   # Jcoins (int)

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
        self.Jcoins = self.Jcoins+1
        return ""

    # Quitar una moneda
    def Remove_coin(self):
        self.Jcoins -= 1
        return ""

# Prueba

# Jcoins = 0
# Jco = Coins(Jcoins)
# Jco.Award_coin()
# print(Jcoins)