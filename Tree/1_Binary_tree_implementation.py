class _Node:
    __slots__ = '_element','_left','_right'

    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right


class Binary_Tree:

    def __init__(self):
        self._root = None

    def make_tree(self, element, left = None, right = None):
        self._root = _Node(element, left._root, right._root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)
        
    def postorder(self, troot):
        if troot:
            self.preorder(troot._left)
            self.preorder(troot._right)
            print(troot._element, end=' ')

        

    
# x = Binary_Tree()
# y = Binary_Tree()
# z = Binary_Tree()
# a = Binary_Tree()

# x.make_tree(20, a, a)
# y.make_tree(30, a, a)
# z.make_tree(10, x, y)

# z.preorder(z._root)
# z.inorder(z._root)
# z.postorder(z._root)


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

print('-----------INORDER---------')
t.inorder(t._root)

print()
print('------------PREORDER----------')
t.preorder(t._root)
print()
print('------------POSTORDER----------')
t.preorder(t._root)
