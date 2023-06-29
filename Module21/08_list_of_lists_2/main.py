nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def reclist(nice_list):
    result = []
    for element in nice_list:
        if type(element) != list:
            result.append(element)
        else:
            result.extend(reclist(element))
    return(result)

print('Ответ: ', reclist(nice_list))