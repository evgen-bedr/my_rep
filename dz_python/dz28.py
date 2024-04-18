# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее часто встречающиеся слова.
# Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством вхождений каждого слова.
# Выведите наиболее часто встречающиеся слова и их количество.
#
# Пример вывода:
#
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

from string import punctuation
from collections import Counter

def count_words(text):
    t = str.maketrans('', '', punctuation)
    text = text.lower().translate(t).split()
    text = Counter(text)
    return text


my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."

for key, val in count_words(my_text).most_common(2):
    print(f"{key}: {val}")


# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке, включающий поля name, age и city.
# Создайте список объектов Person и выведите информацию о каждом человеке на экран.
#
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

people = [
    Person(name="Alice", age=25, city="New York"),
    Person(name="Bob", age=30, city="London"),
    Person(name="Carol", age=35, city="Paris")
]

for i in people:
    print(f"Name: {i.name}, Age: {i.age}, City: {i.city}")


# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного ключа с использованием метода get или setdefault.
# Создайте функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта. Выведите полученное значение на экран.
#
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

def get_value_from_dict(dict_inc, key, method):
    if method == 'y':
        return dict_inc.get(key)
    else:
        return dict_inc.setdefault(key, 0)

my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key = input('Введите ключ для поиска: ').lower()

method = input('Использовать метод get (y/n)? ').lower()
res = get_value_from_dict(my_dict, key, method)
print(f"Значение для ключа '{key}': {res}")
