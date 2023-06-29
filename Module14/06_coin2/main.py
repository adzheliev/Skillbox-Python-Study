def coin(x, y, r):
    if (x ** 2 + y ** 2) ** 0.5 <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

coin(x, y, r)