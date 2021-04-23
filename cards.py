
# --------------- Creación de clase Cards

class Cards():

# -------------------- Atributos --------------------

    def __init__(self, character):
        self.character = character   # character (str)


# -------------------- Autoreferencial --------------------

    def character(self):
        return self.character


# -------------------- Funciones --------------------

    def action(self):
        if self.character == "A":
            print("Tu tarjeta es Asesino")
        #if self.character
        return
    

# --------------- PRUEBA

#carta = Cards("A")
#carta.action()