"Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран."

str = "аргентина манит негра"
if str == str[::-1]:
    print("yes")
    if str != str[::-1]:
        print("no")


my_str = "аргентина манит негра"

my_str = my_str.lower().replace(" ", "")

if my_str == my_str[::-1]:
    print("True")


