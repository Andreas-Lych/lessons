import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()

create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", "36")
create_user("Andreas", "Lych", "andreas1981@gmail.com", "TestPass", "39")