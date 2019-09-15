# reduce.py

from functools import reduce

# tanpa lambda expression dan reduce
hasil = 1
x = [1, 2, 3, 4, 5]
for num in x:
    hasil = hasil * num

print(hasil)

# dengan lambda expression dan reduce
hasil2 = reduce((lambda x, y: x * y),[1, 2, 3, 4, 5])

print(hasil2)

# hasil:
# 120
# 120
