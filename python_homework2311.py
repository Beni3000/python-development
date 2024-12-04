# 1 задание
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7, 8]
#
#
# general_elements = set(list1) & set(list2)
# print('Общие элементы списков:', general_elements)
#
#
# difference_first = set(list1) - set(list2)
# print("Элементы, которые есть в первом списке, но нет во втором:", difference_first)

# 2 задание

brand = input('Введите марку машины: ')
model = input('Введите модель машины: ')
year = input('Введите год выпуска машины: ')
color = input('Введите цвет машины: ')


car = {
    'марка': brand,
    'модель': model,
    'год_выпуска': year,
    'цвет': color
}


keys = list(car.keys())
print("Список ключей словаря:", keys)


print("Список значений словаря:")
for keys, meaning in car.items():
    print(f"{keys} -> {meaning}")
