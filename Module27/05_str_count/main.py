from typing import Callable
import functools

count = {}

def counter(func:Callable) -> Callable:
    """Функция декоратор, cчитающая вызовы функции"""
    count[func.__name__] = 0
    @functools.wraps(func)
    def inner(*args, **kwargs):
        count[func.__name__] += 1
        func(*args, **kwargs)
        print('Функция выполнилась {count} раз(а)'.format(count=count[func.__name__]))
    return inner


@counter
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)