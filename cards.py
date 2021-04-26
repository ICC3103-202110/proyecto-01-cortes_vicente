## Código creado por Juan Pablo Cortés y Gonzalo Vicente

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

    def characterComplete(self):
        if self.character == "D":
            return "Duque"
        elif self.character == "A":
            return "Asesino"
        elif self.character == "Ca":
            return "Capitán"
        elif self.character == "E":
            return "Embajador"
        else:
            return "Condesa"

