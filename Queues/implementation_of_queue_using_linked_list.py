class _Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next

class Queue_Linkedlist:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def enqueue(self, ele):
        newest = _Node(ele)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
            return
        else:
            e = self._head._element
            self._head = self._head._next
            self._size-=1
            if self.isEmpty():
                self._tail = None
            return e

    def first(self):
        if self.isEmpty():
            print('queue is empty')
            return
        else:
            return self._head._element

q = Queue_Linkedlist()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()
print(q.first())
print(len(q))
