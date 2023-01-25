""""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык. Написать
две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.
"""
dictionary = {
    "apple": "яблоко",
    "car": "машина",
    "map": "карта"
}

def eng_to_rus(word):
 return dictionary.get(word, "ERROR")

def rus_to_eng(word):
    return {
        value: key
        for key, value in dictionary.items()
    }.get(word, "ERROR")

print(eng_to_rus("apple"))

print(rus_to_eng("карта"))