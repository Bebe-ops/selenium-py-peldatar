"""
Python for ciklus gyakorlása
1. Írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat! A kiírás több oszlopos legyen,
és legfeljebb 10 soros.
A megoldashoz használd a beépített ord() es chr() függvényeket.
"""

# megoldas1
for sor in range(0, 9):
    for i in range(97 + sor, 123 + sor, 9):
        if i < 123:
            print(chr(i), i, " ", end=" ")
    print()
print()

# megoldas2 -ez nem tökéletes
elso = list(range(97, 106))
masodik = list(range(106, 116))
harmadik = list(range(116, 126))

for i in range(0, len(elso)):
    print(chr(elso[i]), elso[i], " ", chr(masodik[i]), masodik[i], " ", chr(harmadik[i]), harmadik[i])
