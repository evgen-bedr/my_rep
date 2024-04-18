# 1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
#
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

class Counter:
    def __init__(self, number):
        self.number = number

    def __iadd__(self, val):
        self.number += val
        return self

    def __isub__(self, val):
        self.number -= val
        return self

    def __str__(self):
        return str(self.number)

    def __int__(self):
        return self.number


counter = Counter(5)
counter += 3
print(counter)
counter -= 2
print(int(counter))


# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
#
# Пример использования:
# email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
# print(email1)  # Вывод:
#
# """
#
# From: john@example.com
# To: jane@example.com
# Subject: Meeting
# Hi Jane, let's have a meeting tomorrow.
#
# """
#
#
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True

class Email:
    def __init__(self, *args):
        self.email_from = args[0]
        self.email_to = args[1]
        self.theme = args[2]
        self.text = args[3]
        self.date = tuple(map(int, args[4].split('-')))

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __ne__(self, other):
        return self.date != other.date

    def __str__(self):
        return f'From: {self.email_from}\nTo: {self.email_to}\nSubject: {self.theme}\n{self.text}'

    def __len__(self):
        return len(self.text)

    def __hash__(self):
        return hash((self.email_from, self.email_to, self.theme, self.text, self.date))

    def __bool__(self):
        if self.text != '':
            return True
        return False


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)
print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)
