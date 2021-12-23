
'''we dont use this because the time complexity of this solution based on tail is O(n)
    so we instead use stack implementation using head which is more efficient and time complexity is O(1)'''

class Node:
    __slots__ = '_elements','_next'
    def __init__(self, ele, next = None):
        self._element = ele
        self._next = next


class Stack_linked_list:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def top(self):
        if self.isEmpty():
            print('stack is empty')
            return
        p = self._tail
        e = p._element
        return e

    def push(self,ele):
        newest = Node(ele)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest

        self._size += 1

    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return
        p = self._head
        i = 1
        while i < len(self)-1:
            p = p._next
            i += 1
        
        self._tail = p
        if len(self) == 1:
            e = p._element
            self._head == None
            self._tail == None
            self._size -= 1
            return e
        else:
            p = p._next
            e = p._element
            self._tail._next = None
            self._size -= 1
        
        return e

    # def display(self):
    #     p = self._head
    #     while p:
    #         print(p._element, end='-->')
    #         p = p._next
    #     print()

s = Stack_linked_list()
s.push(10)
s.push(20)
print(len(s))
print(s.pop())
print(s.isEmpty())
print(s.pop())
print(s.isEmpty())
s.push(30)
s.push(40)
print(s.top())
s.push(50)
print(len(s))
print(s.pop())
s.push(60)
s.push(70)
s.display()
print(s.top())


            




