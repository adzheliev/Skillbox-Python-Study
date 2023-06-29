import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as file2:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                print("Что-то пошло не так с первой функцией")
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                print("Что-то пошло не так со второй функцией")
            try:
                number = random.randint(0, 100)
                my_list = sorted([number, res1, res2])
                file2.write(' '.join(my_list))
            except Exception:
                print("Что-то пошло не так с записью в файл")
except (FileExistsError, FileNotFoundError, IsADirectoryError):
    print("Что-то пошло не так с открытием файла")




