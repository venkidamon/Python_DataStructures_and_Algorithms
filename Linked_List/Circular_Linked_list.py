class Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class Circular_LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add_last(self, ele):
        newest = Node(ele)
        if self.isEmpty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element)
            p = p._next
            i += 1
    





l = Circular_LinkedList()

l.add_last(5)
l.add_last(6)
l.add_last(7)
l.display()