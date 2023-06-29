class Student:

    def __init__(self, name = '', group = 0, votes = []):
        self.name = name
        self.group = group
        self.votes = votes

    def __str__(self):
        return f'Studend {self.name} in group {self.group} has votes {self.votes}'

allstudents = []
for i_student in range(2):
    student = Student()
    student.name = input('Введите имя студента: ')
    student.group = int(input('Введите группу, к которой принадлежит студент: '))
    student.votes = list(map(int, input('Введите оценки через пробел: ').split()))
    allstudents.append(student)

allstudents = sorted(allstudents, key=lambda student: sum(student.votes) / len(student.votes))
for i_student in allstudents:
    print(i_student.__str__())
    print()
