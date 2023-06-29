import random

total_earned = 0
total_eaten = 0
total_fur_coats = 0

class Person:
    def __init__(self, name, satiation = 30, happyness = 100):
        self.name = name
        self.satiation = satiation
        self.happyness = happyness

    def pat_cat(self):
        self.happyness += 5

class Husband(Person):

    def __init__(self, name, satiation=30, happyness=100):
        super().__init__(name, satiation, happyness)

    def eat(self, how_mach_food):
        if house.food > how_mach_food:
            self.satiation += how_mach_food
            house.food -= how_mach_food

    def play(self):
        self.satiation -= 10
        self.happyness += 20

    def work(self):
        self.satiation -= 10
        house.money += 150


class Wife(Person):

    def __init__(self, name, satiation = 30, happyness = 100):
        super().__init__(name, satiation, happyness)

    def eat(self, how_mach_food):
        if house.food > how_mach_food:
            self.satiation += how_mach_food
            house.food -= how_mach_food

    def buy_food(self, value):
        if house.money > value:
            self.satiation -= 10
            house.money -= value
            house.food += value

    def buy_cat_food(self, value):
        if house.money > value:
            self.satiation -= 10
            house.money -= value
            house.cat_food += value

    def buy_fur_coat(self):
        if house.money > 350:
            self.satiation -= 10
            house.money -= 350
            self.happyness += 60

    def clean_house(self):
        self.satiation -= 10
        house.dirt -= 100

class Cat:

    def __init__(self, name, satiation = 30):
        self.name = name
        self.satiation = satiation

    def eat(self, how_mach_food):
        if house.cat_food > how_mach_food:
            self.satiation += (how_mach_food * 2)
            house.cat_food -= how_mach_food

    def sleep(self):
        self.satiation -= 10

    def tear_wallpaper(self):
        self.satiation -= 10
        house.dirt += 5

class House:

    def __init__(self, money = 100, food = 50, cat_food = 30, dirt = 0):
        self.money = money
        self.food = food
        self.cat_food = cat_food
        self.dirt = dirt

house = House()
wife = Wife(name='Яна')
husband = Husband(name='Алан')
cat = Cat(name='Барсик')

husband_actions = ['pat_cat', 'eat', 'play', 'work']
wife_actions = ['pat_cat', 'eat', 'buy_food', 'buy_cat_food', 'buy_fur_coat', 'clean_house']
cat_actions = ['eat', 'sleep', 'tear_wallpaper']

for i in range (365):
    if husband.satiation <= 0:
        food = (random.randint(1, 30))
        husband.eat(food)
        total_eaten += food

    if wife.satiation <= 0:
        food = (random.randint(1, 30))
        wife.eat(food)
        total_eaten += food

    if cat.satiation <= 0:
        food = (random.randint(1, 10))
        cat.eat(food)
        total_eaten += food

    house.dirt += 5

    if house.dirt > 90:
        husband.happyness -= 10
        wife.happyness -= 10

    if husband.happyness < 10:
        husband.pat_cat()

    if wife.happyness < 10:
        wife.pat_cat()

    husband_choice = random.choice(husband_actions)
    wife_choice = random.choice(wife_actions)
    cat_choice = random.choice(cat_actions)

    if husband_choice == 'pat_cat':
        husband.pat_cat()
    elif husband_choice == 'eat':
        food = (random.randint(1, 30))
        husband.eat(food)
        total_eaten += food
    elif husband_choice == 'play':
        husband.play()
    elif husband_choice == 'work':
        husband.work()
        total_earned += 150
    else:
        pass

    if wife_choice == 'pat_cat':
        wife.pat_cat()
    elif wife_choice == 'eat':
        food = (random.randint(1, 30))
        wife.eat(food)
        total_eaten += food
    elif wife_choice == 'buy_food':
        wife.buy_food(random.randint(1, 30))
    elif wife_choice == 'buy_cat_food':
        wife.buy_cat_food(random.randint(1, 10))
    elif wife_choice == 'buy_fur_coat':
        wife.buy_fur_coat()
        total_fur_coats += 1
    elif wife_choice == 'clean_house':
        wife.clean_house()
    else:
        pass

    if cat_choice == 'eat':
        food = (random.randint(1, 10))
        cat.eat(food)
        total_eaten += food
    elif cat_choice == 'sleep':
        cat.sleep()
    elif cat_choice == 'tear_wallpaper':
        cat.tear_wallpaper()
    else:
        pass

print('За год было заработано: ', total_earned)
print('За год было съедено: ', total_eaten)
print('За год было куплено {} шуб'.format(total_fur_coats))





