"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий. Реализовать следующие функции
 для продуктов: создание, чтение, обновление по id, удаление по id. 
"""

import sqlite3

def create_product(id: int, name: str, cost: int, quantity: int, comment: str):
   with sqlite3.connect("my_product.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO product (id, name, cost, quantity, comment)
           VALUES (?, ?, ?, ?, ?);
           """,
           (id, name, cost, quantity, comment),
       )
       session.commit()

create_product (1000, "chair", 50, 30, "вся цветовая гамма")
create_product (1001, "sofa", 450, 12, "комплектация под заказ")
create_product (1002, "table", 250, 6, "вся цветовая гамма")
create_product (1003, "carpet", 150, 6, "размер 1000х2000")
create_product (1004, "armchair", 249, 16, "геймерское кресло")

# поиск по id
def select_product(id: int):
   with sqlite3.connect("my_product.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user_01
           WHERE id = ?;
           """,
           (id,)
       )
       session.commit()
       return cursor.fetchone()

select_product(1003)

#удаление по id
def delete_product(id: int):
   with sqlite3.connect("my_product.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           DELETE *
           FROM user_01
           WHERE id = ?;
           """,
           (id,)
       )
       session.commit()
       return cursor.fetchone()

delete_product(int(input()))