# 1 задание
names = ['Lena', 'Olga', 'Olga', 'Lena', 'Sasha', 'Egor', 'Lena', 'Igor']

name_count = {}

for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print(name_count)

# 2 задание

numbers = [23, 45, 76, 89, 5]

sum_of_numbers = sum(numbers)

product_of_numbers = 1
for number in numbers:
    product_of_numbers *= number

result_dict = {sum_of_numbers: product_of_numbers}

print(result_dict)

# 3 задание

names = ['Lena', 'Olga', 'Olga', 'Lena', 'Sasha', 'Egor', 'Lena', 'Igor']

unique_names = []
for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)
print("Количество уникальных имен:", len(unique_names))
