
#Imprtamos librerías y archivos '.py'

import random as rd
  
from cards import Cards
from player import Player
from paper import Paper


# --------------- Creación de clase Game

class Game():


# -------------------- Atributos --------------------

    def __init__(self):
        self.deck = []
        self.players = []
        self.log = []
        self.turn = 1.33 # int


# -------------------- Recorrido del código --------------------


    # Comienzo del juego
    def begin(self):
        print("\n------------------- COUP ----------------------\n")
        print(" ___________________________________________________")
        print("|¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶|")
        print("|¶¶¶        ¶¶¶        ¶¶¶   ¶¶¶¶¶   ¶¶          ¶¶¶|")
        print("|¶¶         ¶¶   ¶¶¶¶   ¶¶   ¶¶¶¶¶   ¶¶   ¶¶¶¶    ¶¶|")
        print("|¶¶    ¶¶¶¶¶¶¶   ¶¶¶¶   ¶¶   ¶¶¶¶¶   ¶¶   ¶¶¶¶    ¶¶|")
        print("|¶¶    ¶¶¶¶¶¶¶   ¶¶¶¶   ¶¶   ¶¶¶¶¶   ¶¶          ¶¶¶|")
        print("|¶¶    ¶¶¶¶¶¶¶   ¶¶¶¶   ¶¶   ¶¶¶¶¶   ¶¶   ¶¶¶¶¶¶¶¶¶¶|")
        print("|¶¶         ¶¶   ¶¶¶¶   ¶¶   ¶¶¶¶¶   ¶¶   ¶¶¶¶¶¶¶¶¶¶|")
        print("|¶¶¶        ¶¶¶        ¶¶¶¶         ¶¶¶   ¶¶¶¶¶¶¶¶¶¶|")
        print("|¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print("\n------------------- COUP ----------------------\n")
        self.create_deck()                 # 1)
        choose_mode = self.choose_mode()   # 2)
        if choose_mode == 3:
            print("\nEscogiste el modo de 3 Jugadores\n\n")
            self.multiplayer_3P()
        else:
            print("\nEscogiste el modo de 4 Jugadores\n\n")
            self.multiplayer_4P()
        print("\n¡MUCHAS GRACIAS POR JUGAR!\n")
        return

    # Modo 3 Jugadores
    def multiplayer_3P(self):
        self.give_cards()                  # 3)
        player_turn = 1
        gameplay = 3
        while(gameplay > 1):
            if (player_turn % 3) == self.players[0].id:
                if self.players[0].stillPlaying == True:
                    self.player_turn3P(self.players[0].id)  # 4)
            elif (player_turn % 3) == self.players[1].id:
                if self.players[1].stillPlaying == True:
                    self.player_turn3P(self.players[1].id)  # 4)
            else:
                if self.players[2].stillPlaying == True:
                    self.player_turn3P(self.players[2].id)  # 4)
            player_turn += 1

            gameplay = 0
            for i in range(len(self.players)):
                if(self.players[i].stillPlaying == True):
                    gameplay += 1
                
        for i in range(len(self.players)):
            if self.players[i].stillPlaying == True:
                print("¡Felicidades Jugador " + str(self.players[i].id) + ", Ganaste el Juego de COUP!\n¡Ahora eres el dueño de todo el estado!\n")
        return

    # Modo 4 Jugadores
    def multiplayer_4P(self):
        self.give_cards()                  # 3)
        player_turn = 1
        gameplay = 4
        while(gameplay > 1):
            if (player_turn % 4) == self.players[0].id:
                if self.players[0].stillPlaying == True:
                    option_chosen = self.player_turn4P(self.players[0].id)  # 4)
            elif (player_turn % 4) == self.players[1].id:
                if self.players[1].stillPlaying == True:
                    option_chosen = self.player_turn4P(self.players[1].id)  # 4)
            elif (player_turn % 4) == self.players[2].id:
                if self.players[2].stillPlaying == True:
                    option_chosen = self.player_turn4P(self.players[2].id)  # 4)
            else:
                if self.players[3].stillPlaying == True:
                    option_chosen = self.player_turn4P(self.players[3].id)  # 4)
            player_turn += 1

            gameplay = 0
            for i in range(len(self.players)):
                if(self.players[i].stillPlaying == True):
                    gameplay += 1

        for i in range(len(self.players)):
            if self.players[i].stillPlaying == True:
                print("¡Felicidades Jugador " + str(self.players[i].id) + ", Ganaste el Juego de COUP!\n¡Ahora eres el dueño de todo el estado!\n")

        return


# -------------------- Funciones --------------------


# --------------- 1)

    # Crea la baraja de cartas
    def create_deck(self):
        i = 0
        while i < 3:
            self.deck.append(Cards("D", True))
            self.deck.append(Cards("A", True))
            self.deck.append(Cards("E", True))
            self.deck.append(Cards("Ca", True))
            self.deck.append(Cards("Co", True))
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
            self.players.append(Player(1, [], 2, True))
            self.players.append(Player(2, [], 2, True))
            self.players.append(Player(3, [], 2, True))
        else:
            self.players.append(Player(1, [], 2, True))
            self.players.append(Player(2, [], 2, True))
            self.players.append(Player(3, [], 2, True))
            self.players.append(Player(4, [], 2, True))
        return


# --------------- 3)

    # Le da a los jugadores las cardas iniciales
    def give_cards(self):
        i = 0
        while i < len(self.players):
            self.players[i].get_cards(self.deck.pop(0))
            self.players[i].get_cards(self.deck.pop(0))
            i += 1
        return


# --------------- 4)

    # Esta es la función principal del turno del jugador, podrá escoger entre ver sus cartas
    # las acciones de los personajes y tomar una acción
    def player_turn3P(self, player_id):
        opt = 0
        action_opt = 0
        i = 0

        for i in range(len(self.players)):
            if player_id == self.players[i].id:
                if(self.players[i].stillPlaying == True):

                    while(opt != 4):

                        self.show_coins()
                        self.show_cards()

                        print(" Es turno del Jugador " + str(self.players[i].id))
                        print(" ¿Que deseas hacer primero? \n")
                        print(" 1) Ver tus cartas.")
                        print(" 2) Ver las acciones de todas las cartas.")
                        print(" 3) Ver historial de jugadas.")
                        print(" 4) Realizar una acción.\n")

                        opt = int(input("Decide (1 a 4): "))

                        if(opt == 1):
                            self.players[i].see_cards()
                            input("\nPresiona enter para salir: ")

                        elif(opt == 2):
                            self.players[i].see_actions()
                            input("\nPresiona enter para salir: ")

                        elif(opt == 3):
                            for k in range(len(self.log)):
                                print(self.log[k])
                            exit = input("\nPresiona enter para salir: ")

                        elif(opt == 4):
                            option_list = ["Ingresos", "Ayuda Extranjera", "Golpe", "Impuesto", "Asesinato", "Cambio","Extorsión"]

                            if(self.players[i].Jcoins >= 10):
                                print("Tienes 10 monedas o más, tienes que hacer un Golpe.\n")
                                action_opt = 3
                            else:
                                action_opt = self.players[i].take_an_action()
                                while((action_opt == 3 and self.players[i].Jcoins < 7) or (action_opt == 5 and self.players[i].Jcoins < 3)):
                                    print("No puedes realizar la acción Golpe o Asesinato, porque tienes menos de las monedas requeridas para hacer la acción.\n")
                                    action_opt = self.players[i].take_an_action()

                            #for j in range(len(option_list)):
                                #if(action_opt == j+1):
                                    #objt = Paper(self.players[i].id, "", "", option_list[j])
                                    #objt.Write(option_list[j],turn)
                                    #objt.Show_writings()
                                    #a = ["Turno "+ str(i+1) + ": El jugador " + str(self.players[i].id) + " utiliza la opcion '" + option_list[j]+"'"]
                                    #self.log.append(a)
                            
                            truth1 = False
                            truth2 = False

                            #Desafio del Ataque
                            if action_opt >= 4 and action_opt <= 7:

                                truth1 = self.challenge3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], action_opt, player_id, option_list, False)
        
                                input("Presiona enter para salir: ")

                            #Contracción
                            if action_opt == 2 or action_opt == 5 or action_opt == 7:

                                contra = self.contraction3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], action_opt, player_id, option_list)

                            #Desafío de la Contraacción
                                for k in range(len(self.players)):
                                    if(self.players[k].id == contra):
                                        truth2 = self.challenge3P(self.players[k], self.players[(k + 1) % len(self.players)], self.players[(k + 2) % len(self.players)], action_opt, player_id, option_list, True)
                                        
                                input("Presiona enter para salir: ")

                            #Realiza acción
                            if(action_opt == 1): #LISTO
                                self.players[i].get_coin()
                            
                            elif(action_opt == 2): #LISTO
                                if(truth2 == False):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                            
                            elif(action_opt == 3): #LISTO
                                if(self.players[i].Jcoins < 7):
                                    print("No puedes realizar esta opción.\n")
                                else:
                                    for j in range(7):
                                        self.players[i].lose_coin
                                    self.coup_to_3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)])

                            elif(action_opt == 4): #LISTO
                                if(truth1 == True):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                
                            elif(action_opt == 5): #LISTO
                                if(truth1 == True):
                                    self.players[i].lose_coin()
                                    self.players[i].lose_coin()
                                    self.players[i].lose_coin()
                                    if(truth2 == False):
                                        self.coup_to_3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)])

                            elif(action_opt == 6): #LISTO
                                if(truth1 == True):
                                    self.change_cards(self.players[i])

                            elif(action_opt == 7): #LISTO
                                if(truth1 == True and truth2 == False):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                    self.extorsion_3P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)])
                                
                        else:
                            print("Solo se puede escoger las cuatro opciones, Intente de nuevo.")
        return

    # Esta es la versión para cuatro jugadores
    def player_turn4P(self, player_id):
        opt = 0
        action_opt = 0
        i = 0

        for i in range(len(self.players)):
            if player_id == self.players[i].id:
                if(self.players[i].stillPlaying == True):

                    while(opt != 4):

                        self.show_coins()
                        self.show_cards()

                        print(" Es turno del Jugador " + str(self.players[i].id))
                        print(" ¿Que deseas hacer primero? \n")
                        print(" 1) Ver tus cartas.")
                        print(" 2) Ver las acciones de todas las cartas.")
                        print(" 3) Ver historial de jugadas.")
                        print(" 4) Realizar una acción.\n")

                        opt = int(input("Decide (1 a 4): "))

                        if(opt == 1):
                            self.players[i].see_cards()
                            input("\nPresiona enter para salir: ")

                        elif(opt == 2):
                            self.players[i].see_actions()
                            input("\nPresiona enter para salir: ")

                        elif(opt == 3):
                            for k in range(len(self.log)):
                                print(self.log[k])
                            exit = input("\nPresiona enter para salir: ")

                        elif(opt == 4):
                            option_list = ["Ingresos", "Ayuda Extranjera", "Golpe", "Impuesto", "Asesinato", "Cambio","Extorsión"]

                            if(self.players[i].Jcoins >= 10):
                                print("Tienes 10 monedas o más, tienes que hacer un Golpe.\n")
                                action_opt = 3
                            else:
                                action_opt = self.players[i].take_an_action()
                                while((action_opt == 3 and self.players[i].Jcoins < 7) or (action_opt == 5 and self.players[i].Jcoins < 3)):
                                    print("No puedes realizar la acción Golpe o Asesinato, porque tienes menos de las monedas requeridas para hacer la acción.\n")
                                    action_opt = self.players[i].take_an_action()

                            """
                            for j in range(len(option_list)):
                                if(action_opt == j + 1):
                                    a = ["Turno "+ str(i+1) + ": El jugador " + str(self.players[i].id) + " utiliza la opcion '" + option_list[j]+"'"]
                                    self.log.append(a)
                                    if option_list[j] == 1:
                                        self.players[i].get_coin()
                            """
                            
                            truth1 = False
                            truth2 = False

                            #Desafio del Ataque
                            if action_opt >= 4 and action_opt <= 7:

                                truth1 = self.challenge4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], self.players[(i + 3) % len(self.players)], action_opt, player_id, option_list, False)
        
                                input("Presiona enter para salir: ")

                            #Contracción
                            if action_opt == 2 or action_opt == 5 or action_opt == 7:

                                contra = self.contraction4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)],  self.players[(i + 3) % len(self.players)], action_opt, player_id, option_list)

                                

                            #Desafío de la Contraacción
                                for k in range(len(self.players)):
                                    if(self.players[k].id == contra):
                                        truth2 = self.challenge4P(self.players[k], self.players[(k + 1) % len(self.players)], self.players[(k + 2) % len(self.players)], self.players[(k + 3) % len(self.players)], action_opt, player_id, option_list, True)

                                input("Presiona enter para salir: ")

                            #Realiza acción
                            if(action_opt == 1): #LISTO
                                self.players[i].get_coin()
                            
                            elif(action_opt == 2): #LISTO
                                if(truth2 == False):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                            
                            elif(action_opt == 3): #LISTO
                                if(self.players[i].Jcoins < 7):
                                    print("No puedes realizar esta opción.\n")
                                else:
                                    for j in range(7):
                                        self.players[i].lose_coin
                                    self.coup_to_4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], self.players[(i + 3) % len(self.players)])
            
                            elif(action_opt == 4): #LISTO
                                if(truth1 == True):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                
                            elif(action_opt == 5): #LISTO
                                if(truth1 == True):
                                    self.players[i].lose_coin()
                                    self.players[i].lose_coin()
                                    self.players[i].lose_coin()
                                    if(truth2 == False):
                                        self.coup_to_4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], self.players[(i + 3) % len(self.players)])

                            elif(action_opt == 6): #LISTO
                                if(truth1 == True):
                                    self.change_cards(self.players[i])

                            elif(action_opt == 7): #LISTO
                                if(truth1 == True and truth2 == False):
                                    self.players[i].get_coin()
                                    self.players[i].get_coin()
                                    self.extorsion_4P(self.players[i], self.players[(i + 1) % len(self.players)], self.players[(i + 2) % len(self.players)], self.players[(i + 3) % len(self.players)])
                             
                        else:
                            print("Solo se puede escoger las cuatro opciones, Intente de nuevo.")
        return

    # Muestra las monedas de todos los jugadores
    def show_coins(self):
        print("\n Monedas de los Jugadores:\n")
        for i in range(len(self.players)):
            print(" Monedas de Jugador " + str(self.players[i].id) + ": " + str(self.players[i].Jcoins))
        print("")
        return

    # Muestra las cartas de los jugadores, si ya son usadas, se muestran
    def show_cards(self):
        print("\n Cartas de los Jugadores:\n")
        for i in range(len(self.players)):
            print(" Cartas de Jugador " + str(self.players[i].id) + ": ") 
            for j in range(len(self.players[i].Jcards)):
                if(self.players[i].Jcards[j].playable == True):
                    print(" " + str(j + 1) + ") Carta Jugable")
                else:
                    if(self.players[i].Jcards[j].character == "D"):
                        print(" " + str(j + 1) + ") Duque")
                    elif(self.players[i].Jcards[j].character == "A"):
                        print(" " + str(j + 1) + ") Asesino")
                    elif(self.players[i].Jcards[j].character == "Ca"):
                        print(" " + str(j + 1) + ") Capitán")
                    elif(self.players[i].Jcards[j].character == "E"):
                        print(" " + str(j + 1) + ") Embajador")
                    else:
                        print(" " + str(j + 1) + ") Condesa")
            print("")
        print("")

        return

    def coup_to_3P(self, player, otherPlayer1, otherPlayer2):

        print("\n ----- Eliminación de influencia -----\n")
        how_many_playing = 0

        if otherPlayer1.stillPlaying == True:
            print(" 1) Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True:
            print(" 2) Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1

        if how_many_playing >= 2:
            Jcoup = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o 2): "))
            while(Jcoup < 1 or Jcoup > 2):
                print("Escoge bien tu opción")
                Jcoup = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o 2): "))
        
            if Jcoup == 1:
                otherPlayer1.remove_influence()
            else:
                otherPlayer2.remove_influence()
        
        else:
            if otherPlayer1.stillPlaying == True:
                otherPlayer1.remove_influence()
            if otherPlayer2.stillPlaying == True:
                otherPlayer2.remove_influence()

        return

    def extorsion_3P(self, player, otherPlayer1, otherPlayer2):
    
        print("\n ----- Extorsión -----\n")
        how_many_playing = 0

        if otherPlayer1.stillPlaying == True:
            print(" 1) Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True:
            print(" 2) Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1

        if how_many_playing >= 2:
            extor = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o 2): "))
            while(extor < 1 or extor > 2):
                print("Escoge bien tu opción")
                extor = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o 2): "))
        
            if extor == 1:
                otherPlayer1.lose_coin()
                otherPlayer1.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
            else:
                otherPlayer2.lose_coin()
                otherPlayer2.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")
            
        else:
            if otherPlayer1.stillPlaying == True:
                otherPlayer1.lose_coin()
                otherPlayer1.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
            if otherPlayer2.stillPlaying == True:
                otherPlayer2.lose_coin()
                otherPlayer2.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")
        
        return

    def coup_to_4P(self, player, otherPlayer1, otherPlayer2, otherPlayer3):

        print("\n ----- Eliminación de influencia -----\n")
        how_many_playing = 0

        if otherPlayer1.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        if otherPlayer3.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer3.id) + ".")
            how_many_playing += 1

        if how_many_playing >= 2:
            Jcoup = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o " + str(how_many_playing) + "): "))
            while(Jcoup < 1 or Jcoup > how_many_playing):
                print("Escoge bien tu opción")
                Jcoup = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o " + str(how_many_playing) + "): "))
        
            if how_many_playing == 3:
                if Jcoup == 1:
                    otherPlayer1.remove_influence()
                elif Jcoup == 2:
                    otherPlayer2.remove_influence()
                else:
                    otherPlayer2.remove_influence()
            
            else:
                if otherPlayer1.stillPlaying == False:
                    if Jcoup == 1:
                        otherPlayer2.remove_influence()
                    else:
                        otherPlayer3.remove_influence()

                if otherPlayer2.stillPlaying == False:
                    if Jcoup == 1:
                        otherPlayer1.remove_influence()
                    else:
                        otherPlayer3.remove_influence()
                
                if otherPlayer3.stillPlaying == False:
                    if Jcoup == 1:
                        otherPlayer1.remove_influence()
                    else:
                        otherPlayer2.remove_influence()

        else:
            if otherPlayer1.stillPlaying == True:
                otherPlayer1.remove_influence()

            if otherPlayer2.stillPlaying == True:
                otherPlayer2.remove_influence()

            if otherPlayer3.stillPlaying == True:
                otherPlayer1.remove_influence()

        return

    def extorsion_4P(self, player, otherPlayer1, otherPlayer2, otherPlayer3):
    
        print("\n ----- Extorsión -----\n")
        how_many_playing = 0

        if otherPlayer1.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        if otherPlayer3.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer3.id) + ".")
            how_many_playing += 1
        
        if how_many_playing >= 2:
            extor = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o " + str(how_many_playing) + "): "))
            while(extor < 1 or extor > how_many_playing):
                print("Escoge bien tu opción")
                extor = int(input("\nJugador " + str(player.id) + ", elige a cuál Jugador quieres remover su infuencia (1 o " + str(how_many_playing) + "): "))
        
            if extor == 1:
                otherPlayer1.lose_coin()
                otherPlayer1.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
            else:
                otherPlayer2.lose_coin()
                otherPlayer2.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")

            if how_many_playing == 3:
                if extor == 1:
                    otherPlayer1.lose_coin()
                    otherPlayer1.lose_coin()
                    print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
                elif extor == 2:
                    otherPlayer2.lose_coin()
                    otherPlayer2.lose_coin()
                    print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")
                else:
                    otherPlayer3.lose_coin()
                    otherPlayer3.lose_coin()
                    print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer3.id) + ".")
            
            else:
                if otherPlayer1.stillPlaying == False:
                    if extor == 1:
                        otherPlayer2.lose_coin()
                        otherPlayer2.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")
                    else:
                        otherPlayer3.lose_coin()
                        otherPlayer3.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer3.id) + ".")

                if otherPlayer2.stillPlaying == False:
                    if Jcoup == 1:
                        otherPlayer1.lose_coin()
                        otherPlayer1.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
                    else:
                        otherPlayer3.lose_coin()
                        otherPlayer3.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer3.id) + ".")
                
                if otherPlayer3.stillPlaying == False:
                    if Jcoup == 1:
                        otherPlayer1.lose_coin()
                        otherPlayer1.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
                    else:
                        otherPlayer2.lose_coin()
                        otherPlayer2.lose_coin()
                        print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer2.id) + ".")
            
        else:
            if otherPlayer1.stillPlaying == True:
                otherPlayer1.lose_coin()
                otherPlayer1.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
            if otherPlayer2.stillPlaying == True:
                otherPlayer2.lose_coin()
                otherPlayer2.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer1.id) + ".")
            if otherPlayer3.stillPlaying == True:
                otherPlayer3.lose_coin()
                otherPlayer3.lose_coin()
                print("\nEl Jugador " + str(player.id) + " extorsionó al Jugador " + str(otherPlayer3.id) + ".")
        
        return
