# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
#
# Пример использования:
# @validate_args(int, str)
# def greet(age, name):
#
#     print(f"Привет, {name}! Тебе {age} лет.")
#
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
#
# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

def validate_args(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError(f"Аргумент {args[0]} имеет неправильный тип {type(args[0])}. Ожидается <class 'int'>.")
        if not isinstance(args[1], str):
            raise TypeError(f"Аргумент {args[1]} имеет неправильный тип {type(args[1])}. Ожидается <class 'str'>.")
        return func(*args, **kwargs)

    return wrapper


@validate_args
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


try:
    greet("25", "Анна")
except TypeError as e:
    print(e)

# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
#
# Пример использования:
# python
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(5, 7)
#
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.


from logging import basicConfig
from logging import info
from logging import INFO

basicConfig(filename='log.txt', level=INFO, format='%(message)s', encoding='utf-8')


def my_logging(func):
    def wrapper(*args):
        res = func(*args)
        info(f'Аргументы {args}, результат {res}')

    return wrapper


@my_logging
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)
