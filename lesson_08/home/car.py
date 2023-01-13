"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости
(скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задний ход
(изменение знака скорости).
"""

class Car:
    mark = None
    model = None
    age = None
    speed = None

    def __init__(self, mark, model, age, speed):
        self.mark = mark
        self.model = model
        self.age = age
        self.speed = speed

    def speed_1(self):
        print(f"{self.mark} speed is 0km/h")
    def speed_2(self):
        print(f"{self.mark} speed, + 5km/h")

    def speed_3(self):
        print(f"{self.mark} speed, - 5km/h")

    def speed_4(self):
        print(f"{self.mark} is stopping, 0km/h")

if __name__ == "__main__":
    car = Car("Car", "prototype", 2023, 0)

    car.speed_1()
    car.speed_2()
    car.speed_3()
    car.speed_4()

    print(car.mark, car.model, car.age, car.speed)