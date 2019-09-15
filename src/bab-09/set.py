# set.py

proglang = {'Rust', 'Python', 'Go', 'Rust'}
print(proglang)
tambahan = ('Ruby', 'Lua')
proglang.add(tambahan)
print(proglang)
print('Rust' in proglang)

huruf = set('Wabi Teknologi')
print(huruf)

huruf2 = set()
print(huruf2)
huruf2.add('Wabi Teknologi')
print(huruf2)

kata1 = set('indonesia')
kata2 = set('merdeka')
print(kata1)
print(kata2)

# ada di kata1, tidak ada di kata2
print(kata1 - kata2)

# ada di kata1 atau di kata2 atau di keduanya
print(kata1 | kata2)

# ada di kata1 dan kata2
print(kata1 & kata2)

# ada di kata1 atau di kata2 tapi tidak di keduanya
print(kata1 ^ kata2)
