import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_car_pattern = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
taxi_pattern = r"[АВЕКМНОРСТУХ]{2}\d{5,6}"

print('Список номеров частных автомобилей: ', re.findall(private_car_pattern, text))
print('Список номеров такси: ', re.findall(taxi_pattern, text))