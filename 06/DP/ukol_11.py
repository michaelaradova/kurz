"""Vypise na kazdy radek tolik X, kolikaty je to radek """

for cislo_radku in range(1, 5):
    for cislo_sloupce in range(cislo_radku):
        print("X", end=" ")
    print()
