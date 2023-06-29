class Parent:

    def __init__(self, parentname = '', parentage = 0, childlist = []):
        self.parentname = parentname
        self.parentage = parentage
        self.childlist = childlist

    def info(self):
        print(f"I'm {self.parentname}, and I'm {self.parentage} years old and have {len(self.childlist)} children: ", end='')
        children = []
        for i_child in self.childlist:
            children.append(i_child.child_info())
        children = ', '.join(children)
        print(children)

    def calm(self, child):
        if child in self.childlist and child.calm == False:
            child.calm_down()

    def feed(self, child):
        if child in self.childlist and child.hunger == True:
            child.eat()

    def add_child(self, child):
        self.childlist.append(child)

class Child:

    def __init__(self, childname = '', childage = 0, calm = False, hunger = True):
        self.name = childname
        self.age = childage
        self.calm = calm
        self.hunger = hunger

    def child_info(self):
        return self.name

    def calm_down(self):
        if self.calm == False:
            print("I'm calm")
            self.calm == True


    def eat(self):
        if self.hunger == True:
            print("I'm not hungry")
            self.hunger == False


child1 = Child(childname ='Demid', childage = 3)
child2 = Child(childname ='Mark', childage = 1)
father = Parent(parentname = 'Alan', parentage = 38, childlist = [child1, child2])

father.info()
father.feed(child1)
father.calm(child2)






