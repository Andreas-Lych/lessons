"Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m), а также количество x этих чисел."

n = 7
m = 35
primary_count = 0

for current in range(n, m + 1):
    is_primary = True
    for x in range(2, current):
        if current % x == 0:
            is_primary = False
            break
    if is_primary:
        primary_count += 1
        print(current)

print("primary_count", primary_count)