"""Vypise tabulku o velikosti zadane uzivatelem, kde na kazde pozici je X"""

pocet_radku = int(input("Zadej pocet radku: "))
while pocet_radku <= 0:
    pocet_radku = int(input("Pocet radku musi byt kladny. Zadej znovu: "))

pocet_sloupcu = int(input("Zadej pocet sloupcu: "))
while pocet_sloupcu <= 0:
    pocet_sloupcu = int(input("Pocet sloupcu musi byt kladny. Zadej znovu: "))
    
for cislo_radku in range(pocet_radku):
    for cislo_sloupce in range(pocet_sloupcu):
        print("X", end=" ")
    print("")
