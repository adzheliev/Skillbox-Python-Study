import functools
from typing import Callable

def check_permission(permission: str = 'admin') -> Callable:
    def internal_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if permission not in user_permissions:
                raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию {func}'.format(func=func.__name__))
            return func(*args, **kwargs)
        return wrapped
    return internal_func


user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()