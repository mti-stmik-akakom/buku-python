# dict.py

rumah = {'H-304': 'Bambang Purnomosidi', 'H-303': 'Anton'}
print(rumah)
print(rumah.items())
print(rumah['H-304'])
for k, v in rumah.items():
    print(f'Rumah nomor {k} adalah tempat tinggal keluarga {v}')

print('H-304' in rumah)
print('H-305' in rumah)
print('H-304' not in rumah)
print(sorted(rumah))
