from collections import Counter
import os

initial = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')
text = initial.read()

totalletters = 0
totalwords = 1
totalstring = 1
lettercount = Counter()

for sym in text.lower():
    if sym.isalpha():
        totalletters += 1
        lettercount.update(sym)
    if sym == ' ':
        totalwords += 1
    if sym == '\n':
        totalstring += 1
rare_letter = min(lettercount, key=lettercount.get)

print('Количество букв в файле:', totalletters)
print('Количество слов в файле:', totalwords)
print('Количество строк в файле:', totalstring)
print('Самая редкая буква:', rare_letter)

initial.close()


