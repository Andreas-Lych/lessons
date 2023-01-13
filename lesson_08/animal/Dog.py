"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Добавить конструктор класса и
инициализировать атрибуты класса значениями переменных. Класс имеет три метода: jump, run, bark. Каждый метод выводит
сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""

from lesson_08.animal.animal import Animal
class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking")

if __name__ == "__main__":
    dog = Dog(100, 50, "My dog", 10)

    dog.jump()
    dog.run()
    dog.bark()

    print(dog.name, dog.age, dog.height, dog.weight)