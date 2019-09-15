# iterator.py

daftar = [1,2,3,4,5,6]

# cara iterator
i_daftar = iter(daftar)

print(i_daftar)

a = 1

while a < len(daftar):
    print(next(i_daftar))
    a += 1

# cara mudah
for z in daftar:
    print(z)
