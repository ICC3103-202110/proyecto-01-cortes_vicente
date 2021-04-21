
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


# -------------------- Recorrido del código --------------------


    # Comienzo del juego
    def begin(self):
        os.system('clear')
        print("\n   ---- COUP ----   \n")
        self.create_deck()                 # 1)
        opt = self.choose_mode()           # 2)
        if opt == 3:
            print("\nEscogiste el modo de 3 Jugadores\n\nCargando...")
            tm.sleep(2)
            self.multiplayer_3P()
        else:
            print("\nEscogiste el modo de 4 Jugadores\n\nCargando...")
            tm.sleep(2)
            self.multiplayer_4P()
        return

    # Modo 3 Jugadores
    def multiplayer_3P(self):
        os.system('clear')
        self.give_cards(3)                 # 3)
        turn = 1
        while(turn < 4):
            self.show_coins(3)             # 4)
            if turn == self.players[0].id:
                print("\n Es turno del Jugador " + str(self.players[0].id))
                option_chosen = self.players[0].take_an_action()
                option_duel = self.players[0].challenge3P(self.players[1].id, self.players[2].id)
            elif turn == self.players[1].id:
                print("\n Es turno del Jugador " + str(self.players[1].id))
                option_chosen = self.players[1].take_an_action()
                option_duel = self.players[1].challenge3P(self.players[0].id, self.players[2].id)
            else:
                print("\n Es turno del Jugador " + str(self.players[2].id))
                option_chosen = self.players[2].take_an_action()
                option_duel = self.players[2].challenge3P(self.players[0].id, self.players[1].id)
            print("Cargando...")
            tm.sleep(2)
            os.system('clear')
            turn += 1
            
        return

    # Modo 4 Jugadores
    def multiplayer_4P(self):
        os.system('clear')
        self.give_cards(4)                 # 3)
        turn = 1
        while(turn < 5):
            self.show_coins(4)             # 4)
            if turn == self.players[0].id:
                print("Es turno del Jugador " + str(self.players[0].id))
            elif turn == self.players[1].id:
                print("Es turno del Jugador " + str(self.players[1].id))
            elif turn == self.players[2].id:
                print("Es turno del Jugador " + str(self.players[2].id))
            else:
                print("Es turno del Jugador " + str(self.players[3].id))
            tm.sleep(2)
            os.system('clear')
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

    # Muestra las monedas de los jugadores
    def show_coins(self, players):
        i = 0
        print("")
        while i < players:
            print(" Monedas de Jugador " + str(self.players[i].id) + ": " + str(self.players[i].Jcoins))
            i += 1
        print("")
        return


# --------------- PRUEBA

    def show_deck(self):
        i = 0
        while i < len(self.deck):
            print(" \'" + self.deck[i].character + "\'", end = "")
            i += 1
        print("\n")
        return

    


# --------------- Comienzo del código

coup = Game()
coup.begin()
print("¡Muchas gracias por jugar!")