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
                print(t._left._element, end = ' ')
                q.enqueue(t._left)
            if t._right:
                print(t._right._element, end = ' ')
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

    # def delete(self, element):
    #     p = self._root
    #     parent_p = None
    #     while p and p._element != element:
    #         parent_p = p
    #         if element < p._element:
    #             p = p._left
    #         else:
    #             p = p._right
    #     if not p:
    #         print('no element is present')
    #         return
    #     if p._left and p._right:
    #         s = p._right
    #         parent_s = p
    #         while s._left:
    #             parent_s = s
    #             s = s._left
    #         p._element = s._element
    #         p = s
    #         parent_p = parent_s
    #     c = None
    #     if p._left:
    #         c = p._left
    #     else:
    #         c = p._right
    #     if p == parent_p._left:
    #         parent_p._left = c
    #     elif p == parent_p._right:
    #         parent_p._right = c
    #     else:
    #         if p == self._root:
    #             self._root = None

    def delete(self, element):
        p = self._root
        parent_p = None
        while p and p._element != element:
            parent_p = p
            if element < p._element:
                p = p._left
            elif element > p._element:
                p = p._right
        if not p:
            print('no element')
            return 
        if parent_p == None:
            if p._left == None and p._right:
                if element == self._root._element:
                    c = p._right
                    p._element = c._element
                    p = c
                    if p == self._root._right:
                        self._root = p
            elif p._right == None and p._left:
                if element == self._root._element:
                    c = p._left
                    p._element = c._element
                    p = c 
                    if p == self._root._left:
                        self._root = p
            else:
                if p == self._root:
                    self._root = None
                    print('empty')
        else:
            if p._left and p._right:
                s = p._right
                parent_s = p
                while s._left:
                    parent_s = s
                    s = s._left
                p._element = s._element
                p = s
                parent_p = parent_s
            c = None
            if p._left:
                c = p._left
            else:
                c = p._right
            if p == parent_p._left:
                parent_p._left = c
            elif p == parent_p._right:
                parent_p._right = c
            else:
                if p == self._root:
                    self._root = None



        

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
a.insert(a._root, 40)
a.insert(a._root, 65)
a.insert(a._root, 60)
a.insert(a._root, 90)
a.insert(a._root, 52)
a.insert(a._root, 45)
a.insert(a._root, 56)
a.insert(a._root, 70)
a.insert(a._root, 95)
a.insert(a._root, 12)
a.insert(a._root, 15)








a.inorder(a._root)

a.delete(56)
print()
a.inorder(a._root)

a.delete(90)
print()
a.inorder(a._root)

a.delete(65)
print()
a.inorder(a._root)

a.delete(12)
print()
a.inorder(a._root)

a.delete(15)
print()
a.inorder(a._root)

a.delete(40)
print()
a.inorder(a._root)

a.delete(52)
print()
a.inorder(a._root)

a.delete(60)
print()
a.inorder(a._root)

a.delete(95)
print()
a.inorder(a._root)

a.delete(45)
print()
a.inorder(a._root)

a.delete(70)
print()
a.inorder(a._root)



