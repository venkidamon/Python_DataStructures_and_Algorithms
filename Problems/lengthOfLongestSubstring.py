class _Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None) -> None:
        self._element = element
        self._next = next
        


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def len(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def enqueue(self, element):
        newest = _Node(element)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            e = self._head._element
            self._head = self._head._next
            if self.isEmpty():
                self._tail = None
            self._size -= 1
            return e

    def first(self):
        return self._head._element

class Solution:
    def lengthOfLongestSubstring(self, s):
        q = Queue()
        for x in s:
            q.enqueue(x)
        p = q._head
        while p:
            z = Queue()
            c =  p._next
            z.enqueue(p._element)
            while c:
                if c._element != p._element:
                    z.enqueue(c._element)
                else:
                    break
                c = c._next
            p = p._next


s = Solution()
s.lengthOfLongestSubstring('aaabccc')