
#Imprtamos librerías y archivos '.py'

import random as rd
import time as tm
import os
  
from cards import Cards
from player import Player


# --------------- Creación de clase Game

class Game():

# -------------------- Atributos --------------------

    def __init__(self):
        self.deck = []
        self.players = []
        self.log = []


# -------------------- Recorrido del código --------------------


    # Comienzo del juego
    def begin(self):
        print("\n   ---- COUP ----   \n")
        self.create_deck()                 # 1)
        opt = self.choose_mode()           # 2)
        if opt == 3:
            print("\nEscogiste el modo de 3 Jugadores\n\n")
            self.multiplayer_3P()
        else:
            print("\nEscogiste el modo de 4 Jugadores\n\n")
            self.multiplayer_4P()
        return

    # Modo 3 Jugadores
    def multiplayer_3P(self):
        self.give_cards(3)                 # 3)
        turn = 1
        gameplay = 3
        while(gameplay > 1):
            if (turn % 3) == self.players[0].id:
                option_chosen = self.player_turn3P(self.players, 1)  # 4)
            elif (turn % 3) == self.players[1].id:
                option_chosen = self.player_turn3P(self.players, 2)  # 4)
            else:
                option_chosen = self.player_turn3P(self.players, 3)  # 4)
            turn += 1

            gameplay = 0
            for i in range(3):
                if(self.players[i].stillPlaying == 1):
                    gameplay += 1
        return

    # Modo 4 Jugadores
    def multiplayer_4P(self):
        self.give_cards(4)                 # 3)
        turn = 1
        gameplay = 4
        while(gameplay > 1):
            if (turn % 4) == self.players[0].id:
                option_chosen = self.player_turn4P(self.players, 1)  # 4)
            elif (turn % 4) == self.players[1].id:
                option_chosen = self.player_turn4P(self.players, 2)  # 4)
            elif (turn % 4) == self.players[2].id:
                option_chosen = self.player_turn4P(self.players, 3)  # 4)
            else:
                option_chosen = self.player_turn4P(self.players, 4)  # 4)
            turn += 1

            gameplay = 0
            for i in range(4):
                if(self.players[i].stillPlaying == 1):
                    gameplay += 1

        return


# -------------------- Funciones --------------------


# --------------- 1)

    # Crea la baraja de cartas
    def create_deck(self):
        i = 0
        while i < 3:
            self.deck.append(Cards("D"))
            self.deck.append(Cards("A"))
            self.deck.append(Cards("E"))
            self.deck.append(Cards("Ca"))
            self.deck.append(Cards("Co"))
            i += 1
        self.suffle_deck()
        return
    
    # Revuelve la baraja de cartas
    def suffle_deck(self):
        rd.shuffle(self.deck)
        return


# --------------- 2)

    # Escoge el modo del juego
    def choose_mode(self):
        opt = int(input("Seleccione la cantidad de Jugadores para jugar (3 o 4): "))
        while opt < 3 or opt > 4:
            print("Solo se puede jugar de 3 a 4 Jugadores, Intente de nuevo")
            opt = int(input("Seleccione la cantidad de Jugadores para jugar (3 o 4): "))
        self.create_players(opt)
        return opt

    # Crea a los jugadores
    def create_players(self, opt):
        if opt == 3:
            self.players.append(Player(1, [], 2, 1))
            self.players.append(Player(2, [], 2, 1))
            self.players.append(Player(3, [], 2, 1))
        else:
            self.players.append(Player(1, [], 2, 1))
            self.players.append(Player(2, [], 2, 1))
            self.players.append(Player(3, [], 2, 1))
            self.players.append(Player(4, [], 2, 1))
        return


# --------------- 3)

    # Le da a los jugadores las cardas iniciales
    def give_cards(self, players):
        i = 0
        while i < players:
            self.players[i].get_cards(self.deck.pop(0))
            self.players[i].get_cards(self.deck.pop(0))
            i += 1
        return


