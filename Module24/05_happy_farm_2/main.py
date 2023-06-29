class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        for potato in self.potatoes:
            if not potato.is_ripe():
                print('Картошка ещё не созрела!\n')
                return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()

class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def take_care(self):
        while not self.garden.are_all_ripe():
            self.garden.grow_all()

    def harvest(self):
        if self.garden.are_all_ripe():
            print('Картошка собрана!')
            self.garden.potatoes = []

    def plant(self):
        print('Снова сажаем!')
        self.garden.grow_all()

garden = PotatoGarden(5)
gardener = Gardener(name = 'Иван', garden=garden)
gardener.take_care()
gardener.harvest()
gardener.plant()


