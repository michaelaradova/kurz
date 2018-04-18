"""Obsahuje nekolik matematicky zamerenych fci - vypocet faktorialu; urceni,
   zda jde o prvocislo; vypis Fibonacciho posloupnosti"""

from math import sqrt, ceil


def faktorial(cislo):
    """Vypocte faktorial z daneho cisla"""
    faktorial_cisla = 1
    for i in range(2, cislo+1):
        # +1 v range, protoze range neuvazuje posledni cislo
        faktorial_cisla = faktorial_cisla * i
    return faktorial_cisla


def prvocislo(cislo):
    """Urci, zda je zadane cislo prvocislo"""
    # zda je cislo prvocislo se da overit tim, ze se overi, ze neni delitelne
    # zadnym cislem od 2 do odmocniny z toho cisla
    odmocnina = sqrt(cislo)
    # zjisteni, zda je cislo delitelne 2
    delitel = 2
    zbytek_deleni = cislo % delitel
    if zbytek_deleni == 0:
        print("{} neni prvocislo. Je delitelne {}.".format(cislo, delitel))
        return False  # pokuj delitelne 2, neni prvocislo
    # zjistovani, zda je cislo delitelne nejakym lichym cislem az do odmocniny
    # daneho cisla
    delitel = 3
    while zbytek_deleni != 0 and delitel <= ceil(odmocnina):
        zbytek_deleni = cislo % delitel
        delitel = delitel + 2  # + 2, protoze testuji jiz jen licha cisla
    if zbytek_deleni == 0:
        print("{} neni prvocislo. Je delitelne {}.".format(cislo, delitel-2))
        return False
    else:
        print("{} je prvocislo.".format(cislo))
        return True


def Fibonacciho_posloupnost(pocet_cisel):
    """Vrati dany pocet cisel z Fibonacciho posloupnosti"""
    cislo1 = 0
    cislo2 = 1  # prvni cislo Fibonacciho posloupnosti
    Fib_posloupnost = ""
    for i in range(0, pocet_cisel):
        Fib_posloupnost = Fib_posloupnost + " " + str(cislo2)
        docasne_cislo2 = cislo2
        cislo2 = cislo1 + cislo2
        cislo1 = docasne_cislo2
    return Fib_posloupnost


# aby se nasledujici kod spoustel jen, kdyz volam z prikazove radky
if __name__ == "__main__":
    cislo_x = int(input("Zadej cele nezaporne cislo pro provedeni"
                        + " matematickych operaci: "))
    while cislo_x <= 0:
        cislo_x = int(input("Je potreba cele nezaporne cislo. Zadej znova: "))
    print()  # prazdna radka pro prehlednost vypisu
    faktorial_x = faktorial(cislo_x)
    print("Faktorial cisla {} je: {}".format(cislo_x, faktorial_x))
    print()  # prazdna radka pro prehlednost vypisu
    je_prvocislo = prvocislo(cislo_x)
    print()  # prazdna radka pro prehlednost vypisu
    Fib_posloupnost = Fibonacciho_posloupnost(pocet_cisel=cislo_x)
    print("Prvnich {} clenu Fibonacciho posloupnosti je: {}".format(cislo_x,
          Fib_posloupnost))
