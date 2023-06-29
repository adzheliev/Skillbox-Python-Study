initial = open('zen.txt', 'r')

mylist = []
for line in initial:
    mylist.append(line)

finallist = []
for line in mylist[::-1]:
    print(line, end='')

initial.close()
