
# Exportación de archivos '.py'

from deck import Deck
from coins import Coins
from person import Person
# -------------------------------   Def Main  -------------------------------- #



def interface():
    print("Selecciona una opcion:")
    print("1.- ")
    print("2.- ")
    print("3.- ")
    print("4.- ")
    print("5.- Exit")
    return int(input())



# Esta función comienza el juego con 3 jugadores
def Multiplayer3P(J1, J2, J3, JCa):

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

    J1.See_cards()
    J2.See_cards()
    J3.See_cards()

    J1.Show_coins()
    J2.Show_coins()
    J3.Show_coins()

    return



# Esta función comienza el juego con 4 jugadores
def Multiplayer4P(J1, J2, J3, JCa):

    # Configuramos el jugador 4
    J4 = Person(4, [], 2)

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
    J1 = Person(1, [], 2)
    J2 = Person(2, [], 2)
    J3 = Person(3, [], 2)

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
