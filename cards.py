
# --------------- Creación de clase Cards

class Cards():

# -------------------- Atributos --------------------

    def __init__(self, character, playable):
        self.character = character    # character (str)
        self.playable = playable    # playable (bool)


# -------------------- Autoreferencial --------------------

    def character(self):
        return self.character
    
    def playable(self):
        return self.playable

