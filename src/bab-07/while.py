nilai = 1

# akan ditampilkan angka 1 - 9 
# setelah itu berhenti
while nilai < 10:
    print(nilai)
    nilai += 1

while nilai <= 20:
    print(nilai)
    nilai += 1
else:
    print("nilai sudah mencapai 20 ...")

input("Tekan sembarang tombol untuk meneruskan ... ")

# akan ditampilkan angka 21 
# dan seterusnya tidak akan berhenti
# kecuali ditekan Ctrl-C
while True:
    print(nilai)
    nilai += 1
