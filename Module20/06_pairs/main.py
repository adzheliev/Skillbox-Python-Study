import random

original_list = random.sample(range(10),10)
endlist = list(zip(original_list[::2], original_list[1::2]))

print('Оригинальный список: ',original_list)
print('Новый список: ', endlist)