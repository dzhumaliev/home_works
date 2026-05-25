import sqlite3




connect = sqlite3.connect('store.db')

cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR (50) NOT NULL,
               price INTEGER,
               quantity INTEGER
               )
            ''')
connect.commit()

print('Таблица создана!!')

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES(?,?,?)',
        (name, price, quantity)
    )
    connect.commit()
    print('Продукт добавлен!!')



# create_product('Молоко', 100, 10)
# create_product('Хлеб', 50, 20)
# create_product('Яйца', 200, 30)



def read_products():
    cursor.execute(
        'SELECT * FROM products'
    )
    print('Продукты получены!!')
    return cursor.fetchall()

print(read_products())


def update_product(id, price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, id)
    )
    connect.commit()
    print('Продукт обновлен!!')

# print(update_product(1, 120))

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (id,)
    )
    connect.commit()
    print('Продукт удален!!')

# print(delete_product(5))