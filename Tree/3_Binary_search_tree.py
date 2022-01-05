class _Node:
    __slots__ = '_element','_left','_right'
    def __init__(self, element, left = None, right = None) -> None:
        self._element = element
        self._left = left
        self._right = right

class Binary_Tree:
    def __init__(self) -> None:
        self._root = None

    def make_tree(self, element, left, right):
        self._root = _Node(element, left._root, right._root)

    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end = ' ')
            self.inorder(root._right)

    def search(self, root, element):
        if root:
            if element == root._element:
                return True
            if element < root._element:
                return self.search(root._left, element)

            if element > root._element:
                return self.search(root._right, element)
        else:
            return False

    def search_iter(self, element):
        root = self._root
        while root:
            if element == root._element:
                return True
            elif element < root._element:
                root = root._left
            elif element > root._element:
                root = root._right
        return False
                

    def insert(self, root, element):                   #this method is iterative approach of insert function O(h) h --> height of the tree
        temp = None 
        while root:
            temp = root
            if root._element == element:
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

p = Binary_Tree()
q = Binary_Tree()
r = Binary_Tree()
s = Binary_Tree()
t = Binary_Tree()
u = Binary_Tree()
v = Binary_Tree()
w = Binary_Tree()
# a = Binary_Tree()
# a.insert(a._root, 2)
# a.insert(a._root, 7)
# a.inorder(a._root)


s.make_tree(1,w,w)
t.make_tree(4,w,w)
u.make_tree(6,w,w)
v.make_tree(9,w,w)
q.make_tree(3,s,t)
r.make_tree(8,u,v)
p.make_tree(5,q,r)




p.inorder(p._root)

print(p.search(p._root, 80))


print(p.search_iter(50))


p.insert(p._root, 52)
p.inorder(p._root)


