import os
import glob
from collections.abc import Iterable

def linecount(path = os.path.abspath(os.curdir)) -> Iterable[str]:
    for filename in glob.glob(os.path.join(path)):
        if filename.endswith('.py'):
            with open (filename, 'r') as file:
                for line in file:
                    yield line


path = input('Введите директорию:')

count = 0
for line in linecount(path=path):
    if not line and line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
        pass
    else:
        count += 1

print('Общее количество строк кода в директории составляет: ', count)

