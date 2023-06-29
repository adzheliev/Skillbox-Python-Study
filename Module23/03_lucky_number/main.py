import random

total = 0
randomallert = [ValueError, TypeError, ZeroDivisionError, FileNotFoundError, EncodingWarning, FileExistsError, AttributeError, ImportError, ArithmeticError, AssertionError, StopIteration, NameError, TimeoutError]
while total < 777:
    number = int(input('Введите число: '))
    with open('out_file.txt', 'a') as file:
        if random.randint(1, 13) == 6:
            raise random.choice(randomallert)('Вас постигла неудача!')
        else:
            file.write(str(number))
            file.write('\n')
            total += number
print('Вы успешно выполнили условие для выхода из порочного цикла!')


