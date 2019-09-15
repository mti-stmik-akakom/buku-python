# except.py

import sys

# tanpa exception handling
# b = float(input('masukkan angka float: '))
# amasukkan angka float: f
# Traceback (most recent call last):
#  File "except.py", line 5, in <module>
#    b = float(input('masukkan angka float: '))
# ValueError: could not convert string to float: 'f'

# Setelah dihandle:
try:
    a = float(input("masukkan angka float: "))
except ValueError:
    print('harus memasukkan nilai float')

# Jika tidak tau kemungkinan error:
try:
    a = float(input("masukkan angka: "))
    b = float(input("masukkan angka pembagi: "))
    z = a/b
except:
    print("Error:", sys.exc_info()[0])
else:
    print('Hasil bagi: ', z)
finally:
    # bagian ini biasanya untuk clean-up, di dunia nyata 
    # biasanya berisi bagian utk close connection, menutup
    # file dan lain-lain
    print('Selesai')
# hasil:
# masukkan angka: 40
# masukkan angka pembagi: 0
# Error: <class 'ZeroDivisionError'>
