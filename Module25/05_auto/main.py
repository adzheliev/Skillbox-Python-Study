import math

class Car:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, km):
        self.x = self.x + km * math.cos(self.direction)
        self.y = self.y + km * math.sin(self.direction)

    def turn(self, direction):
        self.direction = direction

class Bus(Car):

    def __init__(self, x, y, direction, passagers, money = 0):
        super().__init__(x, y, direction)
        self.passagers = passagers
        self.money = money

    def passagers_in(self, value):
        self.passagers = value

    def passagers_out(self, value):
        if self.passagers >= value:
            self.passagers -= value
        else:
            print('В автобусе всего {} пассажиров'.format(self.passagers))

    def move(self, km):
        super().move(self, km)
        self.money += self.passagers * km * 10

