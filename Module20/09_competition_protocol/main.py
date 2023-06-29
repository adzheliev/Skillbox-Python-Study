N = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')

partecipants = {}
for i in range(1, N + 1):
    print(i,'-я запись: ', end='')
    score, name = input().split()
    score = int(score)
    if name in partecipants:
        if score > partecipants[name][0]:
            partecipants[name][0] = score
            partecipants[name][1] = i
    else:
        partecipants[name] = [score, i]

records = sorted(partecipants.items(),
                 key=lambda x: (x[1][0], -x[1][1]),
                 reverse=True)
for i in range(3):
    print(i+1,'-e место', records[i][0], records[i][1][0])

