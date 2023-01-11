"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""

    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

if __name__ == "__main__":

    dog = Dog(100, 50, "My dog", 10)
    dog.bark()
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

    cat = Cat(50, 7, "My cat", 4)
    cat.meow()
