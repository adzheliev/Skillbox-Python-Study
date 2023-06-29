from typing import Callable
import functools
import time

def how_are_you(func: Callable) -> Callable:
    """Бесполезный декоратор  с задержкой выполнения декорируемой функции"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        a = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        time.sleep(7)
        func(*args, **kwargs)
    return inner


@how_are_you
def test() -> None:
    """Внутренняя функция для демонстрации работы декоратора"""
    print('<Тут что-то происходит...>')

test()