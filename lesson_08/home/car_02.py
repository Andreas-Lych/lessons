"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран
"""
from lesson_08.home.car import Car

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
        print(f"{self.mark} speed increased to 100km/h")
    def change_mark(self, mark):
        self.mark = mark

if __name__ == "__main__":
    car = Car("Car", "E500", 2000, 100)

    car.speed_1()
    car.change_mark(mark="Mercedes")


    print(car.mark, car.model, car.age, car.speed)
