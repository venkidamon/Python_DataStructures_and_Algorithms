class _Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next

class DEQue_linked:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add_first(self, element):
        newest = _Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def add_last(self, element):
        newest = _Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def remove_first(self):
        if self.isEmpty():
            print('DEQue is Empty')
            return 
        else:
            e = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return e
    
    def remove_last(self):
        if self.isEmpty():
            print('DEQue is Empty')
            return
        else:
            p = self._head
            i = 1
            while i < len(self) - 1:
                p = p._next
                i += 1
            self._tail = p
            if len(self) == 1:
                e = p._element
                self._head = None
                self._tail = None
                self._size -= 1
                return e
            else:
                p = p._next
                e = p._element
                self._tail._next = None
                self._size -= 1
                return e

    def first(self):
        if self.isEmpty():
            print('DEQue is Empty')
            return
        else:
            return self._head._element

    def last(self):
        if self.isEmpty():
            print('DEQue is Empty')
            return
        else:
            return self._tail._element

    def display(self):
        p = self._head
        while p:
            print(p._element, end = '-->')
            p = p._next
        print()

d = DEQue_linked()
d.add_first(1)
d.add_last(2)
d.add_last(3)
print(d.first(), end='--------')
print(d.last())
d.add_first(4)
d.add_first(5)
d.add_last(6)
print(len(d))
d.display()
d.remove_first()
d.display()
print(len(d))
d.remove_last()
print(d.last())
print(len(d))
d.remove_last()
d.remove_last()
d.remove_last()
d.remove_last()
d.remove_last()
print(len(d))




