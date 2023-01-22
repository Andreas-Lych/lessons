"""
Создать тест в отдельном файле и проверить несколько телефонных номеров.
"""


from lesson_10.class_01 import check_string

if __name__ == "__main__":
    assert check_string("+375 (29) 299-20-29") is not None
    assert check_string("+375 (29) 300-00-00") is not None


