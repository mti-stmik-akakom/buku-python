# map.py

def make_ucase(the_str):
    return the_str.upper()

# a => iterable
a = ['a', 'b', 'c']

# kerjakan fungsi make_ucase utk setiap item a
b = map(make_ucase,a)

for c in b:
    print(c)
