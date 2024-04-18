#1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

with open('test.txt', 'w') as file:
    file.write('10 -2')

try:
    with open('test.txt', 'r') as file:
        numbers = file.read().split()

    num1, num2 = map(int, numbers)

    if num1 > 0 and num2 > 0:
        print(num1 / num2)

    if num1 < 0 or num2 < 0:
        raise ValueError("Число должно быть положительным")

except ValueError as ff:
    print(ff)


# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами (ValueError, ZeroDivisionError).
# Используйте конструкцию try-except-finally для обработки исключений и закрытия файла в блоке finally.


file = 0
try:
    file = open('test.txt', 'r')
    numbers = file.read().split()
    num1, num2 = map(int, numbers)
    print(num1 / num2)

except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Mistake in values')
except ZeroDivisionError:
    print('На 0 нельзя')


finally:
    if file:
        file.close()