
# Definimos la clase Cartas para almacenar las cartas de los jugadores

class Cards():

    # -------------------------------  Builder  ------------------------------ #
    
    # Entrada:
    def __init__(self, character):
        self.character = character   # character (str)

    # ---------------------------  Private methods  -------------------------- #  

    def character(self):
        return self.character


    # ---------------------------  Public methods  --------------------------- #

    def action(self):
        if self.character == "A":
            print("Tu tarjeta es Asesino")
        return
    

# ---------------------------------------------------------------------------- #

#carta = Cards("A")
#carta.action()