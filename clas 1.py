import random

my_lyst =[]

x = random.randint(0, 20)
for i in range(x):
    y = random.randint(0, 100)
    my_lyst.append(y)

print(my_lyst)

for i in range(3):
    y = random.randint(0, 100)
    my_lyst.append(y)

print(my_lyst)

result = 0

for element in my_lyst:
    if element > 10:
        result = result + element