
# --------------- Creación de clase Cards

class Cards():

# -------------------- Atributos --------------------

    def __init__(self, character):
        self.character = character   # character (str)


# -------------------- Autoreferencial --------------------

    def character(self):
        return self.character

