"""Vypise, jaka je 2. mocnina cisel od 0 do uzivatelem zadaneho cisla."""

print("Vypoctu a vypisu druhe mocniny pro cisla od nuly az po zadane cislo.")
maximum = int(input("Zadej cele nezaporne cislo: "))

while maximum < 0:
    print("Cislo nema byt zaporne.")
    maximum = int(input("Zadej cele nezaporne cislo: "))

for mocnenec in range(maximum + 1):
    # + 1 je v range, protoze range uz posledni cislo neuvazuje
    mocnina = mocnenec ** 2
    print(mocnenec, "na druhou je", mocnina)
