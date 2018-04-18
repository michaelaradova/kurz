"""Na prvni a posledni radek vypise radku X, v radcich mezi napise X vzdy jen
   do prvniho a posledniho sloupce"""

pocet_radku = int(input("Zadej pocet radku: "))
while pocet_radku <= 0:
    pocet_radku = int(input("Pocet radku musi byt kladny. Zadej znova: "))
pocet_sloupcu = int(input("Zadej pocet sloupcu: "))
while pocet_sloupcu <= 0:
    pocet_sloupcu = int(input("Pocet sloupcu musi byt kladny. Zadej znova: "))

for cislo_radku in range(0, pocet_radku):
    for cislo_sloupce in range(0, pocet_sloupcu):
        if (cislo_radku == 0 or cislo_radku == pocet_radku - 1 or
           cislo_sloupce == 0 or cislo_sloupce == pocet_sloupcu - 1):
            # - 1, protoze range uz posledni cislo neuvazuje
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
