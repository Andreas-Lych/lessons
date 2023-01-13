"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""
from lesson_08.animal.animal import Animal


class Cat(Animal):

    def meow(self):
        print(f"{self.name} is meowing")

if __name__ == "__main__":
    cat = Cat(50, 7, "My cat", 4)

    cat.jump()
    cat.run()
    cat.meow()


    print(cat.name, cat.age, cat.height, cat.weight)