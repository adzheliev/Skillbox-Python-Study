import functools
import time
from datetime import datetime
from typing import Callable

def logger(cls, func, dateformat:str = "b d Y - H:M:S") -> Callable:
    def wrapped(*args, **kwargs):
        if dateformat == "b d Y - H:M:S":
            print('Запускается {cls}.{funcname}, Дата и время запуска: {date}'.format(
                cls=cls.__name__,
                funcname=func.__name__,
                date=datetime.today().strftime("%b %d %Y - %H:%M:%S"))
            )
            start = time.time()
            result = func(*args, **kwargs)
            print('Завершение {cls}.{funcname}, время работы = {time}s'.format(
                cls=cls.__name__,
                funcname=func.__name__,
                time= round((time.time() - start), 3)
            )
            )
            return result
    return wrapped


def log_methods(dateformat:str = "b d Y - H:M:S") -> Callable:
    def wrapped(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                current_method = getattr(cls, method_name)
                decorated_method = logger(cls, current_method, dateformat)
                setattr(cls, method_name, decorated_method)
        return cls
    return wrapped


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()