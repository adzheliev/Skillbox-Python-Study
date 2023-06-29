import math

class Circle:


    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.r = r


    def area(self):
        S = math.pi * self.r ** 2
        return S


    def perimetr(self):
        P = 2 * math.pi * self.r
        return P


    def increase(self, K):
        increased = self.r * K
        return increased


    def interception(self, other):
        d = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if d > self.r + other.r:
            return True
        return False




