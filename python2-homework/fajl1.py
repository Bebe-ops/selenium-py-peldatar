# Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget, hanem minden sort
# azonnal kiírsz!

# egy sorban kiírva
with open("adat.txt", "r") as f:
    print(f.readlines())

print("°" * 95)

# fájl kiírása soronként
with open("adat.txt", "r") as file:
    print(file.read())

print("°" * 95)

# 1 sorba kiírva folyó szövegként:
with open("adat.txt", "r") as f1:
    for sor in f1:
        print(sor.strip() + " ", end="")
