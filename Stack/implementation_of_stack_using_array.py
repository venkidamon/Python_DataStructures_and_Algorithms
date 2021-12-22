


class Stack:
    def __init__(self):
        self._stack = []
        self._size = 0

    
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def top(self):
        if self.isEmpty():
            print('stack is empty')
            return
        return self._stack[len(self)-1]

    def push(self, ele):
        self._stack.append(ele)
        self._size += 1
    
    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return
        e = self._stack.pop()
        self._size -= 1
        return e
    def display(self):
        return self._stack

s = Stack()
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
print(s.display())

