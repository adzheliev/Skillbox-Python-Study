from pprint import pprint
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def phonesale(copysite, phone):
    if 'title' in copysite:
        copysite['title'] = 'Куплю/продам {} недорого'.format(phone)
    if 'h2' in copysite:
        copysite['h2'] = 'У нас самая низкая цена на {}'.format(phone)
        return copysite

    for subdict in copysite.values():
        if type(subdict) == dict:
            result = phonesale(subdict, phone)
            if result:
                return copysite


n = int(input('Сколько сайтов: '))
copysite = copy.deepcopy(site)
for i in range(n):
    phone = input('Введите название продукта для нового сайта: ')
    print('Сайт для ', phone)
    pprint(phonesale(copysite, phone))