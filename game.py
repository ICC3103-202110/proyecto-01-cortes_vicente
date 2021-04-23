
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
        self.clear() # Esto es para limpiar la pantalla
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
        self.clear() # Esto es para limpiar la pantalla
        self.give_cards(3)                 # 3)
        turn = 1
        while(turn < 6):
            if turn == self.players[0].id:
                option_chosen = self.player_turn3P(self.players, 1)  # 4)
            elif turn == self.players[1].id:
                option_chosen = self.player_turn3P(self.players, 2)  # 4)
            else:
                option_chosen = self.player_turn3P(self.players, 3)  # 4)
            self.clear() # Esto es para limpiar la pantalla
            turn += 1
        return

    # Modo 4 Jugadores
    def multiplayer_4P(self):
        self.clear() # Esto es para limpiar la pantalla
        self.give_cards(4)                 # 3)
        turn = 1
        while(turn < 5):
            if turn == self.players[0].id:
                option_chosen = self.player_turn4P(self.players, 1)  # 4)
            elif turn == self.players[1].id:
                option_chosen = self.player_turn4P(self.players, 2)  # 4)
            elif turn == self.players[2].id:
                option_chosen = self.player_turn4P(self.players, 3)  # 4)
            else:
                option_chosen = self.player_turn4P(self.players, 4)  # 4)
            self.clear() # Esto es para limpiar la pantalla
            turn += 1
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
            self.players.append(Player(1, [], 2))
            self.players.append(Player(2, [], 2))
            self.players.append(Player(3, [], 2))
        else:
            self.players.append(Player(1, [], 2))
            self.players.append(Player(2, [], 2))
            self.players.append(Player(3, [], 2))
            self.players.append(Player(4, [], 2))
        return


# --------------- 3)

    # Le da a los jugadores las cardas iniciales
    def give_cards(self, players):
        i = 0
        while i < players:
            self.players[i].get_cards(self.deck.pop(0))
            self.players[i].get_cards(self.deck.pop(0))

            # PRUEBA
            """
            print("Jugador " + str(i+1))
            print(self.players[i].Jcards[0].character)
            print(self.players[i].Jcards[1].character)
            """
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
                        self.clear() 
                        self.players[i].see_cards()

                    elif(opt == 2):
                        self.clear()
                        self.players[i].see_actions()

                    elif(opt == 3):
                        self.clear()
                        for k in range(len(self.log)):
                            print(self.log[k])
                        exit = input("\nPresiona enter para salir: ")
                        self.clear()

                    elif(opt == 4):
                        self.clear()
                        option_list = ["Ingresos","Ayuda extranjera","Golpe","Impuesto","Asesinato","Cambio","Extorsion"]
                        action_opt = self.players[i].take_an_action()  


                        for j in range(len(option_list)):
                            if(action_opt == j+1):
                                a = ["Turno "+ str(i+1) + ": El jugador " + str(self.players[i].id) + " utiliza la opcion '" + option_list[j]+"'"]
                                self.log.append(a)
                                if option_list[j] == 1:
                                    self.players[i].Get_coin()
                                    
                                    

                        
                        #Desafio del Ataque
                        if action_opt >= 4 and action_opt <= 7:

                            truth = self.challenge3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], action_opt, turn, option_list)
     
                            input("\nPresiona enter para salir: ")

                        #Contracción
                        #if action_opt == 2 or action_opt == 5 or action_opt == 7:

                        #Realiza acción
                        if(action_opt == 1):
                            self.players[i].Get_coin()
                        
                        if(action_opt == 2):
                            self.players[i].Get_coin()
                            self.players[i].Get_coin()
                        
                        if(action_opt == 3):
                            for h in range(7):
                                self.players[i].Lose_coin()
                                # Aqui falta un metodo para que un jugador pierda una carta
                        if(action_opt = 4):
                            self.players[i].Get_coin()
                            self.players[i].Get_coin()
                            self.players[i].Get_coin()
                            
                        if(action_opt = 5):
                            self.players[i].Lose_coin()
                            self.players[i].Lose_coin()
                            self.players[i].Lose_coin()
                            # Aqui falta un metodo para que un jugador pierda una carta
                        #if(action_opt = 6):
                        #if(action_opt = 7):
                            

                    else:
                        print("Solo se puede escoger las cuatro opciones, Intente de nuevo.")
                        self.clear()
        return

    # Esta es la versión para cuatro jugadores
    def player_turn4P(self, players, turn):
        opt = 0
        action_opt = 0
        i = 0
        for i in range(len(self.players)):
            if turn == self.players[i].id:
                while(opt != 3):
                    self.show_coins(self.players)
                    print("\n Es turno del Jugador " + str(self.players[i].id))
                    print(" ¿Que deseas hacer primero? \n")
                    print(" 1) Ver tus cartas.")
                    print(" 2) Ver las acciones de todas las cartas.")
                    print(" 3) Realizar una acción.\n")
                    opt = int(input("Decide (1 a 3): "))
                    if(opt == 1):
                        self.clear() 
                        self.players[i].see_cards()
                    elif(opt == 2):
                        self.clear()
                        self.players[i].see_actions()
                    elif(opt == 3):
                        self.clear()
                        action_opt = self.players[i].take_an_action()
                        if action_opt >= 4 and action_opt <= 7 :
                            option_duel = self.players[i].challenge4P(self.players[(i + 1) % len(self.players)].id, self.players[(i + 2) % len(self.players)].id, self.players[(i + 3) % len(self.players)].id)
                    else:
                        print("Solo se puede escoger las tres opciones, Intente de nuevo.")
                        tm.sleep(2)
                        self.clear()
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
    def challenge3P(self, playerPrincipal, otherPlayer1, otherPlayer2, playerPrincipalAction, turn, option_list):

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
        print("\n")

        if option != 0:

            for k in range(len(self.players)):
                if(self.players[k].id == option):
                    truth = self.true_challenge3P(playerPrincipalAction, self.players[k], playerPrincipal)

        
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


# --------------- PRUEBA

    def show_deck(self):
        i = 0
        while i < len(self.deck):
            print(" \'" + self.deck[i].character + "\'", end = "")
            i += 1
        print("\n")
        return
    
    def clear(self):
        return os.system('clear')

    
# --------------- Comienzo del código
"""
coup = Game()
coup.begin()
print("¡Muchas gracias por jugar!")
"""