def first_number_reverse(N):
    fraction = round((N % 1) * 100)
    integer = int(N // 1)
    reverse_integer = str(integer)
    reverse_integer = reverse_integer[::-1]
    reverse_fraction = str(fraction)
    reverse_fraction = reverse_fraction[::-1]
    reverse_number = int(reverse_integer) + float(reverse_fraction)/100
    return reverse_number


def second_number_reverse(K):
    fraction = round((K % 1) * 100)
    integer = int(K // 1)
    reverse_integer = str(integer)
    reverse_integer = reverse_integer[::-1]
    reverse_fraction = str(fraction)
    reverse_fraction = reverse_fraction[::-1]
    reverse_number = int(reverse_integer) + float(reverse_fraction)/100
    return reverse_number


N = float(input('Введите первое число: '))
K = float(input('Введите второе число: '))

first_number_reverse(N)
second_number_reverse(K)

first_number = first_number_reverse(N)
second_number = second_number_reverse(K)

print('Первое число наоборот: ', first_number)
print('Второе число наоборот: ', second_number)
print('Сумма: ', first_number + second_number)



