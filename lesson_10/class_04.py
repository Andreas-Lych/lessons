"""
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + NxM.
"""


n = int(input("Введите число n =")) # число
m = int(input("Введите число m =")) # число

temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp

comp = n + int(t1) + int(t2)
print("Результат равен:", comp)