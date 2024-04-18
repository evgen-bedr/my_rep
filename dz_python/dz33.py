# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
#
# Пример вызова функции и ожидаемого вывода:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)  # Ожидаемый вывод: "dragonfruit"

from typing import List

def find_longest_word(items_list: List[str]) -> str:
    word = max(items_list, key=len)
    return word


words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)


# 2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для аргументов
# и возвращаемых значений функций. Создайте текстовый файл "products.txt",
# в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество". Например:
#
# Apple, 1.50, 10
# Banana, 0.75, 15

# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую стоимость.
# Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на составляющие и создайте список продуктов.
# Затем вызовите функцию calculate_total_price с этим списком и выведите результат.
#
# Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода. Потому что в реальных задачах обычно этого нет.
# Нужно самому придумывать даже самые простые тестовые данные, содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно.

from typing import List

def calculate_total_price(product_list: List[str]) -> float:
    hashmap = {}
    for i in range(0, len(product_list), 3):
        total_price = float(product_list[i + 1]) * float(product_list[i + 2])

        if product_list[i] not in hashmap:
            hashmap[product_list[i]] = total_price
        else:
            hashmap[product_list[i]] += total_price

    return sum(hashmap.values())



with open('products.txt', 'r') as file:
    items = file.read().replace('\n', ', ').split(', ')

print(calculate_total_price(items))