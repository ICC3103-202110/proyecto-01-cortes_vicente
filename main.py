
# Exportación de archivos '.py'

from cards import Cards
from coins import Coins

# -------------------------------   Def Main  -------------------------------- #


def interface():
    print("Selecciona una opcion:")
    print("1.- ")
    print("2.- ")
    print("3.- ")
    print("4.- ")
    print("5.- Exit")
    return int(input())


def Main():

    # Lista de cartas de los jugadores
    J1cards = []
    J2cards = []
    J3cards = []
    J4cards = []

    # Jcards tiene las listas de los jugadores
    Jcards = [J1cards, J2cards, J3cards, J4cards]
    
    # Las monedas de cada jugador
    J1coins = 0
    J2coins = 0
    J3coins = 0
    J4coins = 0

    # La baraja con las cartas
    # Existen 15 cartas de personaje, 3 de cada tipo: Duque, Asesino, Capitán, Embajador y Condesa
    deck = ["D", "D", "D", "A", "A", "A", "Ca", "Ca", "Ca", "E", "E", "E", "Co", "Co", "Co"]

    # Pide al usuario con cuantos jugadores quiere en el juego
    opt = int(input("Ingrese la cantidad de jugadores (3 o 4): "))

    # Pide de nuevo si el dato introducido es erroneo
    while opt < 3 or opt > 4:
        print("Solo se puede de 3 a 4 jugadores, escoge de nuevo")
        opt = int(input("Ingrese la cantidad de jugadores (3 o 4): "))

    # Si escogiste 3 jugadores
    if opt == 3:
        J4 = False
        Jcards.pop(3)

        JCa = Cards(deck, Jcards)
        JCa.Shuff_deck()
        print(deck)

        for i in range(len(Jcards)):
            JCa = Cards(deck, Jcards[i])
            JCa.Share_card()
            JCa.Share_card()

        print(deck)
        print(J1cards)
        print(J2cards)
        print(J3cards)

    # Si escogiste 4 jugadores
    else:
        J4 = True

        JCa = Cards(deck, Jcards)
        JCa.Shuff_deck()
        print(deck)
    
        for i in range(len(Jcards)):
            JCa = Cards(deck, Jcards[i])
            JCa.Share_card()
            JCa.Share_card()

        print(deck)
        print(J1cards)
        print(J2cards)
        print(J3cards)
        print(J4cards)


    # ------------------------   Class Coins objects  ------------------------ #

   # J1Co = Coins(J1coins)
   # J2Co = Coins(J2coins)
   # J3Co = Coins(J3coins)
   # J4Co = Coins(J4coins)
    # ------------------------------------------------------------------------ #

   # J1Ca.Show_hand()
   # J2Ca.Show_hand()
   # J3Ca.Show_hand()
   # J4Ca.Show_hand()

   # J1Co.Award_coin()
   # J1Co.Award_coin()
   # J2Co.Award_coin()
   # J2Co.Award_coin()
   # J3Co.Award_coin()
   # J3Co.Award_coin()
   # J4Co.Award_coin()
   # J4Co.Award_coin()

    #print(J1coins)
    #print(J2coins)
    #print(J3coins)
    #print(J4coins)


    return ""

    # ------------------------------------------------------------------------ #

if __name__ == "__main__":
    Main()
