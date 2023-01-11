"""
генератор от 1 до 100 в диапазоне 5
"""

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

print(now)

print(f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}")

print(now.date())
print(now.time())



