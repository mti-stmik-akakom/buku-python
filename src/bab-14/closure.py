# closure.py

from functools import partial

# bilangan pangkat eksponen
def pangkat(bilangan, eksponen):
  return bilangan ** eksponen

kuadrat = partial(pangkat, eksponen=2)
print(kuadrat(2))
# hasil = 2

# parsial:
# pangkat dipanggil dengan arg eksponen ditetapkan di awal
pangkat_empat = partial(pangkat, eksponen=4)
print(pangkat_empat(2))
# hasil = 16
