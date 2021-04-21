<<<<<<< HEAD
#Imprtamos archivo '.py'

from cards import Cards

# --------------- Creación de clase Player

class Player():

# -------------------- Atributos --------------------

=======
 # Definimos la clase Persona para almacenar las cartas de los jugadores

class Player():

    # -------------------------------  Builder  ------------------------------ #

    # Entrada:
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
    def __init__(self, id, Jcards, Jcoins):
        self.__id = id   # id (int)
        self.__Jcards = Jcards # Jcards (list)
        self.__Jcoins = Jcoins #Jcoins (int)

<<<<<<< HEAD

# -------------------- Autoreferencial -------------------- 
=======
    # ---------------------------  Private methods  -------------------------- #    
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585

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
    
<<<<<<< HEAD
# -------------------- Funciones --------------------    
=======
    # ---------------------------  Public methods  -------------------------- #      
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585

    # Esta función agrega la carta y lo guarda en Jcards
    def get_cards(self, card):
        self.__Jcards.append(card)
        return

    def Get_coin(self):
<<<<<<< HEAD
        self.Jcoins += 1
        return

    def Lose_coin(self):
        self.Jcoins -= 1

    # Esta función mostrará tus cartas y su información
    def see_cards(self):
=======
        self.Jcoin += 1
        return

    def Lose_coin(self):
        self.Jcoin -= 1

    # Esta función mostrará tus cartas y su información
    def See_cards(self):
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        i = 1
        print("\n Cartas del Jugador " + str(self.__id) + ":\n")
        for card in self.__Jcards:
            if(card == "D"):
                print(str(i) + ") Duque")
            elif(card == "A"):
                print(str(i) + ") Asesino")
            elif(card == "Ca"):
                print(str(i) + ") Capitán")
            elif(card == "E"):
                print(str(i) + ") Embajador")
            else:
                print(str(i) + ") Condesa")
            print("\n")
            i += 1

    def see_actions(self):
        print("Las acciones que tiene cada carta son: ")
<<<<<<< HEAD
        print(" Duque: ")
        print("1.- Impuesto: Puedes tomar 3 monedas.")
        print("2.- Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
        print(" Asesino: ")
        print("1.- Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print("2.- Contraataque: Ninguna.")
        print(" Capitan: ")
        print("1.- Extorsión: Puedes tomar 2 monedas a otro jugador.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print(" Embajador: ")
        print("1.- Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print(" Condesa: ")
=======
        print("Duque: ")
        print("1.- Impuesto: Puedes tomar 3 monedas.")
        print("2.- Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
        print("Asesino: ")
        print("1.- Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print("2.- Contraataque: Ninguna.")
        print("Capitan: ")
        print("1.- Extorsión: Puedes tomar 2 monedas a otro jugador.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print("Embajador: ")
        print("1.- Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print("Condesa: ")
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        print("1.- Acción: Ninguna.")
        print("2.- Contrataque: Puedes bloquear \'Asesinato\'.")



    # Esta función podrás escoger que acción haras
<<<<<<< HEAD
    def take_an_action(self):

        print("\n Acciones: \n")
=======
    def Take_an_action(self):

        print(" Acciones: \n")
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        print(" 1) Ingresos: Obtienes una moneda.")
        print(" 2) Ayuda Extranjera: Obtienes dos monedas.")
        print(" 3) Golpe: Paga siete monedas, y escoge la carta de un enemigo para eliminarla.")
        print(" 4) Impuesto (Duque): Puedes tomar 3 monedas.")
        print(" 5) Asesinato (Asesino): Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print(" 6) Cambio (Embajador): Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print(" 7) Extorsión (Capitán): Puedes tomar 2 monedas a otro jugador.\n")

        option = int(input("Escoge que acción tomarás (1 a 7): "))

<<<<<<< HEAD
        while(option < 1 or option > 7):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge que acción tomarás (1 a 7): "))

        print("Escogiste la opción ", end = "")
=======
        if(option < 1 or option > 7):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge que acción tomarás (1 a 7): "))

        print(" Escogiste la opción ", end = "")
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
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
<<<<<<< HEAD
    def challenge3P(self, id1, id2):

        print("\n¿Algún jugador quiere desafiar su acción?\n")
=======
    def Challenge3P(self, id1, id2):

        print("¿Algún jugador quiere desafiar su acción?\n")
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        print(" 1) Jugador " + str(id1) + ".")
        print(" 2) Jugador " + str(id2) + ".")
        print(" 3) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

<<<<<<< HEAD
        while option < 1 or option > 3:
=======
        if(option < 1 or option > 3):
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 3): "))
        
        if(option == 1):
            print("Jugador " + str(id1) + " te desafiará!")
        elif(option == 2):
            print("Jugador " + str(id2) + " te desafiará!")
<<<<<<< HEAD
        else:
            print("Nadie te ha desafiado")
        return option
    
    
    def true_challenge3P(self):
        a = 4
        while a >= 4 and a <= 7:
            if self.take_an_action == 4:
                for i in range(2):
                    if self.Jcards[i] == "D":
                        print("El jugador" + str(self.id) + " tiene la carta")
                        print("El jugador " + str(self.challenge3P) + " pierde una influencia")
                        break
            a += 1
        return ""
    
    


    def challenge4P(self, id1, id2, id3):

        print("\n¿Algún jugador quiere desafiar su acción?\n")
=======
        elif(option == 3):
            print("Jugador " + str(id3) + " te desafiará!")
        else:
            print("Nadie te ha desafiado")
        return

    def Challenge4P(self, id1, id2, id3):

        print("¿Algún jugador quiere desafiar su acción?\n")
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
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
<<<<<<< HEAD
        elif(option == 3):
            print("Jugador " + str(id3) + " te desafiará!")
=======
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        else:
            print("Nadie te ha desafiado")
        return

        return
    
    #Esta función muestra tus monedas
<<<<<<< HEAD
    def show_coins(self):
=======
    def Show_coins(self):
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
        print(" Monedas de Jugador " + str(self.__id) + ": " + str(self.__Jcoins))
        return


<<<<<<< HEAD
# --------------- PRUEBA

=======
>>>>>>> 2ecf601720b4b3196a84859244e9f9a033eee585
#J1 = Player(1, ["D", "Ca"], 2)
#print(J1.Jcards)