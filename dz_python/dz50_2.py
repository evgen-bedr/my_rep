# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и вывести все покупки этого пользователя.

import mysql.connector
from mysql.connector import Error

dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'ich_edit'
}

try:
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()

    cursor.execute('SELECT id, name FROM users')
    users = cursor.fetchall()

    user_ids_by_name = {}
    for user_id, name in users:
        if name not in user_ids_by_name:
            print(name, end=', ')
            user_ids_by_name[name] = []
        user_ids_by_name[name].append(user_id)
    print()

    input_name = input('Введите имя для поиска: ')
    if input_name in user_ids_by_name:
        user_ids = user_ids_by_name[input_name]

        query = '''
        SELECT sales.id, product.prod, product.quantity
        FROM product
        JOIN sales ON sales.pid = product.pid
        WHERE sales.id IN (%s)
        '''
        format_strings = ','.join(['%s'] * len(user_ids))
        cursor.execute(query % format_strings, tuple(user_ids))

        products = cursor.fetchall()

        user_products = {}
        for user_id, prod, quantity in products:
            product_info = f'{prod} (Количество: {quantity})'
            if user_id not in user_products:
                user_products[user_id] = []
            user_products[user_id].append(product_info)

        for user_id, prods in user_products.items():
            print(f'{input_name} - ' + ', '.join(prods))

except Error as e:
    print(f"Произошла ошибка: {e}")

finally:
    cursor.close()
    connection.close()
