"""Генератор паролей"""

import random
import string

print(__doc__)
print('--------------')

while True:

    def pass_generator(num_of_symbols):
        lit_sm = list(string.ascii_lowercase.lower())
        lit_bg = list(string.ascii_lowercase.upper())
        num = list(map(str, range(0, 10)))
        sym = ['*', '/', '+', '-', '=', '!']
        lvl1 = [random.choice([lit_sm, lit_bg, num, sym]) for i in range(num_of_symbols+1)]
        lvl2 = [random.choice(i) for i in lvl1]
        password = ''.join(lvl2)
        print(password)

    pass_generator(8)

    exit_from = input('Выйти? Y/N:  ')
    if exit_from == 'y' or exit_from == 'Y':
        break
    elif exit_from == 'n' or exit_from == 'N':
        continue
