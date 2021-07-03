# Az autód 7 litert fogyaszt országúton és 9-et városban.
# A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
# Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel
# (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára)
# dolgozol, hanem a felhasználótól kéred ezeket be.
# Ahol szükséges, ne feledd konvertálni az értékeket!
"""
# megoldás előre megadott értékekkel
my_o_fogy = 7 / 100
my_v_fogy = 9 / 100
my_o_ut_oda = 170
my_v_ut_oda = 35
benzin = 350


def fogyasztas_oda(o_fogy, v_fogy, o_ut_oda, v_ut_oda):
    return o_ut_oda * o_fogy + v_ut_oda * v_fogy


ossz_fogy_oda = fogyasztas_oda(my_o_fogy, my_v_fogy, my_o_ut_oda, my_v_ut_oda)
print(f' A fogyasztás az odaúton: {ossz_fogy_oda} liter benzin.')


def fogyasztas_oda_vissza(ossz_fogy_oda):
    return ossz_fogy_oda * 2


ossz_fogy_oda_vissza = fogyasztas_oda_vissza(ossz_fogy_oda)
print(f' A fogyasztás oda-vissza: {ossz_fogy_oda_vissza} liter benzin.')


def ossz_koltseg(ossz_fogy_oda_vissza, benzin):
    return ossz_fogy_oda_vissza * benzin


koltseg = ossz_koltseg(ossz_fogy_oda_vissza, benzin)
print(f' A teljes út költsége: {koltseg} HUF.')

"""

# megoldas bekért értékekkel
orszaguti_fogyasztas = float(input(" Mennyit eszik az autód országúton (/100 km): "))
varosi_fogysztas = float(input(" Mennyit eszik az autód városban (/100 km):  "))
orszagut_hossz = float(input(" Hány Kilométert utazol országúton: "))
varosut_hossz = float(input(" Hány Kilométert utazol városban: "))
benzin_ar = float(input(" Mennyibe fáj a benzin literje: "))


def calc():
    ossz_fogy_oda = (orszaguti_fogyasztas * orszagut_hossz + varosi_fogysztas * varosut_hossz) / 100
    ossz_fogy_oda_vissza = ossz_fogy_oda * 2
    koltseg = ossz_fogy_oda_vissza * benzin_ar
    print(f' A fogyasztás az odaúton: {ossz_fogy_oda} liter benzin.')
    print(f' A fogyasztás oda-vissza: {ossz_fogy_oda_vissza} liter benzin.')
    print(f' A teljes út költsége: {koltseg} HUF.')


calc()
