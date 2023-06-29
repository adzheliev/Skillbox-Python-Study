def item_checker(line):
    try:
        items = line.split()
    except IndexError:
        pass
    if len(items) != 3:
        raise IndexError ('НЕ присутствуют все три поля: IndexError')
    else:
        if not namecheck(items[0]):
            raise NameError('Поле имени содержит НЕ только буквы')
        if not emailcheck(items[1]):
            raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
        if not agecheck(items[2]):
            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


def namecheck(name):
    return name.isalpha()


def emailcheck(email):
    return  '.'  and '@' in email


def agecheck(age):
    return age.isnumeric() and 10 < int(age) < 99


goodfile = open('registrations_good.log', 'a', encoding='utf-8')
badfile = open('registrations_bad.log', 'a', encoding='utf-8')

with open('registrations.txt', 'r', encoding='utf-8') as initial:
    for line in initial:
        try:
            string = item_checker(line)
        except IndexError:
            badfile.write(line + ' НЕ присутствуют все три поля: IndexError.' + '\n')
        except NameError:
            badfile.write(line + ' Поле имени содержит НЕ только буквы: NameError' + '\n')
        except SyntaxError:
            badfile.write(line + ' Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError' + '\n')
        except ValueError:
            badfile.write(line + ' Поле «Возраст» НЕ является числом от 10 до 99: ValueError' + '\n')
        else:
            goodfile.write(line + '\n')

goodfile.close()
badfile.close()