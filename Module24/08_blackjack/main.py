import random


class Card:

    def __init__(self, other):
        self.name = other[0]
        self.points = other[1]

    def return_name(self):
        return self.name

    def return_value(self):
        return self.points


class Deck:

    def __init__(self):
        self.deck = {
        ('Десятка', 'Червы'): 10, ('Десятка', 'Бубны'): 10, ('Десятка', 'Крести'): 10, ('Десятка', 'Пики'): 10,
        ('Девятка', 'Червы'): 9, ('Девятка', 'Бубны'): 9, ('Девятка', 'Крести'): 9, ('Девятка', 'Пики'): 9,
        ('Восьмёрка', 'Червы'): 8, ('Восьмёрка', 'Бубны'): 8, ('Восьмёрка', 'Крести'): 8, ('Восьмёрка', 'Пики'): 8,
        ('Семёрка', 'Червы'): 7, ('Семёрка', 'Бубны'): 7, ('Семёрка', 'Крести'): 7, ('Семёрка', 'Пики'): 7,
        ('Шестёрка', 'Червы'): 6, ('Шестёрка', 'Бубны'): 6, ('Шестёрка', 'Крести'): 6, ('Шестёрка', 'Пики'): 6,
        ('Пятёрка', 'Червы'): 5, ('Пятёрка', 'Бубны'): 5, ('Пятёрка', 'Крести'): 5, ('Пятёрка', 'Пики'): 5,
        ('Четвёртка', 'Червы'): 4, ('Четвёртка', 'Бубны'): 4, ('Четвёртка', 'Крести'): 4, ('Четвёртка', 'Пики'): 4,
        ('Тройка', 'Червы'): 3, ('Тройка', 'Бубны'): 3, ('Тройка', 'Крести'): 3, ('Тройка', 'Пики'): 3,
        ('Двойка', 'Червы'): 2, ('Двойка', 'Бубны'): 2, ('Двойка', 'Крести'): 2, ('Двойка', 'Пики'): 2,
        ('Валет', 'Червы'): 10, ('Валет', 'Бубны'): 10, ('Валет', 'Крести'): 10, ('Валет', 'Пики'): 10,
        ('Дама', 'Червы'): 10, ('Дама', 'Бубны'): 10, ('Дама', 'Крести'): 10, ('Дама', 'Пики'): 10,
        ('Король', 'Червы'): 10, ('Король', 'Бубны'): 10, ('Король', 'Крести'): 3, ('Король', 'Пики'): 3,
        ('Туз', 'Червы'): 11, ('Туз', 'Бубны'): 11, ('Туз', 'Крести'): 11, ('Туз', 'Пики'): 11
    }

    def return_random_card(self):
        random_card = tuple(random.choice(list(self.deck.items())))
        del self.deck[random_card[0]]
        return random_card


class Player:

    def __init__(self, name='Kostia', cards=None):
        self.name = name
        self.cards = []

    def request_card(self, deck):
        self.cards.append(deck.return_random_card())

    def return_all_points(self):
        total_points = 0
        for card in self.cards:
            total_points += card[1]
        return total_points


class Diler(Player):

    def card_for_diler(self, deck):
        choice = random.randint(1, 2)
        if choice == 1:
            self.cards.append(deck.return_random_card())
            return self.return_all_points()
        elif choice == 2:
            return self.return_all_points()


deck = Deck()
kostia = Player(name='Костя')
diler = Diler(name='Дилер')

kostia.request_card(deck)
kostia.request_card(deck)
diler.request_card(deck)
diler.request_card(deck)


diler_points = diler.card_for_diler(deck)

while True:
    choice = input('Возьмёшь карту: 1 - ДА, 2 - НЕТ: ')
    if choice == '1':
        kostia.request_card(deck)
    elif choice == '2':
        kostia_points = kostia.return_all_points()
        break

print('У Кости {} очков'.format(kostia_points))
print('У Диллера {} очков'.format(diler_points))

if diler_points <= 21 and kostia_points <= 21:
    if diler_points > kostia_points:
        print('Дилер выиграл')
    elif diler_points < kostia_points:
        print('Костя выиграл')
    else:
        print('Ничья')
elif diler_points > 21 and kostia_points < 21:
    print('Костя выиграл')
elif kostia_points > 21 and diler_points < 21:
    print('Дилер выиграл')
elif diler_points > 21 and kostia_points > 21:
    print('Никто не выиграл')




