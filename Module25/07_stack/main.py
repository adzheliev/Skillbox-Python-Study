class Stack:

    count = 1

    def __init__(self):
        self.booklist = {}

    def add(self, book):
        self.booklist[self.count] = book
        self.count += 1

    def delete(self):
        del self.booklist[self.count]
        self.count -= 1

class TaskManager:

    def __init__(self):
        self.taskslist = {}

    def __str__(self):
        finallist = sorted(self.taskslist.items())
        final = ''
        for i in finallist:
            element = str(i[0]) + '\t' + i[1]
            final += element + '\n'
        return final


    def new_task(self, task, priority):
        if priority not in self.taskslist:
            self.taskslist[priority] = task
        else:
            key_to_add_value = self.taskslist.get(priority)
            self.taskslist[priority] = key_to_add_value + ', ' + task

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)







