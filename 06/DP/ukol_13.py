"""Na prvni a posledni radek vypise radku X, v radcich mezi napise X vzdy jen
   do prvniho a posledniho sloupce"""

pocet_radku = 6
pocet_sloupcu = 6

for cislo_radku in range(0, pocet_radku):
    for cislo_sloupce in range(0, pocet_sloupcu):
        if cislo_radku == 0 or cislo_radku == pocet_radku - 1:
            print("X", end=" ")
        else:
            if cislo_sloupce == 0 or cislo_sloupce == pocet_sloupcu - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
    print()
