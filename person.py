# Definimos la clase Persona para almacenar las cartas de los jugadores

class Person():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, id, Jcards, Jcoins):
        self.__id = id   # id (int)
        self.__Jcards = Jcards   # Jcards (list)
        self.__coins = Jcoins # Jcoins (int)

    # ---------------------------  Private methods  -------------------------- #    

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def Jcards(self):
        return self.__Jcards

    @Jcards.setter
    def Jcards(self, Jcards):
        self.__Jcards = Jcards

    @property
    def Jcoins(self):
        return self.__Jcoins

    @Jcoins.setter
    def Jcoins(self, Jcoins):
        self.__Jcoins = Jcoins
    
    # ---------------------------  Public methods  -------------------------- #      

    def Get_cards(self, card):
        self.__Jcards.append(card)
        return

    def See_cards(self):
        i = 1
        print("\n Cartas del Jugador " + str(self.__id) + ":\n")
        for card in self.__Jcards:
            if(card == "D"):
                print(str(i) + ") Duque")
                print(" - Impuesto: Puedes tomar 3 monedas.")
                print(" - Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
            elif(card == "A"):
                print(str(i) + ") Asesino")
                print(" - Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
                print(" - Contraataque: Ninguna.")
            elif(card == "Ca"):
                print(str(i) + ") Capitán")
                print(" - Extorsión: Puedes tomar 2 monedas a otro jugador.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            elif(card == "E"):
                print(str(i) + ") Embajador")
                print(" - Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            else:
                print(str(i) + ") Condesa")
                print(" - Acción: Ninguna.")
                print(" - Contrataque: Puedes bloquear \'Asesinato\'.")
            print("\n")
            i += 1
        
        return


# J1 = Person(1, ["D", "Ca"], 2)
# J1.See_cards()
