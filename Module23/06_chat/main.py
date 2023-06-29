
while True:
    user = input('Введите имя пользователя: ')
    print('1 - Посмотреть текущий текст чата')
    print('2 - Отправить сообщение')
    choice = input()
    choicecheck = ('1', '2')
    if choice not in choicecheck:
        raise ValueError('Введите корректное значение')
    else:
        if choice == '1':
            try:
                with open('chat.txt', 'r', encoding='utf-8') as file:
                    for line in file:
                        print(line + '\n')
            except FileNotFoundError:
                print('История сообщений пуста')
        elif choice == '2':
            try:
                with open('chat.txt', 'a', encoding='utf-8') as file:
                    message = input('Введите сообщение: ')
                    file.write(user + ': ' + message + '\n')
            except Exception:
                print('Ошибка записи в файл')


