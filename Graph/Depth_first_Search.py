from select import select
import numpy as np


class Graph:
    def __init__(self, vertices) -> None:
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
        self._visited = [0] * vertices

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
                if self._adjMat[i][j] == 1:
                    count += 1
        return count 

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,'--',j)

    def outdegree(self,v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[j][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)


    def depth_first_search(self, s):
        if self._visited[s] == 0:
            print(s, end = " ")
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._visited[j] == 0:
                    self.depth_first_search(j)