import random

class Life:

    def __init__(self, total_carma = 500):
        self.total_carma = total_carma

    def one_day(self):
        ona_day_carma = random.randint(1, 7)
        badchoice = random.randint(1, 10)
        if badchoice == 5:
            with open('karma.log', 'a') as file:
                errorlist = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError','DepressionError']
                logerror = random.choice(errorlist)
                file.write(logerror + '\n')
        return ona_day_carma

mylife = Life()
gaincarma = 0

while gaincarma < mylife.total_carma:
    gaincarma += mylife.one_day()