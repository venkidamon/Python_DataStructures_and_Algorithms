#a1b4 --> abbbb
 
from email import header
from re import A
from unicodedata import numeric


class Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next

class Queue:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addLast(self, element):
        newest = Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def remove_first(self):
        if self.isEmpty():
            return "Empty"
        else:
            e = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.isEmpty():
                self._head = None
                self._tail = None
            return e

    def display(self):
        p = self._head
        while(p):
            print(self._head._element)
            p = p._next

    def top(self):
        return self._head._element
    

word = input()
q = Queue()
for x in word:
    q.addLast(x)


while q != None:
    y = q.remove_first()
    if(y == "Empty"):
        break
    if y.isalpha():
        char1 = y
        z = q.remove_first()
        if(z == "Empty"):
            break
        if z.isdigit():
            iter1 = z
            a = q.top()
            if(a == "Empty"):
                pass
            if a.isdigit():
                q.remove_first()
                if(a == "Empty"):
                    pass
                iter1 =z + a
        for i in range(int(iter1)):
            print(char1)
      
        
            


