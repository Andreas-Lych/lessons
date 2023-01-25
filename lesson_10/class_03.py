"""
Создать генератор и/или итератор простой геометрической прогрессии. a = an-1*q
"""

a_first = 3 # знаменатель прогрессии
n = 12 # число элементов прогрессии
q = 4 # знаменатель прогрессии

print(a_first)
# в переменной i_prev будем хранить значение предыдущего элемента
# поместим в переменную i_prev значение первого элемента
a_prev = a_first
# Для каждого элемента прогрессии, начиная с первого:
for i in range(3, n):
    # вычислим значение элемента,
    a_cur = a_prev*q
    # выведем его на экран,
    print(a_cur)
    # сохраним значение текущего элемента в переменной b_prev
    a_prev = a_cur


import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def my_generator(power: int, limit: int):
    for current in range(1, limit + 1):
        yield current * power


if __name__ == "__main__":
    my_geo = my_generator(power=2, limit=5)
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    for item in my_geo:
        logger.info(item)