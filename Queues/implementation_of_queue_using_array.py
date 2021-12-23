class Queue:
    def __init__(self) -> None:
        self._queue = []
        
    def __len__(self):
        return len(self._queue)

    def isEmpty(self):
        return len(self._queue) == 0

    def enqueue(self, element):
        self._queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
            return
        else:
            e = self._queue.pop(0)
            return e

    def first(self):
        if self.isEmpty():
            print('queue is empty')
            return
        else:
            return self._queue[0]

    # def display(self):
    #     return self._queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.first())
q.enqueue(3)
q.enqueue(4)
print(q.display())
q.dequeue()
print(q.first())
print(q.display())
print(q.first())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.display())


