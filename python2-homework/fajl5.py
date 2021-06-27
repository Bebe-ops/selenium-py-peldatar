# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz!
# A megoldást egy fajl5.py nevű file-ban kell beadnod.

with open("adat.txt", "r") as f:
    with open("adat4.txt", "w") as f2:
        f2.write(f.read())
