from itertools import chain

def dict(students):
    ID_age = []
    interests = []
    string = ''
    for index, value in students.items():
        element = (index, value['age'])
        ID_age.append(element)
        interests.append(value['interests'])
        string += value['surname']
    return ID_age, interests, string


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

super = dict(students)
print(super)
print('Список пар "ID студента — возраст: ', super[0])
print(set(list(chain(*super[1]))))
print('Общая длина всех фамилий студентов: ', len(super[2]))
