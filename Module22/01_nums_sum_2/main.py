initial = open('numbers.txt', 'r')
total = 0
for line in initial:
    for sym in line:
        if sym.isnumeric():
            total += int(sym)

initial.close()

final = open('answer.txt', 'w')
final.write(str(total))
final.close()