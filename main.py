# Exportación de archivos '.py'

from deck import Deck
from cards import Cards
from coins import Coins
from player import Player
# -------------------------------   Def Main  -------------------------------- #



# Esta función comienza el juego con 3 jugadores
def Multiplayer3P(J1, J2, J3, JCa):

    # Declaramos la variable turno
    turn = 1

    # Revuelve las cartas
    JCa.Shuff_deck()
    print(JCa.deck)

    # Los jugadores quitan las cartas de la baraja
    J1.Get_cards(JCa.deck.pop(0))
    J1.Get_cards(JCa.deck.pop(0))
    J2.Get_cards(JCa.deck.pop(0))
    J2.Get_cards(JCa.deck.pop(0))
    J3.Get_cards(JCa.deck.pop(0))
    J3.Get_cards(JCa.deck.pop(0))

    print(JCa.deck)
    print(J1.Jcards)
    print(J2.Jcards)
    print(J3.Jcards)

    J1.Show_coins()
    J2.Show_coins()
    J3.Show_coins()

    while(turn < 4):

        print("\nListo Jugador " + str(turn) + "\n")

        if(turn == J1.id):
            opt = J1.Take_an_action()
        elif(turn == J2.id):
            opt = J2.Take_an_action()
        else:
            opt = J3.Take_an_action()
        
        turn += 1


    return



# Esta función comienza el juego con 4 jugadores
def Multiplayer4P(J1, J2, J3, JCa):

    # Configuramos el jugador 4
    J4 = Player(4, [], 2)

    # Revuelve las cartas
    JCa.Shuff_deck()
    print(JCa.deck)

    # Los jugadores quitan las cartas de la baraja
    J1.Get_cards(JCa.deck.pop(0))
    J1.Get_cards(JCa.deck.pop(0))
    J2.Get_cards(JCa.deck.pop(0))
    J2.Get_cards(JCa.deck.pop(0))
    J3.Get_cards(JCa.deck.pop(0))
    J3.Get_cards(JCa.deck.pop(0))
    J4.Get_cards(JCa.deck.pop(0))
    J4.Get_cards(JCa.deck.pop(0))

    print(JCa.deck)
    print(J1.Jcards)
    print(J2.Jcards)
    print(J3.Jcards)
    print(J4.Jcards)

    J1.See_cards()
    J2.See_cards()
    J3.See_cards()
    J4.See_cards()

    J1.Show_coins()
    J2.Show_coins()
    J3.Show_coins()
    J4.Show_coins()

    return



# Esta función es donde comienza el código main
def SetUp():

    #Presentación del título
    print("\n   ---- COUP ----   \n")

    # Crea J1, J2 y J3 como clase Person
    # id: Identificador de jugador (Ex: id = 1, entonces es Jugador 1) lo usamos para los turnos
    # Jcards: Cartas del jugador, al principio vacio, pero se agregan más adelante
    # Jcoins: Monedas del jugador, se empieza con 2 monedas
    J1 = Player(1, [], 2)
    J2 = Player(2, [], 2)
    J3 = Player(3, [], 2)

    # La baraja con las cartas
    # Existen 15 cartas de personaje, 3 de cada tipo: Duque, Asesino, Capitán, Embajador y Condesa
    deck = ["D", "D", "D", "A", "A", "A", "Ca", "Ca", "Ca", "E", "E", "E", "Co", "Co", "Co"]

    # Crea JCa como clase Deck
    # deck: La baraja guardada
    JCa = Deck(deck)

    # Pide al usuario con cuantos jugadores quiere jugar
    opt = int(input("Seleccione la cantidad de Jugadores para jugar (3 o 4): "))

    # Pide de nuevo si el dato introducido es erroneo
    while opt < 3 or opt > 4:
        print("Solo se puede jugar de 3 a 4 Jugadores, Intente de nuevo")
        opt = int(input("Seleccione la cantidad de Jugadores para jugar (3 o 4): "))

    # Si escogiste 3 jugadores
    if opt == 3:

        # Vamos al modo de 3 jugadores
        Multiplayer3P(J1, J2, J3, JCa)        

    # Si escogiste 4 jugadores
    else:

        # Vamos al modo de 4 jugadores
        Multiplayer4P(J1, J2, J3, JCa)

    return
    # ------------------------------------------------------------------------ #

if __name__ == "__main__":
    SetUp()