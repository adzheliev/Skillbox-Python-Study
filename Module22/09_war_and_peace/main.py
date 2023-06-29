import zipfile
import operator

z = zipfile.ZipFile('voyna-i-mir.zip', 'r')
z.extractall()
initial = open('voyna-i-mir.txt', 'r')
file = open('result.txt', 'a')
lettersdict = {}

for line in initial:
    for sym in line:
        if sym.isalpha():
            if sym in lettersdict:
                lettersdict[sym] += 1
            else:
                lettersdict[sym] = 1

finallist = sorted(lettersdict.items(), key=operator.itemgetter(1), reverse=True)
print(finallist)
for element in finallist:
    string = str(element[0]) + ' ' + str(element[1]) + '\n'
    file.write(string)

initial.close()
file.close()


