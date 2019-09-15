# kelas.py

# definisi kelas paling sederhana
# bisa ditambah properties
class Dosen:
    pass

bpdp = Dosen()
bpdp.nama = 'Bambang Purnomosidi'

print(bpdp)
print(bpdp.nama)

class DosenSTMIKAkakom(Dosen):

    institusi = 'STMIK AKAKOM'

    # konstruktor
    def __init__(self, npp, nama):
        self.npp = npp
        self.nama = nama

    def mengajar(self, *args):
        self.mk_diampu = args

bambangpdp = DosenSTMIKAkakom('123', 'bpdp')
print(bambangpdp)
bambangpdp.mengajar('Teknologi Cloud Computing', 'Big Data Analytics')
print(bambangpdp.mk_diampu)
print(bambangpdp.institusi)

class DosenSTMIKAkakomTI(DosenSTMIKAkakom):

    prodi = 'Teknik Informatika'

nia = DosenSTMIKAkakomTI('213','Nia R')
print(nia.institusi)
print(nia.prodi)

 
