 # Definimos la clase Persona para almacenar las cartas de los jugadores

class Player():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
    def __init__(self, id, Jcards, Jcoins):
        self.__id = id   # id (int)
        self.__Jcards = Jcards # Jcards (list)
        self.__Jcoins = Jcoins #Jcoins (int)

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

    # Esta función agrega la carta y lo guarda en Jcards
    def Get_cards(self, card):
        self.__Jcards.append(card)
        return

    # Esta función mostrará tus cartas y su información
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

    # Esta función podrás escoger que acción haras
    def Take_an_action(self):

        print(" Acciones: \n")
        print(" 1) Ingresos: Obtienes una moneda.")
        print(" 2) Ayuda Extranjera: Obtienes dos monedas.")
        print(" 3) Golpe: Paga siete monedas, y escoge la carta de un enemigo para eliminarla.")
        print(" 4) Impuesto (Duque): Puedes tomar 3 monedas.")
        print(" 5) Asesinato (Asesino): Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print(" 6) Cambio (Embajador): Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print(" 7) Extorsión (Capitán): Puedes tomar 2 monedas a otro jugador.\n")

        option = int(input("Escoge que acción tomarás (1 a 7): "))

        if(option < 1 or option > 7):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge que acción tomarás (1 a 7): "))

        print(" Escogiste la opción ", end = "")
        if(option == 1):
            print("Ingresos.")
        elif(option == 2):
            print("Ayuda Extranjera.")
        elif(option == 3):
            print("Golpe.")
        elif(option == 4):
            print("Impuesto.")
        elif(option == 5):
            print("Asesinato.")
        elif(option == 6):
            print("Cambio.")
        else:
            print("Extorsión.")

        return option
    
    # Esta función verificará si alguien quiere hacer un desafio por tu acción
    def Challenge3P(self, id1, id2):

        print("¿Algún jugador quiere desafiar su acción?\n")
        print(" 1) Jugador " + str(id1) + ".")
        print(" 2) Jugador " + str(id2) + ".")
        print(" 3) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        if(option < 1 or option > 3):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 3): "))
        
        if(option == 1):
            print("Jugador " + str(id1) + " te desafiará!")
        elif(option == 2):
            print("Jugador " + str(id2) + " te desafiará!")
        elif(option == 3):
            print("Jugador " + str(id3) + " te desafiará!")
        else:
            print("Nadie te ha desafiado")
        return

    def Challenge4P(self, id1, id2, id3):

        print("¿Algún jugador quiere desafiar su acción?\n")
        print(" 1) Jugador " + str(id1) + ".")
        print(" 2) Jugador " + str(id2) + ".")
        print(" 3) Jugador " + str(id3) + ".")
        print(" 4) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        if(option < 1 or option > 4):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 3): "))
        
        if(option == 1):
            print("Jugador " + str(id1) + " te desafiará!")
        elif(option == 2):
            print("Jugador " + str(id2) + " te desafiará!")
        else:
            print("Nadie te ha desafiado")
        return

        return
    
    #Esta función muestra tus monedas
    def Show_coins(self):
        print(" Monedas de Jugador " + str(self.__id) + ": " + str(self.__Jcoins))
        return


J1 = Player(1, ["D", "Ca"], 2)
print(J1.Jcards)