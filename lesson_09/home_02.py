"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""
import math
tip=str(input("Введите название фигуры ="))
if tip=="треугольник":
    a=float(input("Введите сторону a ="))
    b=float(input("Введите сторону b ="))
    c=float(input("Введите сторону c ="))
    p=(a+b+c)/2
    s=math.sqrt((p*(p-a)*(p-b)*(p-c)))
elif tip=="прямоугольник":
    a=float(input("Введите сторону a ="))
    b=float(input("Введите сторону b ="))
    s=a*b
elif tip=="круг":
    r=float(input("Введите радиус r ="))
    s=math.pi*(r**2)
print(s)
