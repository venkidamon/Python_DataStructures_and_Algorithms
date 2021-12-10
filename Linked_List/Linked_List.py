class _Node:
    __slots__ = '_element','_next'

    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class Linked_List:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''this function tells us about the size of the linked list'''
        return self._size

    def isEmpty(self):
        '''this function checks whether the linked list is empty or not returns boolean'''
        return self._size == 0

    def add_last(self, ele):
        '''this function add the new element to the last of the linked list 
        if elements are present else create a new one'''
        newest = _Node(ele)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_first(self, ele):
        '''this function add the new element to the first of the linked list 
        new element next is mapped to the head and then head is changed to the new element itself'''
        newest = _Node(ele)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def add_any(self, ele, position):
        '''this'''
        newest = _Node(ele)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1


    def display(self):
        '''This function is helpful in traversing the linked list'''
        p = self._head
        while p:
            print(p._element, end=' - ')
            p = p._next
        print()

    def search(self, key):
        '''This function search the key element in the linked list and 
        if it founds return the index of the key'''
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1


L = Linked_List()
L.add_last(4)
L.add_last(9)
L.add_last(3)
L.display()


L.add_first(15)
L.display()
print(len(L))
print(L.search(15))

L.add_any(56,1)
L.display()
print(len(L))
