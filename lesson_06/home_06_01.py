'''
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
'''

file_obj = open("LICENSE", "r")

for line in file_obj:
   print(line)

import collections

text = line
words = line.split()
counter = collections.Counter(words)
longest = max(words, key=len)

print(longest)

from collections import Counter
import re

text = line

cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', text))
print(cnt.most_common(1))


