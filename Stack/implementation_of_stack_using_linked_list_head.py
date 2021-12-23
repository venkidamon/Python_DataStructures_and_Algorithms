class _Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next

class Stack_linked:
    def __init__(self) -> None:
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, ele):
        newest = _Node(ele)
        if self.isEmpty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isEmpty():
            print('stack is empty')
            return
        e = self._top._element
        return e

    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

s = Stack_linked()
s.push(10)
s.push(20)
print(len(s))
print(s.pop())
print(s.isEmpty())
print(s.pop())
print(s.isEmpty())
s.display()

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
