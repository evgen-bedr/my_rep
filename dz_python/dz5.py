a, b, c = float(input('Введите первое целое число: ')), float(input('Введите второе целое число: ')), float(input('Введите третье целое число: '))

if int(a) == a:
    a = int(a)
if int(b) == b:
    b = int(b)
if int(c) == c:
    c = int(c)

num_min = min(a, b, c)
num_max = max(a, b, c)

if num_min == a and num_max == c:
    print(a, b, c)
elif num_min == a and num_max == b:
    print(a, c, b)
elif num_min == b and num_max == a:
    print(b, c, a)
elif num_min == b and num_max == c:
    print(b, a, c)
elif num_min == c and num_max == a:
    print(c, b, a)
else:
    print(c, a, b)
