def slicer(posl, number):
    posl = list(posl)
    if posl.count(number) >= 2:
        initial = posl.index(number)
        final = posl.index(number, initial + 1)
        return tuple(posl[initial:final+1])
    elif posl.count(number) == 1:
        initial = posl.index(number)
        return tuple(posl[initial::])
    else:
        return None


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
