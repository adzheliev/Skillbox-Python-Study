class MyDict:

    def __init__(self, dict):
        self.dict = dict

    def get(self, key):
        if key not in self.dict:
            return 0
        else:
            return self.dict[key]

"""Экземпляры созданы для тестирования"""

a = MyDict(dict={'a':1, 'b':2, 'c':3})
print(a.get('n'))
print(a.get('b'))