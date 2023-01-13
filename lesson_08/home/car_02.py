"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран
"""
from lesson_08.home.car import Car

class New_car(Car):

    def speed_5(self):
        print(f"{self.mark} speed increased to 100km/h")
    def speed_now(self):
        print(f"{self.mark}, current speed is 100km/h")
    def change_mark(self, mark):
        self.mark = mark
if __name__ == "__main__":
    car = New_car("Car", "E500", 2000, 100)

    car.speed_5()
    car.change_mark(mark="Mercedes")
    car.speed_now()


    print(car.mark, car.model, car.age, car.speed)
