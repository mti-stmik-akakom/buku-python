# filter.py

nilai = range(-10, 10)

for a in nilai:
    print(a)
    # hasilL -10 sampai 10

# Kita akan memfilter list sehingga hanya yang berisi nilai positif
# yang akan masuk ke list baru

l_baru = list(filter(lambda angka: angka > 0, nilai))
print(l_baru)
# hasil: [1, 2, 3, 4, 5, 6, 7, 8, 9]
