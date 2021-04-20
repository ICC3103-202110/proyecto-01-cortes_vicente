# Definimos la clase Coins para almacenar las monedas
class Coins():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, Jcoins):
        self.__Jcoins = Jcoins   

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