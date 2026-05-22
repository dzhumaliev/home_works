import sqlite3


# A4
connect = sqlite3.connect('users.db')

# Рука и ручка
cursor = connect.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
               name VARCHAR (50) NOT NULL,
               age INTEGER,
               hobby TEXT
               )


''')

connect.commit()


# CRUD Create-Read-Update-Delete

def create_user(def_name, def_age, def_hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (def_name, def_age, def_hobby)
    )

    connect.commit()
    print('пользователь добавлен!!')



create_user('Ardager', 27, "Гоооры")