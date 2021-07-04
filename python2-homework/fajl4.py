# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
# ahogy beolvastad, soronként egy szóval egy másik fájlba!

with open("adat.txt", "r") as file:
    with open("adat3.txt", "w") as out:
        my_list = file.readlines()
        for line in my_list:
            out.write(line)
