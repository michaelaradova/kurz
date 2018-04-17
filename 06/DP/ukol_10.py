"""Vypise tabulku vsech variant vzajemneho nasobeni cisel od 0 do uzivatelem
   zadaneho cisla"""

print("Vypisu tabulku vsech variant vzajemneho nasobeni cisel od 0 do" +
      " zadaneho cisla.")
maximum = int(input("Zadej cele kladne cislo: "))
while maximum <= 0:
    maximum = int(input("Zadane cislo musi byt kladne. Zadej znovu: "))

for cislo_radku in range(maximum+1):
    # +1 je v range, protoze range posledni cislo jiz neuvazuje
    for cislo_sloupce in range(maximum+1):
        # +1 je v range, protoze range posledni cislo jiz neuvazuje
        soucin = cislo_radku * cislo_sloupce
        if soucin <= 9:  # pridani dvou mezer pred jednociferny soucin
            print("  ", soucin, end=" ", sep="")
        elif soucin <= 99:  # pridani jedne mezery pred dvouciferny soucin
            print(" ", soucin, end=" ", sep="")
        else:
            print(soucin, end=" ")
    print("")
