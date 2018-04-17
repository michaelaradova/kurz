"""Vypise uzivatelem zadany pocet radku s napisem Radek a cislo radku."""

pocet_radku = int(input("Zadej pocet radku pro vypis: "))

while pocet_radku < 0:
    print("Pocet radku nemuze byt zaporny.")
    pocet_radku = int(input("Zadej pocet radku pro vypis: "))

for cislo_radku in range(1, pocet_radku + 1):
    print("Řádek", cislo_radku)
