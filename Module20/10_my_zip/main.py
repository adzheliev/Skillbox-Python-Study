string = 'abcd'
numbers = (10, 20, 30, 40)

if len(string) >= len(numbers):
    commonlen = len(numbers)
else:
    commonlen = len(string)

final = ((string[i], numbers[i]) for i in range(commonlen))

print(final)
for i in final:
    print(i)