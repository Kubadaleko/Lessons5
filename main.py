# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод

# 8-5+2-1
# Вывод
# 4

a = input(
    'Введите любые целые положительные однозначные числа и знаки сложения или вычитания между ними : '
)
print(a)
res = int(a[0])
for i in range(len(a)):
    if type(a[i]) == int:
        res = int(a[i]) + res
    elif a[i] == '-':
        res = res - int(a[i + 1])
    elif a[i] == '+':
        res = res + int(a[i + 1])
print(res)

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# Формат ввода
# Вводится строка.

# Формат вывода
# Выведите слова из строки по одному.

# Пример 1
# Ввод

# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод

# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

string = input(' :')
word = ''
for i in string:
    if i != ' ':
        word = word + i
    elif i == ' ':
        print(word)
        word = ''
print(word)

# или еще вариант, но тут ! или ? в вывод не попадают.

string = input(':')
word = ''
for i in string:
    if i.isalpha():
        word = word + i
    elif not i.isalpha():
        print(word)
        word = ''
print(word)
