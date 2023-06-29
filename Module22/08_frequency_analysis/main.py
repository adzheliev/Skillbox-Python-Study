import operator

initial = open('text.txt', 'r')
file = open('analysis.txt', 'a')

alfavit = 'abcdefghijklmnopqrstuvwxyz'
lettersdict = {}
lensym = 0


for line in initial:
    for sym in line:
        if sym.lower() in alfavit:
            lensym += 1
            if sym.lower() in lettersdict:
                lettersdict[sym.lower()] += 1
            else:
                lettersdict[sym.lower()] = 1

finaldict = {}

for index, value in lettersdict.items():
    finaldict[index] = round(value / lensym, 3)

finallist = sorted(finaldict.items(), key=operator.itemgetter(1, 0), reverse=True)
for element in finallist:
    string = str(element[0]) + ' ' + str(element[1]) + '\n'
    file.write(string)

initial.close()
file.close()
