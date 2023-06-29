import os
from collections.abc import Iterable

def gen_files_path(path = '/') -> Iterable[tuple]:
    for dirpath, dirnames, filenames in os.walk(path):
        yield dirpath, dirnames, filenames


catalog = input('Укажите каталог: ')

for i in gen_files_path():
    if catalog in i[1]:
        print(os.path.join(i[0], catalog))
        break
    else:
        for dirname in i[1]:
            for filename in i[2]:
                print(os.path.join(i[0], dirname, filename))




