import random

class Warrior:
    def __init__(self, hp = 100):
        self.hp = hp

    def hit(self):
        self.hp -= 20

unit1 = Warrior()
unit2 = Warrior()

while unit1.hp != 0 and unit2.hp != 0:
    choice = random.randint(1, 2)
    if choice == 1:
        unit1.hit()
    elif choice == 2:
        unit2.hit()

if unit1.hp == 0:
    print('Юнит 2 одержал победу')
else:
    print('Юнит 1 одержал победу')

