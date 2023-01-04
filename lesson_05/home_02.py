def my_func(a, b):
    if a > 5:
        b += 5
        for x in range(5):
            a += x
            my_sum = a + b
            return my_sum

result = my_func(4, 7)
print(result)