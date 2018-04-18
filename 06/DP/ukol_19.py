"""Zepta se na 3 cisla a zjisti, jestli je jejich soucet vetsi nez 10."""

print("Sectu 3 zadana cisla a vypisu, zda je jejich soucet vetsi nez 10.")
soucet = 0

for i in range(1, 4):
    cislo = float(input("Zadej {}. cislo: ".format(i)))
    soucet = soucet + cislo

print("Soucet zadanych cisel je: {} ".format(soucet), end="")
if soucet > 10:
    print("a je tedy vetsi nez 10.")
else:
    print("a je tedy mensi nebo roven 10.")
