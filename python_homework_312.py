# 1 задание

def calculate_numbers(a, b, c):
    sum_of_numbers = a + b + c
    product_of_numbers = a * b * c
    max_number = max(a, b, c)
    min_number = min(a, b, c)

    print(f'Сумма: {sum_of_numbers}')
    print(f'Произведение: {product_of_numbers}')
    print(f'Наибольшее число: {max_number}')
    print(f'Наименьшее число: {min_number}')


calculate_numbers(3, 5, 2)

# 2 задание

# def analyze_string(user_input):
#     words = user_input.split()
#
#     total_words = len(words)
#
#     words_more_than_two = len([word for word in words if len(word) > 2])
#
#     print(f'Общее количество слов: {total_words}')
#     print(f'Количество слов с более чем 2 символами: {words_more_than_two}')
#     print(f'Введенная строка в нижнем регистре: "{user_input.lower()}"')
#     print(f'Введенная строка в верхнем регистре: "{user_input.upper()}"')
#
#
# user_input = input('Введите строку: ')
# analyze_string(user_input)

# 3 задание

original_list = [1, 30, 30, 25, 24, 30, 1, 27, 25, 40]

unique_numbers = list(set(original_list))
print('Уникальные числа:', unique_numbers)

filtered_list = [num for num in original_list if num > 24]
print('Числа больше 24:', filtered_list)

even_dict = {str(index + 1): num for index, num in enumerate(filtered_list) if num % 2 == 0}
print('Словарь с четными числами:', even_dict)

# 4 задание

def centimeters_to_meters(centimeters):
    meters = centimeters / 100
    return meters


cm = 250
m = centimeters_to_meters(cm)
print(f'{cm} сантиметров равно {m} метров.')

# 5 задание

def my_func(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f'{hours} час(а) {remaining_minutes} минут(ы)'


result = my_func(90)
print(result)

# 6 задание

def my_func(number):
    if 100 <= number <= 999:
        hundreds = number // 100
        tens = (number // 10) % 10
        units = number % 10


        sum_of_digits = hundreds + tens + units
        product_of_digits = hundreds * tens * units

        return f'Сумма цифр = {sum_of_digits}, Произведение цифр = {product_of_digits}'
    else:
        return 'Ошибка: Введите положительное трёхзначное число.'



result = my_func(132)
print(result)

# 7 задание

# def is_in_range(x, a, b):
#
#     if a <= x <= b:
#         return True
#     else:
#         return False
#
# x = int(input('Введите число x: '))
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
#
# if is_in_range(x, a, b):
#     print(f'Число {x} принадлежит промежутку от {a} до {b}.')
# else:
#     print(f'Число {x} не принадлежит промежутку от {a} до {b}.')

# 8 задание

def create_dict(txt_1, txt_2):
    if len(txt_1) == len(txt_2):
        return {txt_1[i]: txt_2[i] for i in range(len(txt_1))}
    else:
        return 'Ошибка: Длины строк должны быть одинаковыми.'


txt1 = 'abcde'
txt2 = '12345'
result = create_dict(txt1, txt2)
print(result)

# 9 задание

# def collect_user_info(full_name, age, phone_number):
#
#     if age < 1 or age > 150:
#         print('Предупреждение: Возраст должен быть от 1 до 150 лет. Установлен возраст = 0.')
#         age = 0
#
#     if len(phone_number) < 4 or len(phone_number) > 11:
#         print('Предупреждение: Номер телефона должен содержать от 4 до 11 символов. Установлен номер = 8-000-000-00-00.')
#         phone_number = '8-000-000-00-00'
#
#     user_info = {
#         'ФИО': full_name,
#         'Возраст': age,
#         'Номер телефона': phone_number
#     }
#
#     return user_info
#
# full_name = input('Введите ФИО: ')
# age = int(input('Введите возраст: '))
# phone_number = input('Введите номер телефона: ')
#
# result = collect_user_info(full_name, age, phone_number)
#
# print(result)


# 10 задание

text = 'Python is the best programming language'

length_of_string = len(text)
print('Количество символов в строке:', length_of_string)

first_character = text[0]
print('Первый элемент строки:', first_character)

last_character = text[-1]
print('Последний элемент строки:', last_character)

first_word = text.split()[0]
print('Первое слово:', first_word)

last_word = text.split()[-1]
print('Последнее слово:', last_word)

programming_word = text[20:30]
print("'Слово 'programming' с использованием среза:'", programming_word)

# 11 задание

def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return 'Ошибка: Деление на ноль!'
    else:
        return 'Ошибка: Неизвестная операция!'

# Пример использования функции
operation = input('Введите операцию (add, subtract, multiply, divide): ')
a = float(input('Введите первое число (a): '))
b = float(input('Введите второе число (b): '))

result = calculator(operation, a, b)
print('Результат:', result)
