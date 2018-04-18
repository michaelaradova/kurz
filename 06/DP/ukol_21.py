"""Vypise cisla od 1 do 100. Pokud je cislo delitelne 3, napise misto nej 
   'bum'. Pokud je delitelne 5, napise 'bác'. Pokud zaroven 3 i 5, napise
   'bum-bác'."""

for cislo in range(1, 101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("bum-bác")
    elif cislo % 3 == 0:
        print("bum")
    elif cislo % 5 == 0:
        print("bác")
    else:
        print(cislo)