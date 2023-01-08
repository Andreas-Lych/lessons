'''
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
'''

with open(":home\lessons\lesson_01\LICENSE.txt", "r") as file_obj:
    for line in file_obj:
       print(line)

my_list = ['one', 'two', 'three', 'four', 'one']
filtered_names = []
for word in my_list:
    if