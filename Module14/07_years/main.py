def three_same_numbers (first_year, second_year):
    for i in range(first_year, second_year + 1):
        for f in range (10):
            i = str(i)
            f = str(f)
            if i.count(f) == 3:
                print(i)


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

three_same_numbers (first_year, second_year)