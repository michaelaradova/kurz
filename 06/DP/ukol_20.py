"""Nacte cislo a zjisti, zda je sude."""

print("Urcim, zda je zadane cislo sude.")
cislo = int(input("Zadej cele cislo: "))

if cislo % 2 == 0:
    print("Cislo {} je sude.".format(cislo))
else:
    print("Cislo {} je liche.".format(cislo))
