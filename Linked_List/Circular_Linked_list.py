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
    
    def add_first(self, ele):
        newest = Node(ele)
        if self.isEmpty():
            newest._next = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        
        self._head = newest
        self._size += 1

    def add_any(self, ele, position):
        newest = Node(ele)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def remove_first(self):
        if self.isEmpty():
            print('list is empty')
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1  
        if self.isEmpty():
            self._head = None
            self._tail = None
        return e

    def remove_last(self):
        if self.isEmpty():
            print('list is empty')
            return
        p = self._head
        i = 1
        while i < len(self)-1:
            p = p._next
            i += 1
        self._tail = p
        e = p._next._element
        self._tail._next = self._head
        self._size -= 1
        return e

    
    def remove_any(self, position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e
        

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()






l = Circular_LinkedList()
l.add_first(27)
l.add_last(5)
l.add_last(6)
l.add_last(7)
l.add_first(1)
l.add_any(7,3)
l.add_any(1,3)
l.display()
l.remove_first()
r = l.remove_last()

print(r)
l.display()
k = l.remove_last()
l.display()

l.remove_any(2)
l.display()
print(len(l))
