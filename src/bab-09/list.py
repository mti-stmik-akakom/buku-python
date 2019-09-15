# list.py

daftar_makanan = ['soto', 'bakso', 'pecel', 'nila bakar']

print(daftar_makanan)
# hasil: ['soto', 'bakso', 'pecel', 'nila bakar']

print()
for makanan in daftar_makanan:
    print(makanan)
    # hasil:
    #   soto
    #   bakso
    #   pecel
    #   nila bakar

print()
print(daftar_makanan[0])
# soto

print()
print(daftar_makanan[-1])
# nila bakar

print()
print(daftar_makanan[-3])
# bakso

print()
print(daftar_makanan[-2:])
# hasil: ['pecel', 'nila bakar']

print()
print(daftar_makanan[:])
# hasil: ['soto', 'bakso', 'pecel', 'nila bakar']

daftar2 = daftar_makanan + ['oseng tempe', 'sayur pisang']
print()
print(daftar2)
# hasil: ['soto', 'bakso', 'pecel', 'nila bakar', 'oseng tempe', 'sayur pisang']
jml_makanan = len(daftar2)
print(f'ada {jml_makanan} jumlah makanan')

# list bersifat mutable
daftar2[1] = 'mie ayam'
print()
print(daftar2)
# hasil: ['soto', 'mie ayam', 'pecel', 'nila bakar', 'oseng tempe', 'sayur pisang']

# index 2 diganti sampai sebelum index 4
daftar2[2:4] = ['pecel lele','nila goreng']
print()
print(daftar2)
# hasil: ['soto', 'mie ayam', 'pecel lele', 'nila goreng', 'oseng tempe', 'sayur pisang']

# list bisa berada di dalam list
daftar2[1] = ['mie ayam biasa', 'mie ayam bakso', 'mie ayam istimewa']
print()
print(daftar2)
# hasil: ['soto', ['mie ayam biasa', 'mie ayam bakso', 'mie ayam istimewa'], 
#       'pecel lele', 'nila goreng', 'oseng tempe', 'sayur pisang']
print(daftar2[1])
# hasil: ['mie ayam biasa', 'mie ayam bakso', 'mie ayam istimewa']
print(daftar2[1][2])
# hasil: mie ayam istimewa

