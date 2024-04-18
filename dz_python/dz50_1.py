# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение, что такой таблицы нет.

import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit'}


table_name = input("Введите название таблицы: ")

try:
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    res = cursor.fetchall()
    if res:
        print(*res)
except mysql.connector.Error:
    print(f"Таблицы '{table_name}' нет")

finally:
    cursor.close()
    connection.close()
