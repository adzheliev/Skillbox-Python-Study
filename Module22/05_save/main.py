import os

def textredactor(text):
    dirlist = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    filename = input('Введите имя файла: ')
    filename = filename + '.txt'
    pathcheck = os.path.exists(os.path.join(os.path.sep.join(dirlist)))
    if pathcheck:
        path = os.path.join(os.path.sep.join(dirlist), filename)
        if os.path.exists(path):
            choice = input('Вы действительно хотите перезаписать файл? ').lower()
            if choice == 'да':
                file = open(path, 'w')
                file.write(text)
                file.close()
                print('Файл успешно перезаписан!')
        else:
            file = open(path, 'w')
            file.write(text)
            file.close()
            print('Файл успешно сохранён!')


text = input('Введите строку: ')

textredactor(text)


