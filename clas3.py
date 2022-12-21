n = int(input('N:'))

result = 0
current = 1

while current <= n:
    result += current ** 3
    current += 1

print(result)