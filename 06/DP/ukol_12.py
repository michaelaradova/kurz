"""Na prvni radek napise 'první řádek', na dalsi radky pak 'není první'."""

for cislo_radku in range(1, 5):
    if cislo_radku == 1:
        vystup = "první řádek"
    else:
        vystup = "není první"
    print(vystup)
