my_war1 = input('Введите первое логическое значение (True или False): ').capitalize()
while my_war1 != "True" and my_war1 != "False":
    my_war1 = input('Вы допустили ошибку в слове (True или False): ')
my_war1 = my_war1 == "True"

my_war2 = input('Введите второе логическое значение (True или False): ').capitalize()
while my_war2 != "True" and my_war2 != "False":
    my_war2 = input('Вы допустили ошибку в слове (True или False): ')
my_war2 = my_war2 == "True"

print(my_war1 and my_war2)
print(my_war1 or my_war2)
print(not my_war1)
print(not my_war2)
print(my_war1 == my_war2)
print(my_war1 != my_war2)
