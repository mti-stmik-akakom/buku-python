daftar = ["first", "2nd", 3]

for a in daftar:
    print(a)

print(" === 1 === ")

for a in range(20):
    print(a) # 0 - 19

print(" === 2 === ")
for a in range(1, 5):
    print(a) # 1 -4

print(" === 3 === ")
for a in 'ABCDEFG':
    print(a)

print(" === 4 === ")
# range(start, stop, step)
for a in range(1, 5, 2):
    print(a) # 1, 3
else:
    print("bukan selisih 2")

print(" === 5 === ")
for a in range(20):
    if a > 0 and a % 2 == 0:
        print(a, " habis dibagi dua")
    else:
        print(a, " ganjil")
