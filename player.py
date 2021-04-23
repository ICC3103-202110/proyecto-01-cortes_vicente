#Imprtamos archivo '.py'

import time as tm
import os

from cards import Cards

# --------------- Creación de clase Player

class Player():

# -------------------- Atributos --------------------

    def __init__(self, id, Jcards, Jcoins, stillPlaying):
        self.__id = id   # id (int)
        self.__Jcards = Jcards # Jcards (list)
        self.__Jcoins = Jcoins #Jcoins (int)
        self.__stillPlaying = stillPlaying # 1 si sigue jugando, 0 si pierden


# -------------------- Autoreferencial -------------------- 

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
    
    @property
    def stillPlaying(self):
        return self.__stillPlaying

    @stillPlaying.setter
    def stillPlaying(self, stillPlaying):
        self.__stillPlaying = stillPlaying

    
# -------------------- Funciones --------------------    

    # Esta función agrega la carta y lo guarda en Jcards
    def get_cards(self, card):
        self.__Jcards.append(card)
        return

    def remove_influence(self):
        LoseCard = int(input("Elige cual de tus cartas quieres eliminar: "))
        self.Jcards.pop(LoseCard)
        return 
    def Coup_to(self):
        Jcoup = int(input("Jugador " + str(self.id) + " elige a que jugador dirijes la accion 'Golpe': "))
        return Jcoup

    def Get_coin(self):
        self.Jcoins += 1
        return


    def Lose_coin(self):
        self.Jcoins -= 1

     #Esta función muestra tus monedas
    def show_coins(self):
        print(" Monedas de Jugador " + str(self.__id) + ": " + str(self.__Jcoins))
        return

    # Esta función mostrará tus cartas y su información
    def see_cards(self):
        print("\n Cartas del Jugador " + str(self.__id) + ":\n")
        for i in range(len(self.__Jcards)):
            if(self.__Jcards[i].character == "D"):
                print(str(i + 1) + ") Duque")
                print(" - Impuesto: Puedes tomar 3 monedas.")
                print(" - Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
            elif(self.__Jcards[i].character == "A"):
                print(str(i + 1) + ") Asesino")
                print(" - Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
                print(" - Contraataque: Ninguna.")
            elif(self.__Jcards[i].character == "Ca"):
                print(str(i + 1) + ") Capitán")
                print(" - Extorsión: Puedes tomar 2 monedas a otro jugador.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            elif(self.__Jcards[i].character == "E"):
                print(str(i + 1) + ") Embajador")
                print(" - Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            else:
                print(str(i + 1) + ") Condesa")
                print(" - Acción: Ninguna.")
                print(" - Contrataque: Puedes bloquear \'Asesinato\'.")
            print("\n")
        input("\nPresiona enter para salir: ")
        return


    def see_actions(self):
        print("Las acciones que tiene cada carta son: ")
        print("\n Duque: ")
        print("1.- Impuesto: Puedes tomar 3 monedas.")
        print("2.- Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
        print("\n Asesino: ")
        print("1.- Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print("2.- Contraataque: Ninguna.")
        print("\n Capitan: ")
        print("1.- Extorsión: Puedes tomar 2 monedas a otro jugador.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print("\n Embajador: ")
        print("1.- Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print("2.- Contrataque: Puedes bloquear \'Extorsión\'.")
        print("\n Condesa: ")
        print("1.- Acción: Ninguna.")
        print("2.- Contrataque: Puedes bloquear \'Asesinato\'.")
        exit = input("\nPresiona enter para salir: ")
        return



    # Esta función podrás escoger que acción haras
    def take_an_action(self):

        print("\n Acciones: \n")
        print(" 1) Ingresos: Obtienes una moneda.")
        print(" 2) Ayuda Extranjera: Obtienes dos monedas.")
        print(" 3) Golpe: Paga siete monedas, y escoge la carta de un enemigo para eliminarla.")
        print(" 4) Impuesto (Duque): Puedes tomar 3 monedas.")
        print(" 5) Asesinato (Asesino): Puedes pagar 3 monedas para quitar la carta de un jugador.")
        print(" 6) Cambio (Embajador): Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
        print(" 7) Extorsión (Capitán): Puedes tomar 2 monedas a otro jugador.\n")

        option = int(input("Escoge que acción tomarás (1 a 7): "))

        while(option < 1 or option > 7):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge que acción tomarás (1 a 7): "))

        print("Escogiste la opción ", end = "")
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
  

    def challenge4P(self, id1, id2, id3):

        print("\n¿Algún jugador quiere desafiar su acción?\n")
        print(" 1) Jugador " + str(id1) + ".")
        print(" 2) Jugador " + str(id2) + ".")
        print(" 3) Jugador " + str(id3) + ".")
        print(" 4) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        if(option < 1 or option > 4):
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 4): "))
        
        if(option == 1):
            print("Jugador " + str(id1) + " te desafiará!")
        elif(option == 2):
            print("Jugador " + str(id2) + " te desafiará!")
        elif(option == 3):
            print("Jugador " + str(id3) + " te desafiará!") 
        else:
            print("Nadie te ha desafiado")
        return option

