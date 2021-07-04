# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
# A megoldást egy fajl2.py nevű file-ban kell beadnod.


with open("adat.txt", "r") as f1:
    my_list = f1.readlines()
    for sor in my_list:
        print(sor.strip(), end=" ")