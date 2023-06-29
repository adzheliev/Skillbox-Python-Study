initial = open('first_tour.txt', 'r')
file = open('second_tour.txt', 'a')
linelist = []

for line in initial:
    linelist.append(line.rstrip())

k = int(linelist[0])
linelist.remove(str(k))

secondtourlist = []
partecipantscount = 0
for element in linelist:
    partecipant = element.split()
    if int(partecipant[2]) > k:
        secondtourlist.append(partecipant)
        partecipantscount += 1

secondtourlist = sorted(secondtourlist, key=lambda partecipant: partecipant[2], reverse=True)

print(secondtourlist)
file.write(str(partecipantscount))
file.write('\n')
partecipantnumber = 1
for element in secondtourlist:
    wordslist = [str(partecipantnumber) + ')', element[1][0] + '.', element[0], element[2], '\n']
    finaltext = ' '.join(wordslist)
    file.write(finaltext)
    partecipantnumber += 1

initial.close()
file.close()

