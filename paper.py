class Paper():
    def __init__(self, id, contra_id, log, action):
        self.id = id # Int
        self.contra_id = contra_id
        self.log = [["Historial de jugadas: "]] # list
        self.action = action # string

    def Write(self, action, turn):
        self.log.append("Turno " + str(turn) +" El jugador " + str(self.id) + "realizo la accion '" + action + "'")
        return

    def Show_writings(self):
        print(self.log)
        return


