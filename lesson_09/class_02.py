"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические методы сравнения
 (==, !=, >=, <=, <, >).

Переопределить магические методы сложения, вычитания, умножения на число.

Создать метод, который выводит на экран отформатированное время (HH:MM:SS).

Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.

Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать
результат.

Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day, month, year.
“Исправить” все магические методы для этого класса.

Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""
from __future__ import annotations
class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp

    def __add__(self, other) -> MyTime:
        timestamp = self.timestamp + other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)

    def __str__(self):
        return f"MyTime: {self.hours}:{self.minutes}:{self.seconds}"


if __name__ == "__main__":
    time1 = MyTime(12, 12, 12)
    time2 = MyTime(12, 12, 12)
    print(time1 == time2)
    print(time1 + time2)
