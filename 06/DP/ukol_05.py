"""Vypise uzivatelem zadany pocet radku, na kazdem je napsano 'a'."""

pocet_radku = int(input("Zadej pocet radku pro vypis 'a': "))

while pocet_radku < 0:
    print("Pocet radku nemuze byt zaporny.")
    pocet_radku = int(input("Zadej pocet radku pro vypis 'a': "))

for cislo_radku in range(pocet_radku):
    print("a")
