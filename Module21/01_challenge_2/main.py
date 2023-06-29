def recnum(max, num = 1):
    print(num)
    if num == max:
        return
    return recnum(max, num + 1)


max = int(input('Введите num: '))
recnum(max)