# --------------- 5)

# Esta función verificará si alguien quiere hacer un desafio por tu acción
    def challenge3P(self, playerPrincipal, otherPlayer1, otherPlayer2, playerPrincipalAction, turn, option_list, is_contraction):

        how_many_playing = 0
        truth = False

        print("\n¿Algún Jugador quiere desafiar su acción?\n")

        if otherPlayer1.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True: 
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        print(" " + str(how_many_playing + 1) + ") Ninguno.\n")

        if how_many_playing >= 2:
            option = int(input("Escoge quien desafiará (1 a 3): "))
            while option < 1 or option > 3:
                print("\nEscoge bien tu opción")
                option = int(input("Escoge quien desafiará (1 a 3): "))

            if is_contraction == False:
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                    truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                    playerAttackid = otherPlayer1.id
                elif(option == 2):
                    print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                    truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                    playerAttackid = otherPlayer2.id
                else:
                    print("Nadie te ha desafiado.")
                    return True
            else:
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                    truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                    playerAttackid = otherPlayer1.id
                elif(option == 2):
                    print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                    truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                    playerAttackid = otherPlayer2.id
                else:
                    print("Nadie te ha desafiado.")
                    return True
        
        else:
            if otherPlayer1.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))

                if is_contraction == False:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                
                    else:
                        print("No has desafiado.")
                        return True

                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                
                    else:
                        print("No has desafiado.")
                        return True
            
            if otherPlayer2.stillPlaying == True:
                option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if is_contraction == False:

                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                
                    else:
                        print("No has desafiado.")
                        return True

                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                    
                    else:
                        print("No has desafiado.")
                        return True
        
        a = ["Turno "+ str(turn) + ": El Jugador " + str(playerAttackid) + " desafia la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el Jugador "+ str(playerPrincipal.id) + "."]
        self.log.append(a)

        print("\n")

        return truth

    
    def true_challenge(self, playerAttack, playerDefense, playerDefenseAction):

        print("\n ----- DESAFÍO -----\n\n¡¡El desafio entre el Jugador " + str(playerDefense.id) + " y el Jugador " + str(playerAttack.id) + " comienza!!")
        truth = 0

        if(playerDefenseAction == 4): #Impuesto

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "D" and playerDefense.Jcards[i].playable == True):
                    truth += 1
                    character = playerDefense.Jcards[i].character

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Duque.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "D")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Duque.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False

        elif(playerDefenseAction == 5): #Asesinato

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "A" and playerDefense.Jcards[i].playable == True):
                    truth += 1
                    character = playerDefense.Jcards[i].character

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Asesino.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "A")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Asesino.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False

        elif(playerDefenseAction == 6): #Cambio

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "E" and playerDefense.Jcards[i].playable == True):
                    truth += 1
                    character = playerDefense.Jcards[i].character

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Embajador.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "E")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Embajador.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False
                
        else: #Extorsión

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "Ca" and playerDefense.Jcards[i].playable == True):
                    truth += 1
                    character = playerDefense.Jcards[i].character

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Capitán.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "Ca")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Capitán.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False
                
        return False


    def change_card(self, player, character):
        for i in range(len(player.Jcards)):
            if(player.Jcards[i].character == character):
                print("El Jugador " + str(player.id) + " tendrá que cambiar su carta por una del mazo.")
                cardBackup = player.Jcards.pop(i)
                player.get_cards(self.deck.pop(0))
                self.deck.append(cardBackup)
                return
        return
    

    def contraction3P(self, playerPrincipal, otherPlayer1, otherPlayer2, playerPrincipalAction, turn, option_list):

        how_many_playing = 0
        option = 0

        print("\nEsta acción se puede contraatacar!\n¿Alguien que desea contraatacar?")

        if otherPlayer1.stillPlaying == True:
            print(" 1) Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True: 
            print(" 2) Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        print(" 3) Ninguno.\n")

        if how_many_playing >= 2:
            option = int(input("Escoge quien contraatacará (1 a 3): "))
            while option < 1 or option > 3:
                print("\nEscoge bien tu opción")
                option = int(input("Escoge quien contraatacará (1 a 3): "))
            
            if(option == 1):
                print("¡El Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                option = otherPlayer1.id
            elif(option == 2):
                print("¡El Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                option = otherPlayer2.id
            else:
                print("Nadie te ha contraatacado!")
                option = 0
            print("\n")

            if option != 0:
                if(option == 1):
                    a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer1.id) + " contraatacará la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                    self.log.append(a)
                else:
                    a = ["Turno "+ str(turn) + ": El jugador " + str(otherPlayer2.id) + " contraatacará la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el jugador "+ str(playerPrincipal.id)]
                    self.log.append(a)

        else:
            if otherPlayer1.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres contraatacar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                    option = otherPlayer1.id
                
                else:
                    print("No has desafiado.")
                    option = 0



            if otherPlayer2.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres contraatacar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                    option = otherPlayer2.id
                
                else:
                    print("No has desafiado.")
                    option = 0

        return option


    def true_challenge_contra(self, playerAttack, playerDefense, playerDefenseAction):
        
        print("\n ----- DESAFÍO DE CONTRA -----\n\n¡¡El desafio entre el Jugador " + str(playerDefense.id) + " y el Jugador " + str(playerAttack.id) + " comienza!!")
        truth = 0

        if(playerDefenseAction == 2): #Ayuda Extrangera

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "D" and playerDefense.Jcards[i].playable == True):
                    truth += 1

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Duque.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "D")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Duque.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False

        elif(playerDefenseAction == 5): #Asesinato

            for i in range(len(playerDefense.Jcards)):
                if(playerDefense.Jcards[i].character == "Co" and playerDefense.Jcards[i].playable == True):
                    truth += 1

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene una Condesa.\nEl Jugador " + str(playerAttack.id) + " pierde el desafio.")
                self.change_card(playerDefense, "Co")
                playerAttack.remove_influence()
                return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene una Condesa.\nEl Jugador " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False
                
        else: #Extorsión

            for i in range(len(playerDefense.Jcards)):
                if((playerDefense.Jcards[i].character == "Ca" and playerDefense.Jcards[i].playable == True) or (playerDefense.Jcards[i].character == "E" and playerDefense.Jcards[i].playable == True)):
                    truth += 1

            if truth > 0:
                print("El Jugador " + str(playerDefense.id) + " tiene un Capitán o un Embajador.\nEl jugador " + str(playerAttack.id) + " pierde el desafio.")
                for i in range(len(playerDefense.Jcards)):
                    if(playerDefense.Jcards[i].character == "Ca"):
                        self.change_card(playerDefense, "Ca")
                        playerAttack.remove_influence()
                        return True
                    else:
                        self.change_card(playerDefense, "E")
                        playerAttack.remove_influence()
                        return True
            else:
                print("El Jugador " + str(playerDefense.id) + " no tiene un Capitán o un Embajador.\nEl jugador que " + str(playerAttack.id) + " gana el desafio.")
                playerDefense.remove_influence()
                return False
                
        return False


    def challenge4P(self, playerPrincipal, otherPlayer1, otherPlayer2, otherPlayer3, playerPrincipalAction, turn, option_list, is_contraction):

        how_many_playing = 0
        truth = False

        print("\n¿Algún jugador quiere desafiar su acción?\n")

        if otherPlayer1.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True: 
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        if otherPlayer3.stillPlaying == True: 
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer3.id) + ".")
            how_many_playing += 1
        print(" " + str(how_many_playing + 1) + ") Ninguno.")

        if how_many_playing >= 2:
            option = int(input("Escoge quien desafiará (1 a " + str(how_many_playing + 1) + "): "))
            while option < 1 or option > (how_many_playing + 1):
                print("\nEscoge bien tu opción")
                option = int(input("Escoge quien desafiará (1 a " + str(how_many_playing + 1) + "): "))

            if how_many_playing == 3:
                if is_contraction == False:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                    elif(option == 2):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                    elif(option == 3):
                        print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer3, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer3.id
                    else:
                        print("Nadie te ha desafiado.")
                        return True
                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                    elif(option == 2):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                    elif(option == 3):
                        print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer3, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer3.id
                    else:
                        print("Nadie te ha desafiado.")
                        return True

            if how_many_playing == 2:
                if is_contraction == False:
                    if otherPlayer1.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer2.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer3, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer3.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True
                    
                    if otherPlayer2.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer1.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer3, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer3.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True
                    
                    if otherPlayer3.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer1.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                            truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer2.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True
                        
                else:
                    if otherPlayer1.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer2.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer3, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer3.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True
                    
                    if otherPlayer2.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer1.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer3, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer3.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True
                    
                    if otherPlayer3.stillPlaying == False:
                        if(option == 1):
                            print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer1.id
                        elif(option == 2):
                            print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                            truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                            playerAttackid = otherPlayer2.id
                        else:
                            print("Nadie te ha desafiado.")
                            return True

        else:
            if otherPlayer1.stillPlaying == True:
                option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))

                if is_contraction == False:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                
                    else:
                        print("No has desafiado.")
                        return True

                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer1.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer1, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer1.id
                
                    else:
                        print("No has desafiado.")
                        return True
            
            if otherPlayer2.stillPlaying == True:
                option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if is_contraction == False:

                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                
                    else:
                        print("No has desafiado.")
                        return True

                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer2.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer2, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer2.id
                    
                    else:
                        print("No has desafiado.")
                        return True

            if otherPlayer3.stillPlaying == True:
                option = int(input("Jugador " + str(otherPlayer3.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer3.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if is_contraction == False:

                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                        truth = self.true_challenge(otherPlayer3, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer3.id
                
                    else:
                        print("No has desafiado.")
                        return True

                else:
                    if(option == 1):
                        print("¡El Jugador " + str(otherPlayer3.id) + " te desafiará!")
                        truth = self.true_challenge_contra(otherPlayer3, playerPrincipal, playerPrincipalAction)
                        playerAttackid = otherPlayer3.id
                    
                    else:
                        print("No has desafiado.")
                        return True
        
        a = ["Turno "+ str(turn) + ": El Jugador " + str(playerAttackid) + " desafia la acción '" + option_list[playerPrincipalAction-1]+"' hecha por el Jugador "+ str(playerPrincipal.id) + "."]
        self.log.append(a)

        print("\n")

        return truth
    
    
    def contraction4P(self, playerPrincipal, otherPlayer1, otherPlayer2, otherPlayer3, playerPrincipalAction, turn, option_list):

        how_many_playing = 0
        option = 0

        print("\nEsta acción se puede contraatacar!\n¿Alguien que desea contraatacar?")

        if otherPlayer1.stillPlaying == True:
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer1.id) + ".")
            how_many_playing += 1
        if otherPlayer2.stillPlaying == True: 
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer2.id) + ".")
            how_many_playing += 1
        if otherPlayer3.stillPlaying == True: 
            print(" " + str(how_many_playing + 1) + ") Jugador " + str(otherPlayer3.id) + ".")
            how_many_playing += 1
        print(" " + str(how_many_playing + 1) + ") Ninguno.")

        if how_many_playing >= 2:
            option = int(input("Escoge quien contraatacará (1 a " + str(how_many_playing + 1) + "): "))
            while option < 1 or option > (how_many_playing + 1):
                print("\nEscoge bien tu opción")
                option = int(input("Escoge quien contraatacará (1 a " + str(how_many_playing + 1) + "): "))

            if how_many_playing == 3:
                if(option == 1):
                    print("Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                    option = otherPlayer1.id
                elif(option == 2):
                    print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                    option = otherPlayer2.id
                elif(option == 3):
                    print("Jugador " + str(otherPlayer3.id) + " te contraatacará!")
                    option = otherPlayer3.id
                else:
                    print("Nadie te ha contraatacado!")
                    option = 0
            
            else:
                if otherPlayer1.stillPlaying == False:
                    if(option == 1):
                        print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                        option = otherPlayer2.id
                    elif(option == 2):
                        print("Jugador " + str(otherPlayer3.id) + " te contraatacará!")
                        option = otherPlayer3.id
                    else:
                        print("Nadie te ha contraatacado!")
                        option = 0
                
                if otherPlayer2.stillPlaying == False:
                    if(option == 1):
                        print("Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                        option = otherPlayer1.id
                    elif(option == 2):
                        print("Jugador " + str(otherPlayer3.id) + " te contraatacará!")
                        option = otherPlayer3.id
                    else:
                        print("Nadie te ha contraatacado!")
                        option = 0
                
                if otherPlayer3.stillPlaying == False:
                    if(option == 1):
                        print("Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                        option = otherPlayer1.id
                    elif(option == 2):
                        print("Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                        option = otherPlayer2.id
                    else:
                        print("Nadie te ha contraatacado!")
                        option = 0

        else:
            if otherPlayer1.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres contraatacar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer1.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer1.id) + " te contraatacará!")
                    option = otherPlayer1.id
                
                else:
                    print("No has desafiado.")
                    option = 0

            if otherPlayer2.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres contraatacar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer2.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer2.id) + " te contraatacará!")
                    option = otherPlayer2.id
                
                else:
                    print("No has desafiado.")
                    option = 0
            
            if otherPlayer3.stillPlaying == True:

                option = int(input("Jugador " + str(otherPlayer3.id) + ", ¿Quieres contraatacar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                while option < 0 or option > 1:
                    print("\nEscoge bien tu opción")
                    option = int(input("Jugador " + str(otherPlayer3.id) + ", ¿Quieres desafiar a Jugador " + str(playerPrincipal.id) + "? (1 para si, 0 para no)"))
                
                if(option == 1):
                    print("¡El Jugador " + str(otherPlayer3.id) + " te contraatacará!")
                    option = otherPlayer3.id
                
                else:
                    print("No has desafiado.")
                    option = 0

        return option


    def change_cards(self, player):

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
        while cardSelected < 1 or cardSelected > 2:
            print("\nEscoge bien tu opción")
            cardSelected = int(input("Cual quieres (1 o 2): "))

        how_many_cards = 0
        for i in range(len(player.Jcards)):
            if player.Jcards[i].playable == True:
                how_many_cards += 1

        if how_many_cards >= 2:
            print("\n Estas son tus cartas:\n")
            player.see_cards()

            cardReplace = int(input("¿Con cual quieres reemplazar? (1 o 2): "))
            while cardReplace < 1 or cardReplace > 2:
                print("\nEscoge bien tu opción")
                cardReplace = int(input("¿Con cual quieres reemplazar? (1 o 2): "))
            
            print("\n Reemplazaste la carta " + player.Jcards[cardReplace - 1].characterComplete() + " por la carta " + self.deck[cardSelected - 1].characterComplete())
            cardBackup = player.Jcards[cardReplace - 1]
            player.Jcards[cardReplace - 1] = self.deck[cardSelected - 1]
            self.deck[cardSelected - 1] = cardBackup
            self.suffle_deck()
        
        else:
            for i in range(len(player.Jcards)):
                if player.Jcards[i].playable == True:
                    print("\n Tu carta es " + player.Jcards[i].characterComplete + "\n")
                    print("\n Reemplazaste la carta " + player.Jcards[i].characterComplete() + " por la carta " + self.deck[cardSelected - 1].characterComplete())
                    cardBackup = player.Jcards[cardReplace - 1]
                    player.Jcards[cardReplace - 1] = self.deck[cardSelected - 1]
                    self.deck[cardSelected - 1] = cardBackup
                    self.suffle_deck()
                    
        return

