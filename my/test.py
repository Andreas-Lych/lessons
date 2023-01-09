message = 'hello world'
print(message)

name = 'tom and jerry'
print(name)

text = """За каждой успешной продажей стоит текст. Начиная с рекламного объявления и заканчивая надписью
         Но больше всего заказов копирайтерам приходит с e-commerce ниши и от интернет-магазинов (ИМ) в частности.
На сайте интернет-магазина может быть как 100, так и 100 000 страниц. На каждую нужно написать уникальный,
оптимизированный и грамотный текст. А если учесть, что сайтов ИМ в Рунете больше, чем волос у вас на голове, получается
непаханое поле работы.
Давайте же разберёмся, как писать тексты для разных страниц интернет-магазина и что вообще копирайтер может предложить
бизнесу в этой сфере."""
print(text)

userName = "Andreas"
userAge = 42
user = f"name: {userName} age: {userAge}"
print(user)

string = "hello world"
for char in string:
    print(char)

name = "Tom"
surname = "Smith"
fullname = name + " " + surname
print(fullname)

class person:
 __slots__ = ["first_name", "last_name", "phone"]
 def__init__(self, first_name, last_name, phone):
   self.first_name = first_name
   self.last_name = last_name
   self.phone = phone

