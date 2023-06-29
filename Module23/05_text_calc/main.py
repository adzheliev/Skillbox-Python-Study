def item_checker(line):
    try:
        items = line.split()
    except IndexError:
        pass
    if len(items) != 3:
        raise IndexError ('НЕ присутствуют все три поля: IndexError')
    else:
        if not firstoperand(items[0]):
            raise TypeError('Первый операнд должен быть числом')
        if not operation (items[1]):
            raise TypeError('Ошибка в поле операция. Допускаются только следующие операции (+, -, /, *, **, //, %)')
        if not secondoperand(items[2]):
            raise ValueError('Второй операнд должен быть числом и не должен равняться нулю')


def firstoperand(value):
    return value.isnumeric()


def operation(symbol):
    operations = ('+', '-', '/', '*', '**', '//', '%')
    return symbol in operations


def secondoperand(value):
    return value.isnumeric() and value != '0'

try:
    file = open('calc.txt', 'r')
except FileNotFoundError('Файл не найден'):
    pass
else:
    total = 0
    for line in file:
        try:
            string = item_checker(line)
        except Exception:
            print('Проверьте строку')
        else:
            result = 0
            items = line.split()
            if items[1] == '+':
                result = int(items[0]) + int(items[2])
            elif items[1] == '-':
                result = int(items[0]) - int(items[2])
            elif items[1] == '/':
                result = int(items[0]) / int(items[2])
            elif items[1] == '*':
                result = int(items[0]) * int(items[2])
            elif items[1] == '**':
                result = int(items[0]) ** int(items[2])
            elif items[1] == '//':
                result = int(items[0]) // int(items[2])
            elif items[1] == '%':
                result = int(items[0]) % int(items[2])
            total += result
file.close()
print('Результат вычислений', total)