# --------------- 4)

    # Esta es la función principal del turno del jugador, podrá escoger entre ver sus cartas
    # las acciones de los personajes y tomar una acción
    def player_turn3P(self, players, turn):
        opt = 0
        action_opt = 0
        i = 0
        for i in range(len(self.players)):

            if turn == self.players[i].id:
                if(self.players[i].stillPlaying == 1):

                    while(opt != 4):

                        self.show_coins(self.players)

                        print("\n Es turno del Jugador " + str(self.players[i].id))
                        print(" ¿Que deseas hacer primero? \n")
                        print(" 1) Ver tus cartas.")
                        print(" 2) Ver las acciones de todas las cartas.")
                        print(" 3) Ver historial de jugadas.")
                        print(" 4) Realizar una acción.\n")

                        opt = int(input("Decide (1 a 4): "))

                        if(opt == 1):
                            self.players[i].see_cards()

                        elif(opt == 2):
                            self.players[i].see_actions()

                        elif(opt == 3):
                            for k in range(len(self.log)):
                                print(self.log[k])
                            exit = input("\nPresiona enter para salir: ")

                        elif(opt == 4):
                            option_list = ["Ingresos","Ayuda extranjera","Golpe","Impuesto","Asesinato","Cambio","Extorsion"]
                            action_opt = self.players[i].take_an_action()  

                             
                            for j in range(len(option_list)):
                                if(action_opt == j+1):
                                    a = ["Turno "+ str(i+1) + ": El jugador " + str(self.players[i].id) + " utiliza la opcion '" + option_list[j]+"'"]
                                    self.log.append(a)
                                    if option_list[j] == 1:
                                        self.players[i].Get_coin()
                            
                            truth1 = 0
                            truth2 = 0

                            #Desafio del Ataque
                            if action_opt >= 4 and action_opt <= 7:

                                truth1 = self.challenge3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], action_opt, turn, option_list, False)
        
                                input("\nPresiona enter para salir: ")

                            #Contracción
                            if action_opt == 2 or action_opt == 5 or action_opt == 7:

                                contra = self.contraction3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], action_opt, turn, option_list)

                                input("\nPresiona enter para salir: ")

                            #Desafío de la Contraacción
                                for k in range(len(self.players)):
                                    if(self.players[k].id == contra):
                                        truth2 = self.challenge3P(self.players[k], self.players[(k + 1) % len(self.players)], self.players[(k + 2) % len(self.players)], action_opt, turn, option_list, True)
                                        input("\nPresiona enter para salir: ")
                                        if(truth2 == 0):
                                            contra = 0

                            #Realiza acción
                            if(action_opt == 1):
                                self.players[i].Get_coin()
                            
                            if(action_opt == 2):
                                if(truth2 == 0):
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                            
                            if(action_opt == 3):
                                if(self.players[i].Jcoins < 7):
                                    print("No puedes realizar esta opción.\n")
                                else:
                                    for h in range(7):
                                        self.players[i].Lose_coin()
                                
                                CoupTo = self.players[i].Coup_to()
                                if CoupTo != self.players[i].id:
                                    #print("Jugador" + self.players[CoupTo].id + " ")
                                    self.players[CoupTo].remove_influence()
            
                                
                                    # Aqui falta un metodo para que un jugador pierda una carta
                            if(action_opt == 4):
                                if(truth1 == 1):
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                                
                            if(action_opt == 5):
                                self.players[i].Lose_coin()
                                self.players[i].Lose_coin()
                                self.players[i].Lose_coin()
                                # Aqui falta un metodo para que un jugador pierda una carta

                            if(action_opt == 6):
                                if(truth1 == 1):
                                    self.players[i] = self.changeCards(self.players[i])


                            #if(action_opt = 7):
                                

                        else:
                            print("Solo se puede escoger las cuatro opciones, Intente de nuevo.")
        return

    # Esta es la versión para cuatro jugadores
    def player_turn4P(self, players, turn):
        opt = 0
        action_opt = 0
        i = 0
        for i in range(len(self.players)):
            if turn == self.players[i].id:
                if(self.players[i].stillPlaying == 1):

                    while(opt != 4):

                        self.show_coins(self.players)

                        print("\n Es turno del Jugador " + str(self.players[i].id))
                        print(" ¿Que deseas hacer primero? \n")
                        print(" 1) Ver tus cartas.")
                        print(" 2) Ver las acciones de todas las cartas.")
                        print(" 3) Ver historial de jugadas.")
                        print(" 4) Realizar una acción.\n")

                        opt = int(input("Decide (1 a 4): "))

                        if(opt == 1):
                            self.players[i].see_cards()

                        elif(opt == 2):
                            self.players[i].see_actions()
                        
                        elif(opt == 3):
                            for k in range(len(self.log)):
                                print(self.log[k])
                            exit = input("\nPresiona enter para salir: ")

                        elif(opt == 4):
                            
                            option_list = ["Ingresos","Ayuda extranjera","Golpe","Impuesto","Asesinato","Cambio","Extorsion"]
                            action_opt = self.players[i].take_an_action()  


                            for j in range(len(option_list)):
                                if(action_opt == j+1):
                                    a = ["Turno "+ str(i+1) + ": El jugador " + str(self.players[i].id) + " utiliza la opcion '" + option_list[j]+"'"]
                                    self.log.append(a)
                                    if option_list[j] == 1:
                                        self.players[i].Get_coin()
                            
                            truth1 = 0
                            truth2 = 0

                            #Desafio del Ataque
                            if action_opt >= 4 and action_opt <= 7:

                                truth1 = self.challenge4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], self.players[(i + 3) % len(self.players)], action_opt, turn, option_list, False)
        
                                input("\nPresiona enter para salir: ")

                            #Contracción
                            if action_opt == 2 or action_opt == 5 or action_opt == 7:

                                contra = self.contraction4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)],  self.players[(i + 3) % len(self.players)], action_opt, turn, option_list)

                                input("\nPresiona enter para salir: ")

                            #Desafío de la Contraacción
                                for k in range(len(self.players)):
                                    if(self.players[k].id == contra):
                                        truth2 = self.challenge4P(self.players[k], self.players[(k + 1) % len(self.players)], self.players[(k + 2) % len(self.players)], self.players[(i + 3) % len(self.players)], action_opt, turn, option_list, True)
                                        input("\nPresiona enter para salir: ")

                            #Realiza acción
                            if(action_opt == 1):
                                self.players[i].Get_coin()
                            
                            if(action_opt == 2):
                                if(truth2 == 0):
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                            
                            if(action_opt == 3):
                                if(self.players[i].Jcoins < 7):
                                    print("No puedes realizar esta opción.\n")
                                else:
                                    for h in range(7):
                                        self.players[i].Lose_coin()
                                
                                CoupTo = self.players[i].Coup_to()
                                if CoupTo != self.players[i].id:
                                    #print("Jugador" + self.players[CoupTo].id + " ")
                                    self.players[CoupTo].remove_influence()
            
                                
                                    # Aqui falta un metodo para que un jugador pierda una carta
                            if(action_opt == 4):
                                if(truth1 == 1):
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                                    self.players[i].Get_coin()
                                
                            if(action_opt == 5):
                                self.players[i].Lose_coin()
                                self.players[i].Lose_coin()
                                self.players[i].Lose_coin()
                                # Aqui falta un metodo para que un jugador pierda una carta

                            if(action_opt == 6):
                                if(truth1 == 1):
                                    self.players[i] = self.changeCards(self.players[i])


                            #if(action_opt = 7):
                             
                        else:
                            print("Solo se puede escoger las cuatro opciones, Intente de nuevo.")
        return

    # Muestra las moneds de todos los jugadores
    def show_coins(self, players):
        i = 0
        print("")
        while i < len(self.players):
            print(" Monedas de Jugador " + str(self.players[i].id) + ": " + str(self.players[i].Jcoins))
            i += 1
        print("")
        return


