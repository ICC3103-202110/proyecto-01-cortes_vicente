class Coins():

    # -------------------------------  Builder  ------------------------------ #
    def __init__(self, Jcoins):
        self.__Jcoins = int(Jcoins)

    # ---------------------------  Private methods  -------------------------- #    
    @property
    def Jcoins(self):
        return self.__Jcoins

    @Jcoins.setter
    def Jcoins(self, Jcoins):
        self.__Jcoins = Jcoins

    # ---------------------------  Public methods  --------------------------- #  
    def Award_coin(self):
        self.Jcoins = self.Jcoins+1
        return ""

    def Remove_coin(self):
        self.Jcoins -=1
        return ""

Jcoins = 0
Jco = Coins(Jcoins)
Jco.Award_coin()
print(Jcoins)