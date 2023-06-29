class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calculate_salary(self):
        pass

class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000

    def calculate_salary(self):
        return self.salary

class Agent(Employee):

    def __init__(self, name, surname, age, salesvolume):
        super().__init__(name, surname, age)
        self.salesvolume = salesvolume
        self.fixpay = 5000

    def calculate_salary(self):
        return self.fixpay + (self.salesvolume / 100 * 5)

class Worker(Employee):

    def __init__(self, name, surname, age, hours_quantity):
        super().__init__(name, surname, age)
        self.hours_quantity = hours_quantity

    def calculate_salary(self):
        return self.hours_quantity * 100

manager1 = Manager(name='Tom', surname='Cruise', age=60)
manager2 = Manager(name='Julia', surname='Roberts', age=44)
manager3 = Manager(name='Lady', surname='Gaga', age=35)

agent1 = Agent(name='Steeve', surname='Jobs', age=70, salesvolume=340000)
agent2 = Agent(name='Elon', surname='Musk', age=48, salesvolume=500000)
agent3 = Agent(name='John', surname='Besos', age=66, salesvolume=500000)

worker1 = Worker(name='Ivan', surname='Shakmeev', age=28, hours_quantity=0)
worker2 = Worker(name='Alan', surname='Dzheliev', age=38, hours_quantity=160)
worker3 = Worker(name='Tania', surname='Shakmeeva', age=23, hours_quantity=20)

print(manager1.calculate_salary())
print(manager2.calculate_salary())
print(manager3.calculate_salary())
print(agent1.calculate_salary())
print(agent2.calculate_salary())
print(agent3.calculate_salary())
print(worker1.calculate_salary())
print(worker2.calculate_salary())
print(worker3.calculate_salary())