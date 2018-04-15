"""Vypise tabulku vsech variant vzajemneho nasobeni cisel od 0 do 4"""

for cislo_radku in range(5):
    for cislo_sloupce in range(5):
        soucin = cislo_radku * cislo_sloupce
        print(soucin, end=" ")
    print("")
