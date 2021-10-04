class BinaryTree(object):
    def __init__(self, root_val):
        self.key = root_val
        self.left_child = None
        self.right_child = None

    def insertLeft(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_value(self):
        return self.key

def preorder(tree):
        
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value())
    







value = BinaryTree('a')

value.insertLeft('b')
value.insertRight('c')
value.insertLeft('d')
value.insertRight('m')
value.insertRight('n')


preorder(value)
print("--------------")
inorder(value)
print("--------------")
postorder(value)
print("--------------")



