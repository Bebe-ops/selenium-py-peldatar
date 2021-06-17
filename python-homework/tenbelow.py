# Python while ciklus gyakorlása
# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!
# A megoldást egy tenbelow.py nevű file-ban kell beadnod.


num = 0
numbers = []
while True:
    num = int(input("Kérek egy számot: "))
    if num >= 10:
        break
    else:
        numbers.append(num)
print(sum(numbers))