"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте
номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random

my_names = ['h6', 'h7', 'h8', 'h9', 'h10', 'hJ', 'hD', 'hK', 'hA', 'd6', 'd7', 'd8', 'd9', 'd10', 'dJ', 'dD', 'dK', 'dA',
'c6', 'c7', 'c8', 'c9', 'c10', 'cJ', 'cD', 'cK', 'cA', 's6', 's7', 's8', 's9', 's10', 'sJ', 'sD', 'sK', 'sA']

print(random.sample(my_names, 2))