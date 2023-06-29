import re

'''Закомментированный код реализует функцию ввода списка номеров пользователем, 
но для простоты тестирования взят готовый список'''

# phone_list = []
# N = int(input('Сколько номеров хотите проверить: '))
# for number in range(1, N+1):
#     print(f'Введите {number} номер: \n')
#     num_to_add = input()
#     phone_list.append(num_to_add)

phone_list = ['9999999999', '999999-999', '99999x9999']
pattern = r"[8,9]\d{9}"

count = 1
for phone_number in phone_list:
    result = re.match(pattern, phone_number)
    if result:
        print(f'{count} номер: всё в порядке')
    else:
        print(f'{count} номер: не подходит')
    count += 1

