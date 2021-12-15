class Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, next = None, prev = None):
        self._element = element
        self._next = next
        self._prev = prev

class Doubly_Linked_List:
    def __init__(self) -> None:
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
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

    def add_first(self, ele):
        newest = Node(ele)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def add_any(self, ele, position):
        newest = Node(ele)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest  
        newest._prev = p
        self._size += 1

    def remove_first(self):
        if self.isEmpty():
            print('list is empty')
            return
        
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e

    def remove_last(self):
        if self.isEmpty():
            print('list is empty')
            return
       
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
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
        p._next._prev = p
        self._size -= 1
        return e


    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next 
        print()

    def display_rev(self):
        q = self._tail          #reverse order
        while q:
            print(q._element, end='-->')
            q = q._prev 
        print()
            


L = Doubly_Linked_List()

# L.add_last(5)

L.add_first(6)
# L.add_first(7)
# L.add_last(4)

# L.add_first(8)
# L.add_last(3)

# L.add_first(9)
# L.add_last(2)

# L.add_first(0)
# L.add_last(1)
# L.add_any(10,2)
# L.display()
# el1 = L.remove_any(2)
# print('deleted element', el1)



L.display()
print(len(L))

L.remove_first()
L.display()
