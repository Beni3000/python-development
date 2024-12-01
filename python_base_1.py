# Типы данных

# Integer (int) - целые числа
a = 5
b = 2
c = a + b
d = a % b


print(c)
print(d)
print(a**2)

# Float (float) - вещественные числа

float_a = 0.5
float_b = 1.25

print(type(a))
print(type(float_a))

# Boolean - лоигический тип данных
is_active = False
is_logout = True

# print(is_active or is_logout)
# print(is_active and is_logout)
# print(not is_active and is_logout)
#
# print(a < b)
# print(a > b)
# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)

# приведение строки к типу
age = '15'
year = '2024'
print(int(age) + int(year))

# String (str) - строковый тип даных

text = "I 'love' Python!"
text = text + 'a'
text += 'a'

# None

flag = None

#  Структуры данных
# списки - list() - []

cars = ['bmw', 'audi', 24, True, [1,2]]

# словари - dict() - {}

info = {
    'name': 'Alex',
    'cars': cars,
}

# кортежи - tuple - ()
colors = (
    ('red', '255,0,0'),
    ('blue', '0,0,255')
)

# set - set() - множества - {}

set_numbers = {1,2,3,4,5,5,5,5,5}

# Функции
#Файлы
#Классы

# name = 5
# name = 6

'''
gfjflhjhjfljhjf
fhfhjkjflfh
fhjfhj
'''
text_many_lines = """fkshdkfahfha
dghshkhgs
"""

number = 6
print(number)

# вод данных в консоль

name = input("Введите свое имя ")
age = input("Введите свой возраст ")

print(type(age))