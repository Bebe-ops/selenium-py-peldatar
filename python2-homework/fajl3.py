# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!

with open("adat.txt", "r") as f3:
    list_orig = f3.readlines()
    list2 = []
    for i in list_orig:
        list2.append(i.strip())

# írás fájlba
with open("adat2.txt", "w") as file:
    file.write(" ".join(list2))
