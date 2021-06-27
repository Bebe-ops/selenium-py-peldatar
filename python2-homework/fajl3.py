# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
# A megoldást egy fajl3.py nevű file-ban kell beadnod.

with open("adat.txt", "r") as f3:
    list_orig = f3.readlines()
    list2 = []
    for i in list_orig:
        list2.append(i.strip())

# írás fájlba
with open("adat2.txt", "w") as file:
    file.write(str(list2))
