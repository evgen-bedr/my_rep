year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0:
    if year % 400 != 0:
        print('Год является високосным.')
else: print('Год не является високосным.')
