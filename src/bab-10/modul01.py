# modul-01.py 

def penambah(*args):
    total = 0
    for op in args:
        total += op
    return total

# jika di-import, maka __name__ berisi nama modul yaitu 
# namafile.py
# jika dijalankan dari shell / command line, maka 
# __name__ akan berisi '__main__'
# jadi, di bawah ini tidak akan dijalankan jika di-import
if __name__ == '__main__':
    print(penambah(32,43,12))
