def divider (n):
    number_divider = 1
    while number_divider <= n:
        number_divider += 1
        if n % number_divider == 0:
            break
    return number_divider


n = int(input('Введите число: '))

divider (n)
divider = divider (n)

print('Наименьший делитель, отличный от единицы: ',divider)