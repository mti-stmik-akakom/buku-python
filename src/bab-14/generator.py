# generator.py

def generate_val(N):
    for i in range(N):
        yield i

hasil = generate_val(10)
print(hasil)

for a in hasil:
    print(a)
