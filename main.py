
# Exportación de archivos '.py'

from cards import Cards
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


def Main():
    
    # Configuramos a los jugadores
    J1 = Person(1, [], 2)
    J2 = Person(2, [], 2)
    J3 = Person(3, [], 2)
    J4 = Person(4, [], 2)

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

        JCa = Cards(deck)
        JCa.Shuff_deck()
        print(JCa.deck)

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

    # Si escogiste 4 jugadores
    else:
        
        JCa = Cards(deck)
        JCa.Shuff_deck()
        print(JCa.deck)

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


    return
    # ------------------------------------------------------------------------ #

if __name__ == "__main__":
    Main()
