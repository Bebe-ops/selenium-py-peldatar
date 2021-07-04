# Python függvények gyakorlása
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.


# megoldas1
def szokoev(evszam):
    if evszam % 4 == 0:
        if evszam % 100 == 0:
            if evszam % 400 == 0:
                print(f' A megadott ev ({evszam}) szokoev! ')
            else:
                print(f' A megadott ev ({evszam}) nem szokoev! ')
        else:
            print(f' A megadott ev ({evszam}) szokoev! ')
    else:
        print(f' A megadott ev ({evszam}) nem szokoev! ')


# my_evszam = int(input("Kérlek írd be az évszámot: "))
# szokoev(my_evszam)




def tests():
    for i in test_data:
        szokoev(i)


test_data = [2005, 2000, 1980, 1900]
tests()



# # megoldas2 - boolean
# def szoko(ev):
#     if ev % 4 == 0 and ev % 100 != 0 or ev % 400 == 0:
#         return True
#     elif ev % 400 == 0 and ev % 100 != 0:
#         return False
#     else:
#         return False
#
#
# def test_datas():
#     print(2005, szoko(2005))
#     print(2000, szoko(2000))
#     print(1980, szoko(1980))
#     print(1900, szoko(1900))


# test_datas()