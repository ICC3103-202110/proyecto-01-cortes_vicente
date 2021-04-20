# Definimos la clase Coins para almacenar las monedas
<<<<<<< HEAD
=======

>>>>>>> 4ba9a316970e7f6a352bc24e31a251b0b2edcd59
class Coins():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, Jcoins):
<<<<<<< HEAD
        self.__Jcoins = Jcoins   
=======
        self.__Jcoins = int(Jcoins)   # Jcoins (int)
>>>>>>> 4ba9a316970e7f6a352bc24e31a251b0b2edcd59

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
<<<<<<< HEAD
        self.Jcoins.pop()
=======
        self.Jcoins -= 1
>>>>>>> 4ba9a316970e7f6a352bc24e31a251b0b2edcd59
        return ""

# Prueba

# Jcoins = 0
# Jco = Coins(Jcoins)
# Jco.Award_coin()
# print(Jcoins)