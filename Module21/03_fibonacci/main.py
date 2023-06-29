def fib(num):
    if num < 2:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: ', fib(num))