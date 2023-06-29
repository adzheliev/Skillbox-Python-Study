import sympy

def crypto(data):
    result = []
    if isinstance(data, dict):
        data = data.items()
    for index, value in enumerate(data):
        if sympy.isprime(index):
            result.append(value)
    return result


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
