family = {'Джелиев Алан': 37,
          'Джелиева Яна': 29,
          'Джелиев Демид': 3,
          'Джелиев Марк': 1,
          'Шакмеев Иван': 28,
          'Шакмеева Татьяна': 24
}

request = input('Введите фамилию: ')
if request[-1] == 'а':
    request = request[:-1]
request1 = request + 'a'

for index, value in family.items():
    if request.capitalize() in index or request1.capitalize() in index:
        print(index, value)

