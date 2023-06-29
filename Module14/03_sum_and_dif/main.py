def numbers_sum (N):
    number_summ = 0
    while N > 0:
        number = N % 10
        number_summ += number
        N //= 10

    return number_summ


def number_len (N):
    quantity = len(str(N))

    return quantity


N = int(input('Введите число: '))

numbers_sum(N)
number_len(N)

summa = numbers_sum (N)
count = number_len (N)
diff = abs(numbers_sum (N) - number_len (N))

print('Сумма чисел: ', summa)
print('Количество цифр в числе', count)
print('Разность суммы и количества цифр ', diff)




