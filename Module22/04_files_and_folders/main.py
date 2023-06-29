import os

path = input('Введите путь до каталога: ')
if os.path.exists(path):
    dirlist = os.listdir(path)

dircount = 0
filecount = 0
totalfiledimension = 0

for element in dirlist:
    item = os.path.join(path, element)
    if os.path.isdir(item):
        dircount += 1
    elif os.path.isfile(item):
        filecount += 1
        filedimension = os.path.getsize(item)
        totalfiledimension += filedimension

print(path)
print('Размер каталога (в Кб):', totalfiledimension / 1024)
print('Количество подкаталогов:', dircount)
print('Количество файлов:', filecount)

