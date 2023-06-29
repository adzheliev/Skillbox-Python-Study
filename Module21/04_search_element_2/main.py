site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search(datadict, dictkey, deep):
    count = 0
    if deep == 0:
        if dictkey in datadict:
            return datadict[dictkey]
        for key, value in datadict.items():
            if type(value) == dict:
                result = search(value, dictkey, deep)
                if result is not None:
                    return result
    elif deep > 0:
        count += 1
        if dictkey in datadict:
            return datadict[dictkey]
        while deep != count:
            count += 1
            for key, value in datadict.items():
                if type(value) == dict:
                    result = search(value, dictkey, deep)
                    if result is not None:
                        return result


dictkey = input('Введите искомый ключ: ')

while True:
    question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if question == 'y':
        deep = int(input('Введите максимальную глубину: '))
        break
    elif question != 'n':
        print('Ошибка ответа')
    else:
        deep = 0
        break


print('Значение ключа: ', search(site, dictkey, deep))