# Создать функцию, которая создает таблицу user, для примера использовать слайд №12.
# Запустить функцию и проверить, что создался файл базы данных.
# Создать функцию, которая позволяет добавлять данные в таблицу user.
# Добавить 5 различных записей.
# Создать функцию для поиска всех пользователей с определенным именем.
# Запустить функцию и найти хотя бы одного пользователя по имени.
# Создать функцию для поиска всех пользователей в возрасте от X до Y лет.
# Создать программу позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры.
import sqlite3
from datetime import datetime


def create_user_table(firstname: str, lastname: str, email: str, password: str, age: int, created_at: datetime):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR,
            lastname VARCHAR,
            email VARCHAR,
            password VARCHAR,
            age INTEGER,
            created_at DATETIME
            );
            """,
        )
        session.commit()


def create_user(firstname: str, lastname: str, email: str, password: str, age: int, created_at: datetime):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age, datetime)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age, created_at)
        )
        session.commit()


create_user("Maxim", "Kanashits", "maxi@gmail.com", "TestPass", 12, datetime.now())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
