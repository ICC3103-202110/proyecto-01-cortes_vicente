
<<<<<<< HEAD
# --------------- Creación de clase Cards

class Cards():

# -------------------- Atributos --------------------

    def __init__(self, character):
        self.character = character   # character (str)


# -------------------- Autoreferencial --------------------

    def character(self):
        return self.character

=======
# Definimos la clase Cartas para almacenar las cartas de los jugadores

class Cards():

    # -------------------------------  Builder  ------------------------------ #
    
    # Entrada:
    def __init__(self, character):
        self.character = character   # character (str)

    # ---------------------------  Private methods  -------------------------- #  

    def character(self):
        return self.character

>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585

# -------------------- Funciones --------------------

    def action(self):
        if self.character == "A":
            print("Tu tarjeta es Asesino")
        return
    

<<<<<<< HEAD
# --------------- PRUEBA
=======
# ---------------------------------------------------------------------------- #
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585

#carta = Cards("A")
#carta.action()