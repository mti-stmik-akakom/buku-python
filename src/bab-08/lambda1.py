# lambda1.py

# definisi: 
# lambda arg1, arg2, ... , argN: ekspresi

multiple = lambda x, y: x * y

print(multiple(10,20))

def kali_berapa(n):
    return lambda a: a * n

kali_dua = kali_berapa(2)

print(kali_dua(90))
