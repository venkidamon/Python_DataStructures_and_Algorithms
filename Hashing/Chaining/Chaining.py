





class Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add_first(self, element):
        newest = Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def add_last(self, element):
        newest = Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def add_any(self, element, position):
        newest = Node(element)
        ind = 1
        p = self._head
        while ind < position - 1:
            p = p._next
            ind += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def remove_first(self):
        if self.isEmpty():
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
            return 
        else:
            p = self._head
            ind = 1
            while ind < len(self):
                p = p._next