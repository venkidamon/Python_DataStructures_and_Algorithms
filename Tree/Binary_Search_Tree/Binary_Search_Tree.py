from Node import _Node
from Queue import Queue


class Binary_Search_Tree:

    def __init__(self) -> None:
        self._root = None

    def recursive_insert(self, root, element):
        if root:
            if element == root._element:
                return
            elif element < root._element:
                root._left = self.recursive_insert(root._left, element)
            elif element > root._element:
                root._right = self.recursive_insert(root._right, element)
        else:
            n = _Node(element)
            root = n
        return root

    def insert(self, root, element):
        temp = None
        while root:
            temp = root
            if element == root._element:
                return
            elif element < root._element:
                root = root._left
            elif element > root._element:
                root = root._right
        n = _Node(element)
        if self._root:
            if element < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end=' ')
            self.inorder(root._right)

    def level_order(self, root):
        q = Queue()
        t = self._root
        print(t._element)
        q.enqueue(t)
        while not q.isEmpty():
            t = q.dequeue()
            if t._left:
                print('/')
                print(t._left._element)
                q.enqueue(t._left)
            if t._right:
                print('\\')
                print(t._right._element)
                q.enqueue(t._right)



    def search(self, element):
        root = self._root
        while root:
            if element == root._element:
                return True
            elif element < root._element:
                root = root._left
            elif element > root._element:
                root = root._right
        return False

    def recursive_searh(self, root, element):
        if root:
            if element == root._element:
                return True
            elif element < root._element:
                return self.recursive_searh(root._left, element)
            elif element > root._element:
                return self.recursive_searh(root._right, element)
        else:
            return False

    # def delete_leaf_node(self, element):
    #     p = self._root
    #     parent_node = None
    #     while p and p._element != element:
    #         parent_node = p
    #         if element < p._element:
    #             p = p._left
    #         elif element > p._element:
    #             p = p._right
    #     if parent_node._left._element == element:
    #         parent_node._left = None
    #     elif parent_node._right._element == element:
    #         parent_node._right = None
        

    def height(self, root):
        h = self._height(root)
        return h-1
    def _height(self, root):
        if root:
            x = self._height(root._left)
            y = self._height(root._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        else:
            return 0




            
a = Binary_Search_Tree()
a._root = a.recursive_insert(a._root,5)
a.recursive_insert(a._root,4)
a.recursive_insert(a._root,3)
a.recursive_insert(a._root,2)
a.recursive_insert(a._root,1)
a.insert(a._root,6)
a.insert(a._root,7)
a.insert(a._root,8)
a.insert(a._root,9)
a.insert(a._root,0)

a.inorder(a._root)
print(a.search(5))
print(a.search(0))
print(a.search(56))
print(a.search(21))

print(a.recursive_searh(a._root, 4))
print(a.recursive_searh(a._root, 400))
print(a.recursive_searh(a._root, 3))

print(a.height(a._root))

a.delete_leaf_node(0)

a.level_order(a._root)