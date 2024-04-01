import os

jmena_slozek = [
    'obrazky',
    'texty',
    'gify'
    ]

for slozka in jmena_slozek:
    if os.path.isdir(slozka):
        print("Slozka jiz existuje!")
    else:
        os.mkdir(slozka)
        print(f"Tvorim novou slozku: {slozka}")
        
print('Vsechny slozky existuji')