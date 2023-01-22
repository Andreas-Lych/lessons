"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""
# мой метод - не правильный
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

# from manti
from lesson_09.home_01 import Point, Circle, Triangle, Square

if __name__ == "__main__":
    a = Point(3, 7)
    circle = Circle(a, 3)

    a = Point(3, 7)
    b = Point(5, 2)
    square = Square(a, b)

    a = Point(1, 1)
    b = Point(7, 2)
    c = Point(5, 5)
    triangle = Triangle(a, b, c)

    for figure in [circle, square, triangle]:
        print(figure.__class__.__name__, figure.perimeter(), figure.area())
