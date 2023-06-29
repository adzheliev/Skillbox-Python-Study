class LinkedList:

    leght = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f'[{self.data}] -> {self.next}'

    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def append(self, value):
        if not self.head:
            self.head = self.Node(value)
            self.leght += 1
            return value
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = self.Node(value)
            self.leght += 1
            return value


    def get(self, index):
        self.index = index
        i = 0
        node = self.head
        while i < self.index:
            node = node.next
            i += 1
        return node.data


    def remove(self, index):
        self.index = index
        if self.index == 0:
            self.head = self.head.next
        i = 0
        node = self.head
        prev_node = node
        while i < self.index:
            prev_node = node
            node = node.next
            i += 1
        prev_node.next = node.next
        element = node.data
        del node
        return element


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
