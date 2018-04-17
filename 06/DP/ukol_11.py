"""Vypise na kazdy radek tolik X, kolikaty je to radek """

pocet_radku = int(input("Zadej pocet radku: "))
while pocet_radku <= 0:
    pocet_radku = int(input("Zadane cislo musi byt kladne. Zadej znovu: "))
    
for cislo_radku in range(1, pocet_radku+1):
    # +1 je v range, protoze range posledni cislo uz neuvazuje
    for cislo_sloupce in range(cislo_radku):
        print("X", end=" ")
    print()
