# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

import sys
import os

if len(sys.argv) < 2:
    print("Нужно указать путь")
else:
    script_path = sys.argv[1]

    if not os.path.exists(script_path):
        print("Файл не существует")
    elif not os.path.isfile(script_path):
        print("Путь не является файлом")
    elif not script_path.endswith(".py"):
        print("Не является Python файлом")
    else:
        os.system(f"python {script_path}")
        print(f"Файл {script_path} успешно запущен")


# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории
# и выводит список всех файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории

import os
import sys

if len(sys.argv) > 1:
    script_path = sys.argv[1]
    if os.path.isdir(script_path):
        for script_path, script_names, file_names in os.walk(script_path):
            for name in script_names + file_names:
                print(os.path.join(script_path, name))
    else:
        print("Указанный путь не существует или не является директорией")
else:
    print("Необходимо указать путь к директории как аргумент")