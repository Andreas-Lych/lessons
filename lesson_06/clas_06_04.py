"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае
положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту,
либо сумма его карт больше 21-го.
"""

import random
count = 0
my_names = ['h6', 'h7', 'h8', 'h9', 'h10', 'hJ', 'hD', 'hK', 'hA', 'd6', 'd7', 'd8', 'd9', 'd10', 'dJ', 'dD', 'dK', 'dA',
'c6', 'c7', 'c8', 'c9', 'c10', 'cJ', 'cD', 'cK', 'cA', 's6', 's7', 's8', 's9', 's10', 'sJ', 'sD', 'sK', 'sA']

my_dict = {'h6': 6, 'h7': 7, 'h8': 8, 'h9': 9, 'h10': 10, 'hJ': 2, 'hD': 3, 'hK': 4, 'hA': 11, 'd6': 6, 'd7': 7, 'd8': 8,
           'd9': 9, 'd10': 10, 'dJ': 2, 'dD': 3, 'dK': 4, 'dA': 11, 'c6': 6, 'c7': 7, 'c8': 8, 'c9': 9, 'c10': 10,
           'J': 2, 'cD':3, 'cK': 4, 'cA': 11, 's6': 6, 's7': 7, 's8': 8, 's9': 9, 's10': 10, 'sJ': 2,
           'sD': 3, 'sK': 4, 'sA': 11}

from random import sample

data = list(my_dict.items())
r = sample(data, 2)
print(random.sample(data, 2))

while True:
    choice = input('будете брать карту? y/n\n')
    if choice == 'y':
        data = list(my_dict.items())
        r = sample(data, 1)
        print(random.sample(data, 1))
    elif choice == 'n':
        print('вы закончили игру.')
        break

"""y
def nominal_to_value(nominal):
    return my_dict[nominal]
"""