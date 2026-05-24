import sqlite3

connect = sqlite3.connect("grade.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(30) NOT NULL,
               age INTEGER NOT NULL
               )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               subject VARCHAR(20) NOT NULL,
               grade INTEGER NOT NULL,
               user_id INTEGER NOT NULL,
               FOREIGN KEY (user_id) REFERENCES users(id)
               )
''')

connect.commit()

def create_user(name, age):
    cursor.execute(
        'INSERT INTO users(name, age) VALUES(?,?)',
        (name, age)
    )
    connect.commit()
    print("Пользователь создан")

# create_user("Isak", 28)
# create_user('LoLo', 15)

def create_grade(subject, grade, user_id):
    cursor.execute(
        'INSERT INTO grades(subject, grade, user_id) VALUES (?,?,?)',
        (subject, grade, user_id)
    )
    connect.commit()
    print("Оценка создана")

# create_grade("Алгебра", 5, 1)
# create_grade("Русский", 4, 3)

def get_user_grade():
    cursor.execute('''SELECT users.name, grades.subject
                   FROM users FULL OUTER JOIN grades ON users.id = grades.user_id
                   ''')
    data = cursor.fetchall()

    for i in data:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}")

# get_user_grade()

def get_old_user():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)


get_old_user()