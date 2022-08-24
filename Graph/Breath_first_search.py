import numpy as np

class Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None):
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

    def enqueue(self, element):
        newest = Node(element)
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
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return e

    def display(self):
        p = self._head
        while p: 
            print(p._element, end='==>')
            p = p._next


class Graph:
    def __init__(self, vertices) -> None:
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))

    def insert_edge(self, u, v, w = 1):
        self._adjMat[u][v] = w

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count+=1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edge(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '--', j )

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        return self._adjMat

    def breath_first_search(self, source):
        i = source
        q = Queue()
        visited = [0] * self._vertices
        print(i, end = ' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.isEmpty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end = " ")
                    visited[j] = 1
                    q.enqueue(j)


g = Graph(7)
g.insert_edge(0,5)
g.insert_edge(0,1)
g.insert_edge(0,6)
g.insert_edge(1,0)
g.insert_edge(1,5)
g.insert_edge(1,6)
g.insert_edge(1,2)
g.insert_edge(5,3)
g.insert_edge(5,2)
g.insert_edge(2,6)
g.insert_edge(2,3)
g.insert_edge(2,4)
g.insert_edge(4,5)
g.insert_edge(4,2)
g.insert_edge(4,3)
g.insert_edge(6,3)

print(g.display_adjMat())

g.breath_first_search(0)

