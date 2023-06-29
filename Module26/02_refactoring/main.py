from collections.abc import Iterable

def find_number(list_1:list, list_2:list, to_find:int) -> Iterable[str]:

    for x in list_1:
        for y in list_2:
            result = x * y
            if result == to_find:
                string = f'Found!!! {x} x {y} = {result}'
                yield string


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for i in find_number(list_1=list_1, list_2=list_2, to_find=to_find):
    print(i)

