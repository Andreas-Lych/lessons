import random

my_list =[]

x = random.randint(0, 20)
for i in range(x):
    y = random.randint(0, 100)
    my_list.append(y)

print(my_list)

for i in range(3):
    y = random.randint(0, 100)
    my_list.append(y)

print(my_list)

result = 0

for element in my_list:
    if element > 10:
        result = result + element