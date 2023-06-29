def decode(line, step):
    codedword = ''
    for sym in line:
        if sym in upperletters:
            symindex = upperletters.index(sym)
            codedsym = upperletters[symindex + step]
            codedword = codedword + codedsym
        elif sym in lowerletters:
            symindex = lowerletters.index(sym)
            codedsym = lowerletters[symindex + step]
            codedword = codedword + codedsym
    return codedword


initial = open('text.txt', 'r')
file = open('cipher_text.txt', 'a')
upperletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerletters = 'abcdefghijklmnopqrstuvwxyz'

step = 1
for line in initial:
    file.write(decode(line, step))
    step += 1
    file.write('\n')

initial.close()
file.close()
