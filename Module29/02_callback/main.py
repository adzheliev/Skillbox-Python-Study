import functools
from typing import Callable


app = {}
def callback(path:str) -> Callable:
    def internal_func(func: Callable) -> Callable:
        app[path] = func
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            func(*args, **kwargs)
        return wrapped
    return internal_func


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')