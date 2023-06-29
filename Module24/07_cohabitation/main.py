import random

class Person:

    def __init__(self, name, satiety = 50, house = True):
        self.name = name
        self.satiety = satiety
        self.house = house

    def eat(self):
        self.satiety += 50
        house.food -= 10

    def work(self):
        self.satiety -= 10
        house.money += 50

    def play(self):
        self.satiety -= 10

    def shop(self):
        self.house.add_food()
        self.house.take_away_money()


class House:

    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = money

    def add_food(self):
        self.food += 50

    def take_away_money(self):
        self.money -= 10


house = House()
artem = Person('Артём', house=house)
vasiliy = Person('Василий', house=house)


count = 0
for i in range(365):
    cube = random.randint(1, 6)
    person = random.choice([artem, vasiliy])
    if person.satiety < 0:
        print(f'Сожалею, но {person} скончался')
        break
    elif person.satiety < 20:
        person.eat()
    elif house.food < 10:
        person.shop()
    elif house.money < 50:
        person.work()
    elif cube == 1:
        person.work()
    elif cube == 2:
        person.eat()
    else:
        person.play()
    count += 1

if count == 364:
    print('Все выжили, всё супер')
else:
    print('Все RIP')



