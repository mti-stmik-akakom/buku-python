nilai = int(input("Masukkan nilai siswa = "))

if nilai > 60:
    print("Lulus")
else:
    print("Tidak lulus")

if nilai <= 10:
    print("Anda harus mengulang semester depan")

ipsemester = float(input("Masukkan nilai IP semester = "))

if ipsemester > 3:
    print("Anda bisa mengambil 24 SKS")
elif ipsemester >= 2.75:
    print("Anda bisa mengambil 21 SKS")
elif ipsemester >= 2:
    print("Anda bisa mengambil 18 SKS")
else:
    print("Anda hanya bisa mengambil 12 SKS")
