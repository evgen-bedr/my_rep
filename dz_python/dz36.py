# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
#
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

from functools import reduce
def sum_squared(a: list[str]) -> int:
    int_num = map(int, a)
    int_num = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, int_num))
    int_num = reduce(lambda x, y: x + y, int_num)
    return int_num


inp_list = '4, 6, 3, 4, 2, 3, 9, 0, 7'.split(', ')
print(sum_squared(inp_list))


# Напишите функцию, которая принимает на вход список функций и значение, а затем применяет композицию этих функций к значению, возвращая конечный результат.
#
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9


from functools import reduce

def compose_functions(functions, value):
    return reduce(lambda val, func: func(val), functions, value)


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]
print(compose_functions(functions, 5))
