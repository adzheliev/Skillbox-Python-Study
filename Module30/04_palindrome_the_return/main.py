import collections


def can_be_poly(string:str) -> bool:
    letters_count = collections.Counter()
    for letter in string:
        letters_count[letter] += 1
    result = 0
    for element, value in letters_count.items():
        if value % 2 != 0:
            result += 1
    if result > 1:
        return False
    else:
        return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

