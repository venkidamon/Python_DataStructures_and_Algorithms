class DEQue:
    def __init__(self) -> None:
        self._deque = []

    def __len__(self):
        return len(self._deque)

    def isEmpty(self):
        return len(self._deque) == 0

    def add_first(self, element):
        self._deque.insert(0, element)

    def add_last(self, element):
        self._deque.append(element)

    def remove_first(self):
        if self.isEmpty():
            print('DEQue is empty')
            return
        else:
            return self._deque.pop(0)

    def remove_last(self):
        if self.isEmpty():
            print('DEQue is empty')
            return
        else:
            return self._deque.pop()

    def first(self):
        if self.isEmpty():
            print('DEQue is empty')
            return
        else:
            return self._deque[0]

    def last(self):
        if self.isEmpty():
            print('DEQue is empty')
            return
        else:
            return self._deque[-1]


d = DEQue()

d.add_first(1)
d.add_first(2)
d.add_last(1)
d.add_last(2)
print(len(d))
d.remove_first()
print(len(d))
print(d._deque)
d.remove_last()
print(len(d))
print(d._deque)
print(d.first())
d.add_last(7)
print(d.last())




