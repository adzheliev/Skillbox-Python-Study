class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_count(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_count(self):
        return self.worth / 1000

class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_count(self):
        return self.worth / 200

class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_count(self):
        return self.worth / 5000


total_money = int(input('Сколько у Вас денег всего: '))
app_price = int(input('Сколько стоит Ваша квартира: '))
car_price = int(input('Сколько стоит Ваша машина: '))
house_price = int(input('Сколько стоит Ваш дом: '))

appartment = Apartment(worth=app_price)
car = Car(worth=car_price)
house = CountryHouse(worth=house_price)

if total_money >= appartment.tax_count():
    print('Налог на квартиру составляет: ', round(appartment.tax_count(), 2))
else:
    print('Чтобы заплатить налог на квартиру не хватает: ', round(appartment.tax_count() - total_money), 2)

if total_money >= car.tax_count():
    print('Налог на машину составляет: ', round(car.tax_count(), 2))
else:
    print('Чтобы заплатить налог на машину не хватает: ', round(car.tax_count() - total_money), 2)

if total_money >= house.tax_count():
    print('Налог на дом составляет: ', round(house.tax_count(), 2))
else:
    print('Чтобы заплатить налог на квартиру не хватает: ', round(house.tax_count() - total_money), 2)