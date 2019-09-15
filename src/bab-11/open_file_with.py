# open_file_with.py

# default: tanpa argumen mode, dibuka utk dibaca (read)
with open('angka.txt') as f:
    read_data = f.read()
    print(read_data)
    # error: io.UnsupportedOperation: not writable
    #f.write('tambahan 1')

# dengan 'with',  tidak perlu di close
print(f.closed)

# r+ => read write
with open('angka.txt','r+') as f:
    read_data = f.read()
    print(read_data)
    # bisa ditulisi karena r+
    f.write('tambahan')

# r+ => read write
# dibuka dengan w+ membuat isi hilang
with open('angka.txt','w') as f:
    f.write('tambahan')

with open('angka.txt') as f:
    read_data = f.read()
    print(f'sekarang hanya berisi 1 baris: {read_data}')

# sekarang diisi dengan loop angka
with open('angka.txt', 'w') as f:
    for a in range(1,11):
        f.write(str(a) + '\n')

# tampilkan hasil pengisian
with open('angka.txt') as f:
    for line in f:
        print(line, end='')
