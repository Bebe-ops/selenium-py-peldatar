# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
# ahogy beolvastad, soronként egy szóval egy másik fájlba!
# A megoldást egy fajl4.py nevű file-ban kell beadnod.

with open("adat.txt", "r") as f3:
    my_list1 = f3.readlines()

# írás fájlba
with open("adat3.txt", "w") as f1:
    f1.write(str(my_list1))
