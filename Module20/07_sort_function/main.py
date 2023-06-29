import math

def tpl_sort(sequence):
    for i in list(sequence):
        if not str((abs(i))).isnumeric():
            return set(sequence)
        else:
            return tuple(sorted(sequence))


#sequence = (6, 3, -1, 8, 4, 10, -5)
#print(tpl_sort(sequence))

