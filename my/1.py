import random


def generate_data():
   return {
      f"key-{value}": random.randint(1, 100)
      for value in range(5)
   }

def main():
   data = generate_data()
   print(data)


if __name__ == "__main__":
   main()

   from datetime import datetime

   now = datetime.now()

   # 2021-07-21 20:18:56.239443
   print(now)

   # 21.5.2021 20:18
   print(f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}")

   print(now.date())
   print(now.time())


   class Parent:
      def print_world(self):
         print("Parent: World")


   class Child(Parent):
      def print_hello(self):
         print("Child: Hello")

class Car:
   last_model = None

   def __init__(self, model):
       self.model = model

   @classmethod
   def get_last_model(cls):
       return cls.last_model


Car.last_model = "Opel"


print(Car.get_last_model())
