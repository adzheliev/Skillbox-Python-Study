import itertools

pin_numbers = [x for x in range(10)]

for item in itertools.permutations(pin_numbers, 4):
    print(item)