from typing import Callable
import functools

def debug(func:Callable) -> Callable:
    """Функция декоратор"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        args_str = [repr(a) for a in args]
        kwargs_str = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args_str = ', '.join(args_str + kwargs_str)

        print(f'Вызывается {func.__name__}({all_args_str})')
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула '{result}'")
        print(result)
        print()

        return result
    return inner


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)