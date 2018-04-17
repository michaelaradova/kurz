"""Na prvni radek napise 'první řádek', na dalsi radky pak 'není první'."""

pocet_radku = int(input("Zadej pocet radku: "))
while pocet_radku <= 0:
    pocet_radku = int(input("Pocet radku musi byt kladny. Zadej znovu: "))

for cislo_radku in range(1, pocet_radku+1):
    # +1 je v range, protoze range posledni cislo uz neuvazuje
    if cislo_radku == 1:
        vystup = "první řádek"
    else:
        vystup = "není první"
    print(vystup)
