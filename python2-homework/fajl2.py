# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
# A megoldást egy fajl2.py nevű file-ban kell beadnod.

with open("adat.txt", "r") as f2:
    my_list = f2.readlines()
    print(my_list)
