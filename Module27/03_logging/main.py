from typing import Callable
import functools
import datetime


def logging(func: Callable) -> Callable:
    """Декоратор выводи имя и документацию обрабатываемой функции и логирует её ошибки"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('Название функции:\n', func.__name__)
        print('Документация функции:\n', func.__doc__)
        try:
            func(*args, **kwargs)
        except Exception as error:
            with open('function_errors.log', 'a') as file:
                file.write('В функции {funcname} в {date} произошла ошибка {error}\n'.format(
                    funcname=func.__name__,
                    date = datetime.datetime.now(),
                    error=error)
                )
    return inner


@logging
def test() -> None:
    """Внутренняя функция для демонстрации работы декоратора"""
    print('<Тут что-то происходит...>', b)

test()