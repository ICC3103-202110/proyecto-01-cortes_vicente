from cards import Cards
from coins import Coins
# -------------------------------   Def Main  -------------------------------- #
def main():

    J1cards = []
    J2cards = []
    J3cards = []
    Jcards = [J1cards, J2cards, J3cards]
    J1coins = 0
    J2coins = 0
    J3coins = 0
    J4coins = 0
    deck = ["D", "D", "D", "A", "A", "A", "Ca", "Ca", "Ca", "E", "E", "E", "Co", "Co", "Co"]# Existen 15 cartas de personaje, 3 de cada tipo: Duque, Asesino, Capitán, Embajador y Condesa


    # ------------------------   Class Coins objects  ------------------------ #

    J1Co = Coins(J1coins)
    J2Co = Coins(J2coins)
    J3Co = Coins(J3coins)
    J4Co = Coins(J4coins)

    # ------------------------------------------------------------------------ #
    a = input("Ingrese la cantidad de jugadores(3 o 4): ")
    if a == 3:
        J4 = False
    else:
        J4cards = []
        Jcards.append(J4cards)
        J4 = True

    JCa = Cards(deck, Jcards) 
    JCa.Shuff_deck()
    print(deck)

    if J4 == False:
        Jcards.pop(3)
    for i in range(len(Jcards)):
        JCa = Cards(deck, Jcards[i])
        JCa.Share_card()
        JCa.Share_card()
    
    print(Jcards)
    print(deck)


    #J1Ca.Show_hand()
    #J2Ca.Show_hand()
    #J3Ca.Show_hand()
    #J4Ca.Show_hand() 

    J1Co.Award_coin()
    J1Co.Award_coin()
    J2Co.Award_coin()
    J2Co.Award_coin()
    J3Co.Award_coin()
    J3Co.Award_coin()
    J4Co.Award_coin()
    J4Co.Award_coin()

    print(J1coins)
    print(J2coins)
    print(J3coins)
    print(J4coins)

    return ""

    # ------------------------------------------------------------------------ #

if __name__ == "__main__":
    main()
