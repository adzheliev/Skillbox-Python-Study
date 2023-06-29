line_count = 0
sum_sym = 0
with open('people.txt', 'r', encoding='utf8') as initial, open('errors.log', 'w', encoding='utf8') as logfile:
    for line in initial:
        try:
            line_count += 1
            lenght = len(line)
            if line.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                raise BaseException ('Ошибка: менее трёх символов в строке {}'.format(line_count))
        except BaseException as exc:
            logfile.write(str(exc))
        finally:
            sum_sym += lenght
print('Общее количество символов: ', sum_sym)