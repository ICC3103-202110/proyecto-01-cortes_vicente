from cards import Cards
# -------------------------------   Def Main  -------------------------------- #
def main():
    J1cards = []
    J2cards = []
    J3cards = []
    J4cards = []
    deck = ["D", "D", "D", "A", "A", "A", "Ca", "Ca", "Ca", "E", "E", "E", "Co", "Co", "Co"]# Existen 15 cartas de personaje, 3 de cada tipo: Duque, Asesino, Capitán, Embajador y Condesa
    J1C = Cards(deck, J1cards) # Aqui cree los objetos por separado,
    J2C = Cards(deck, J2cards) # no se me ocurrio otra forma de hacerlo para que cada jugador tuviera sus cartas independientemente
    J3C = Cards(deck, J3cards)
    J4C = Cards(deck, J4cards)
    J1C.Shuff_deck() # El mazo lo barajo solo una vez
    print(deck)
    J1C.Share_cards() # Aqui reparto las cartas a cada jugador, y elimino las dos primeras cartas del mazo (ya que se las di a un jugador)
    J2C.Share_cards()
    J3C.Share_cards()
    J4C.Share_cards() # ojo que todo esto la idea es ponerlo en un ciclo for para no repetir codigo pero de momento lo dejo asi
    print(J1cards)
    print(J2cards)
    print(J3cards)
    print(J4cards)
    print(deck)
    return ""

    # ------------------------------------------------------------------------ #

if __name__ == "__main__":
    main()
