while True:
    operation = input('''
Sčítání:    "+"
Odčítání:   "-"
----------------------
Vyber si operaci: '''
    )
    
    if operation not in ('+','-'):
        print('Nezadali jste platný operátor, zkuste to znovu.')
        continue

    number_1 = int(input('Zadej první číslo: '))
    number_2 = int(input('Zadej druhé číslo: '))

    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')

    if again == 'a':
        continue
    else:
        print('Ukončuji...')
        break

print('aa')