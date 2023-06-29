mydict = {}

while True:
    print('Введите номер дейтвия')
    print('1. Добавить контакт')
    print('2. Найти человека')
    choice = int(input())
    if choice == 1:
        fio = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
        phonenumber = int(input('Введите номер телефона: '))
        mydict[tuple(fio)] = phonenumber
        print(mydict)
    elif choice == 2:
        find = input('Введите фамилию для поиска: ').capitalize()
        for person, number in mydict.items():
            if find in person:
                print(' '.join(person), number)
    else:
        print('Неверный ввод')

