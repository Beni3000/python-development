def collect_user_info():

    with open('users.txt', 'w', encoding='utf-8') as file:
        for user_number in range(1, 4):
            print(f'Введите информацию для Пользователя {user_number}:')
            name = input('Имя: ')
            surname = input('Фамилия: ')
            phone = input('Телефон: ')

            file.write(f'Пользователь {user_number}:\n')
            file.write(f'Имя - {name}\n')
            file.write(f'Фамилия - {surname}\n')
            file.write(f'Телефон - {phone}\n')
            file.write('---------------------\n')

collect_user_info()

print('Информация успешно записана в файл users.txt.')
