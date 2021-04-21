#Imprtamos librería random y archivos '.py'
import random as rd
from cards import Cards
from player import Player

# Creamos la clase Game
class Game():

    # Definimos los atributos
    def __init__(self):
        self.deck = []
        self.players = []
        
    # Comienzo del juego
    def begin(self):
        print("\n   ---- COUP ----   \n")
        self.create_deck()
        opt = self.choose_mode()
        if opt == 3:
            self.multiplayer_3P()
        else:
            self.multiplayer_4P()
        return

    # Modo 3 Jugadores
    def multiplayer_3P(self):
        print("Estás en el modo de 3P\n")
        self.give_cards(3)
        self.show_coins(3)
        return

    # Modo 4 Jugadores
    def multiplayer_4P(self):
        print("Estás en el modo de 4P\n")
        self.give_cards(4)
        self.show_coins(4)
        return

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
    
    # Le da a los jugadores las cardas iniciales
    def give_cards(self, players):
        i = 0
        while i < players:
            self.players[i].get_cards(self.deck.pop(0))
            self.players[i].get_cards(self.deck.pop(0))

            # PRUEBA
            print("Jugador " + str(i+1))
            print(self.players[i].Jcards[0].character)
            print(self.players[i].Jcards[1].character)
            i += 1
        return
    
    # Muestra las monedas de los jugadores
    def show_coins(self, players):
        i = 0
        print("")
        while i < players:
            print(" Monedas de Jugador " + str(self.players[i].id) + ": " + str(self.players[i].Jcoins))
            i += 1
        print("")
        return

    #PRUEBA
    def show_deck(self):
        i = 0
        while i < len(self.deck):
            print(" \'" + self.deck[i].character + "\'", end = "")
            i += 1
        print("\n")
        return


coup = Game()
coup.begin()