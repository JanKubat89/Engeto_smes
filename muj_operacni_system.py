import random

hadana_slova = ['dva', 'hudba', 'vecernicek']

def tajne_slovo():
    slovo = random.choice('slovo')
    return slovo

def vytvor_tajenku(slovo):
    tajenka = ['_'] * len(slovo)
    return tajenka

print(vytvor_tajenku('slovo'))

def ziskej_indexy_pismen(slovo)
    
    for poradi, pismeno in enumerate(slovo):
        