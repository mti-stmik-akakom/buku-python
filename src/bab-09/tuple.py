# tuple.py

the_data = 234, 'data 1', 'data 2', 343
print(the_data)
# hasil: (234, 'data 1', 'data 2', 343)

print(the_data[2])
# hasil: data2

# the_data[2] = 'change this'
# error: TypeError: 'tuple' object does not support item assignment

data2 = 'data x', 'data y', (123, 321)
print(data2)
# hasil: ('data x', 'data y', (123, 321))
print(data2[2][1])
# hasil: 321
for a in data2:
    print(a)
# hasil:
#   data x
#   data y
#   (123, 321)

# membuat tuple yang hanya berisi 1:
data3 = 435,
print(data3)
# hasil: (435,)

