old_dict = {"1": "Alex", "22": "Olga", "311": "Roma"}

# Генерация словаря с условием
new_dict = {}
for key, value in old_dict.items():
   if key == "1" or key == "22" or key == "311":
       new_dict[key + str(len(key))] = f"value = {value}"

print(new_dict)

# Словарное включение
new_dict = {
  key + str(len(key)): f"value = {value}"
  for key, value in old_dict.items()
  if key == "1" or key == "22"
}

print(new_dict)

first_name = input()
last_name = input()

my_string_1 = f"Hello, {first_name} {last_name}"
print(my_string_1)