# --------------- 5)

# Esta función verificará si alguien quiere hacer un desafio por tu acción
    def challenge3P(self, playerPrincipal, otherPlayer1, otherPlayer2, playerPrincipalAction, turn, option_list, contraction):

        truth = 0

        print("\n¿Algún jugador quiere desafiar su acción?\n")
        print(" 1) Jugador " + str(otherPlayer1.id) + ".")
        print(" 2) Jugador " + str(otherPlayer2.id) + ".")
        print(" 3) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        while option < 1 or option > 3:
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 3): "))
        
        if(option == 1):
            print("Jugador " + str(otherPlayer1.id) + " te desafiará!")
            option = otherPlayer1.id
        elif(option == 2):
            print("Jugador " + str(otherPlayer2.id) + " te desafiará!")
            option = otherPlayer2.id
        else:
            print("Nadie te ha desafiado")
            option = 0
            print("truth = " + str(1))
            return 1
        print("\n")

        if option != 0:

            for k in range(len(self.players)):
                if(self.players[k].id == option):
                    if contraction == False:
                        truth = self.true_challenge3P(playerPrincipalAction, self.players[k], playerPrincipal)
                    else:
                        truth = self.true_challengeContra3P(playerPrincipalAction, self.players[k], playerPrincipal)
        
                    a = ["Turno "+ str(turn) + ": El jugador " + str(self.players[k].id) + " desafia la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                    self.log.append(a)
        
        print("truth = " + str(truth))
        return truth
    
    def challenge4P(self, playerPrincipal, otherPlayer1, otherPlayer2, otherPlayer3, playerPrincipalAction, turn, option_list, contraction):

        truth = 0

        print("\n¿Algún jugador quiere desafiar su acción?\n")
        print(" 1) Jugador " + str(otherPlayer1.id) + ".")
        print(" 2) Jugador " + str(otherPlayer2.id) + ".")
        print(" 3) Jugador " + str(otherPlayer3.id) + ".")
        print(" 4) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 4): "))

        while option < 1 or option > 4:
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 4): "))
        
        if(option == 1):
            print("Jugador " + str(otherPlayer1.id) + " te desafiará!")
            option = otherPlayer1.id
        elif(option == 2):
            print("Jugador " + str(otherPlayer2.id) + " te desafiará!")
            option = otherPlayer2.id
        elif(option == 3):
            print("Jugador " + str(otherPlayer3.id) + " te desafiará!")
            option = otherPlayer3.id
        else:
            print("Nadie te ha desafiado")
            option = 0
            print("truth = " + str(1))
            return 1
        print("\n")

        if option != 0:

            for k in range(len(self.players)):
                if(self.players[k].id == option):
                    if contraction == False:
                        truth = self.true_challenge4P(playerPrincipalAction, self.players[k], playerPrincipal)
                    else:
                        truth = self.true_challengeContra4P(playerPrincipalAction, self.players[k], playerPrincipal)
        
                    a = ["Turno "+ str(turn) + ": El jugador " + str(self.players[k].id) + " desafia la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                    self.log.append(a)
        
        print("truth = " + str(truth))
        return truth
    
    
    def true_challenge3P(self, attack, playerAttack, playerDefense):

        print("El desafio entre el jugador " + str(playerDefense.id) + " y jugador " + str(playerAttack.id) + " comienza!!")
        
        truth = 0
        if(attack == 4): #Impuesto

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "D"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene un Duque.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Duque.\nEl jugador que desafió gana el desafio.")
                return 0

        elif(attack == 5): #Asesinato

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "A"):
                    truth += 1
                    

            if truth > 0:
                print("El jugador defensa tiene un Asesino.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Asesino.\nEl jugador que desafió gana el desafio.")
                return 0

        elif(attack == 6): #Cambio

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "E"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene un Asesino.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Asesino.\nEl jugador que desafió gana el desafio.")
                return 0
                
        else: #Extorsión

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "Ca"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene un Capitán.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Capitán.\nEl jugador que desafió gana el desafio.")
                return 0
                
        return 0


    def contraction3P(self, playerPrincipal, otherPlayer1, otherPlayer2, playerPrincipalAction, turn, optionlist):

        print("\nEsta acción se puede contraatacar!\n¿Alguien que desee contraatacar?")
        print(" 1) Jugador " + str(otherPlayer1.id) + ".")
        print(" 2) Jugador " + str(otherPlayer2.id) + ".")
        print(" 3) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        while option < 1 or option > 3:
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 3): "))
        
        if(option == 1):
            print("Jugador " + str(otherPlayer1.id) + " te contraatacará!")
            option = otherPlayer1.id
        elif(option == 2):
            print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
            option = otherPlayer2.id
        else:
            print("Nadie te ha contraatacado!")
            option = 0
        print("\n")

        if option != 0:
            if(option == 1):
                a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer1.id) + " contraatacará la acción '" + optionlist[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                self.log.append(a)
            else:
                a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer2.id) + " contraatacará la acción '" + optionlist[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                self.log.append(a)

        print("option = " + str(option))
        return option

    
    def contraction4P(self, playerPrincipal, otherPlayer1, otherPlayer2, otherPlayer3, playerPrincipalAction, turn, option_list):

        print("\nEsta acción se puede contraatacar!\n¿Alguien que desee contraatacar?")
        print(" 1) Jugador " + str(otherPlayer1.id) + ".")
        print(" 2) Jugador " + str(otherPlayer2.id) + ".")
        print(" 3) Jugador " + str(otherPlayer3.id) + ".")
        print(" 4) Ninguno.")

        option = int(input("Escoge quien desafiará (1 a 3): "))

        while option < 1 or option > 4:
            print("\nEscoge bien tu opción")
            option = int(input("Escoge quien desafiará (1 a 4): "))
        
        if(option == 1):
            print("Jugador " + str(otherPlayer1.id) + " te contraatacará!")
            option = otherPlayer1.id
        elif(option == 2):
            print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
            option = otherPlayer2.id
        elif(option == 3):
            print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
            option = otherPlayer3.id
        else:
            print("Nadie te ha contraatacado!")
            option = 0
        print("\n")

        if option != 0:
            if(option == 1):
                a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer1.id) + " contraatacará la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                self.log.append(a)
            elif(option == 2):
                a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer2.id) + " contraatacará la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                self.log.append(a)
            else:
                a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer3.id) + " contraatacará la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                self.log.append(a)

        print("option = " + str(option))
        return option


    def true_challengeContra3P(self, attack, playerAttack, playerDefense):

        print("El desafio entre el jugador " + str(playerDefense.id) + " y jugador " + str(playerAttack.id) + " comienza!!")
        
        truth = 0
        if(attack == 2): #Ayuda Extrangera

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "D"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene un Duque.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Duque.\nEl jugador que desafió gana el desafio.")
                return 0

        elif(attack == 5): #Asesinato

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "Co"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene una Condesa.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene una Condesa.\nEl jugador que desafió gana el desafio.")
                return 0
                
        else: #Extorsión

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "Ca" or playerDefense.Jcards[i].character == "E"):
                    truth += 1

            if truth > 0:
                print("El jugador defensa tiene un Capitán o un Embajador.\nEl jugador defensa gana el desafio.")
                return 1
            else:
                print("El jugador defensa no tiene un Capitán o un Embajador.\nEl jugador que desafió gana el desafio.")
                return 0
                
        return 0


    def changeCards(self, player):

        print("\n Escoge una de las dos cartas:\n")
        for i in range(2):
            if(self.deck[i].character == "D"):
                print(str(i + 1) + ") Duque")
                print(" - Impuesto: Puedes tomar 3 monedas.")
                print(" - Contrataque: Puedes bloquear \'Ayuda Extranjera\'.")
            elif(self.deck[i].character == "A"):
                print(str(i + 1) + ") Asesino")
                print(" - Asesinato: Puedes pagar 3 monedas para quitar la carta de un jugador.")
                print(" - Contraataque: Ninguna.")
            elif(self.deck[i].character == "Ca"):
                print(str(i + 1) + ") Capitán")
                print(" - Extorsión: Puedes tomar 2 monedas a otro jugador.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            elif(self.deck[i].character == "E"):
                print(str(i + 1) + ") Embajador")
                print(" - Cambio: Puedes tomar 2 cartas del mazo y escoger cual de ellas reemplazar con una de tus cartas.")
                print(" - Contrataque: Puedes bloquear \'Extorsión\'.")
            else:
                print(str(i + 1) + ") Condesa")
                print(" - Acción: Ninguna.")
                print(" - Contrataque: Puedes bloquear \'Asesinato\'.")
            print("\n")

        cardSelected = int(input("Cual quieres (1 o 2): "))

        cardReplace = int(input("¿Con cual quieres reemplazar? (1 o 2): "))

        cardBackup = player.Jcards[cardReplace-1]
        player.Jcards[cardReplace-1] = self.deck[cardSelected-1]
        self.deck.append(cardBackup)

        return player
