n = int(input('N:15'))

result = 0
current = 1

while current <= n:
    result += current ** 3
    current += 1

print(result)