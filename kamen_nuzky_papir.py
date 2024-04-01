import random

moznosti = [
    'kamen',
    'nuzky',
    'papir'
    ]

hrac = moznosti[1]

pocitac = random.choice(moznosti)

if hrac == pocitac:
    print('Nerozhodne!')
elif pocitac == papir:
    print('Prohral jsi :(')
else:
    print('Vyhral jsi!')