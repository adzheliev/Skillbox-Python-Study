class Water:


    def __str__(self):
        return 'Вода'


    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, FithElement):
            return Lilu()
        else:
            return None

class Air:


    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lighitning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, FithElement):
            return Lilu()
        else:
            return None

class Fire:


    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lighitning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, FithElement):
            return Lilu()
        else:
            return None

class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, FithElement):
            return Lilu()
        else:
            return None

class FithElement:


    def __str__(self):
        return 'Пятый элемент'


    def __add__(self, other):
        if isinstance(other, Water):
            return Lilu()
        elif isinstance(other, Air):
            return Lilu()
        elif isinstance(other, Fire):
            return Lilu()
        elif isinstance(other, Earth):
            return Lilu()
        else:
            return None


class Storm():
    def __str__(self):
        return 'Шторм'


class Vapor():
    def __str__(self):
        return 'Пар'


class Dirt():
    def __str__(self):
        return 'Грязь'


class Lighitning():
    def __str__(self):
        return 'Молния'


class Dust():
    def __str__(self):
        return 'Пыль'


class Lava():
    def __str__(self):
        return 'Лава'


class Lilu():
    def __str__(self):
        return 'Лилу Даллас, мультипаспорт'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
fithelement = FithElement()
print(air + fire)
