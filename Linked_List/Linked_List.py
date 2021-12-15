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
        '''this function add the new element based on the position defined the newest element next is assigned 
        first and then previous element next is assigned to the newest element'''
        newest = _Node(ele)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def remove_first(self):
        '''This function deletes the first element of the linked list and the next element is assigned as head
        if no element is present both head and tail are set to None'''
        if self.isEmpty():
            print('List is Empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e

    def remove_last(self):
        '''This function deletes the last element of the linked list and the previous element is assigned as new tail'''
        if self.isEmpty():
            print('List is Empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        return e


    def remove_any(self, position):
        '''This function remove any element between the linked list'''
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

L.add_any(56,2)


L.remove_last()
L.display()
print(len(L))

e = L.remove_any(3)
L.display()
print(len(L))

print(e)

