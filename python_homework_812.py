import os

# 1 задание
def create_numbers_file():
    os.makedirs('numbers', exist_ok=True)

    with open('numbers/numbers.txt', 'w', encoding='utf-8') as file:
        for i in range(1, 11):
            file.write(f"{i} {11 - i}\n")


create_numbers_file()

print("Файл numbers.txt успешно создан и записан в каталог 'numbers'.")

# 2 задание

import os


def read_numbers_file():
    """Читает файл numbers.txt и возвращает список строк."""
    with open('numbers/numbers.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


def calculate_product_sum(lines):
    """Возвращает сумму произведений чисел в каждой строке."""
    total_sum = 0
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            first_number = int(numbers[0])
            second_number = int(numbers[1])
            total_sum += first_number * second_number
    return total_sum


def extract_right_column(lines):
    """Возвращает список чисел из правого столбца."""
    right_column = []
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            right_column.append(int(numbers[1]))
    return right_column


def write_results_to_file(product_sum, right_column):
    """Записывает результаты в файл numbers_result.txt."""
    with open('numbers/numbers_result.txt', 'w', encoding='utf-8') as file:
        file.write(f"Сумма произведений: {product_sum}\n")
        file.write("Числа из правого столбца:\n")
        file.write(' '.join(map(str, right_column)) + '\n')


def main():
    # Читаем файл numbers.txt
    lines = read_numbers_file()

    # Вычисляем сумму произведений
    product_sum = calculate_product_sum(lines)

    # Извлекаем числа из правого столбца
    right_column = extract_right_column(lines)

    # Записываем результаты в файл
    write_results_to_file(product_sum, right_column)

    print("Результаты успешно записаны в файл numbers_result.txt.")


# Запуск основной функции
main()
