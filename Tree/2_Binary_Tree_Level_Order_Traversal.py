# from implementation_of_queue_using_linked_list import Queue_Linkedlist        #------>we can also perform this instead of creating new queue from scratch

class _Node:
    __slots__ = '_element','_next'
    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class Queue:
    def __init__(self) -> None:
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
            print('list is Empty')
            return
        else:
            e = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return e

    def first(self):
        if self.isEmpty():
            print('list is empty')
            return
        else:
            return self._head._element

class Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left, right) -> None:
        self._element = element
        self._left = left
        self._right = right


class Binary_Tree:
    def __init__(self) -> None:
        self._root = None

    def make_tree(self,element, left = None, right = None):
        self._root = Node(element, left._root, right._root)                              

    def levelorder(self):
        q = Queue()
        # q = Queue_Linkedlist()           #---> this will also work but we need to place the file in the same folder
        t = self._root   
        print(t._element, end = ' ')
        q.enqueue(t)
        while not q.isEmpty():
            t = q.dequeue()
            if t._left:
                print(t._left._element, end = ' ')
                q.enqueue(t._left)
            if t._right:
                print(t._right._element, end = ' ')
                q.enqueue(t._right)

    def node_count(self, root):          #function to find the number of nodes

        if root:
            x = self.node_count(root._left)
            y = self.node_count(root._right)
            return x + y + 1
        return 0

    def height_tree(self, root):          #function to reduce the height of the tree by 1 
        x = self.__height_tree(root)
        return x - 1

    def __height_tree(self, root):          #actual function that find the height of the tree
        if root:
            x = self.__height_tree(root._left)
            y = self.__height_tree(root._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0
        

x = Binary_Tree()
r = Binary_Tree()
y = Binary_Tree()
s = Binary_Tree()
t = Binary_Tree()
z = Binary_Tree()
a = Binary_Tree()



x.make_tree(40, a, a)
y.make_tree(60, a, a)
r.make_tree(50, a, y)
z.make_tree(20, x, a)
s.make_tree(30, r, a)
t.make_tree(10, z, s)



t.levelorder()

print()
print(t.node_count(t._root))

print(t.height_tree(t._root))

