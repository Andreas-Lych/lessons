"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса
Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""
Class Point:
x = int(input())
y = int(input())

Class Figure:

Class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
def area(self):
    return 3.14 * self.radius ** 2

Class Triangle(Figure):
    def __init__(self, area):
        self.area = area
def area(self):
    return (a*b)/2

Class Square(Figure):
    def __init__(self, length):
        self.length = length
def area(self):
    return self.length ** 2

