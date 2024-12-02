# создание списка
# с использованием функции list()
users = list()
# с использованием литерала []
#            0      1 (-2)   2 (-1)
# Доступ к элементам списка
users_2 = ['Dima', 'Vova', 'Elena']
print(users_2[0])
print(users_2[-1])
print(users_2[1])
# print(users_2[4])

# Добавление элемента в список
# users_2.append(['Olga', 'Sasha'])
# print(users_2)

users_2.append('Olga')
# расширения списка элементами другого списка
users_2 += ['Sasha', 'Masha']
users_2.extend(['Natasha', 'Sveta'])

#
print(users_2)