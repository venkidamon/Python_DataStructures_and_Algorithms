class _Node:
    __slots__ = '_data','_parent','_height','_left','_right'
    def __init__(self, data, parent = None):
        self._data = data
        self._parent = parent
        self._height = 0
        self._left = None
        self._right = None

class AVL_Tree:
    def __init__(self) -> None:
        self.__root = None
    
    def insert(self, data):
        if not self.__root:
            self.__root = _Node(data)
        else:
            self.__insert_data(data, self.__root)

    def __insert_data(self, data, node):
        if data < node._data:
            if node._left:
                self.__insert_data(data, node._left)
            else:
                node._left = _Node(data, node)
                self.__violation_handler(node._left)
        elif data > node._data:
            if node._right:
                self.__insert_data(data, node._right)
            else:
                node._right = _Node(data, node)
                self.__violation_handler(node._right)

    def remove(self, data):
        try:
            if not self.__root:
                print('no data')
            else:
                self.__remove_data(data, self.__root)
        except TypeError:
            print('Wrong input')

    def __remove_data(self, data, node):
        if data < node._data:
            if node._left:
                self.__remove_data(data, node._left)
        elif data > node._data:
            if node._right:
                self.__remove_data(data, node._right)
        elif data == node._data:
            if not node._left and not node._right:
                parent_node = node._parent
                if parent_node:
                    if parent_node._left == node:
                        parent_node._left = None
                    elif parent_node._right == node:
                        parent_node._right = None
                else:
                    self.__root = None
                del node
                self.__violation_handler(parent_node)
            elif node._left and not node._right:
                parent_node = node._parent
                if parent_node:
                    if parent_node._left == node:
                        parent_node._left = node._left
                    elif parent_node._right == node:
                        parent_node._right = node._left
                else:
                    self.__root = node._left
                node._left._parent = parent_node
                del node
                self.__violation_handler(parent_node)
            elif node._right and not node._left:
                parent_node = node._parent
                if parent_node:
                    if parent_node._left == node:
                        parent_node._left = node._right
                    elif parent_node._right == node:
                        parent_node._right = node._right
                else:
                    self.__root = node._right
                node._right._parent = parent_node
                del node
                self.__violation_handler(parent_node)
            elif node._left and node._right:
                successor_node = self.__successor_node(node._right)
                successor_node._data, node._data = node._data, successor_node._data
                self.__remove_data(successor_node._data, node._right)

    def __successor_node(self, node):
        if node._left:
            return self.__successor_node(node._left)
        return node
    
    def __violation_handler(self, node):
        while node:
            node._height = max(self.__calculate_height(node._left), self.__calculate_height(node._right)) + 1
            self.__violation_fix(node)
            node = node._parent

    def __calculate_height(self, node):
        if not node:
            return -1
        return node._height

    def __violation_fix(self, node):
        if self.__balance_factor(node) > 1:
            if self.__balance_factor(node._left) < 0:
                self.__rotate_left(node._left)
            self.__rotate_right(node)
        elif self.__balance_factor(node) < -1:
            if self.__balance_factor(node._right) > 0:
                self.__rotate_right(node._right)
            self.__rotate_left(node)
    def __balance_factor(self, node):
        if not node:
            return 0
        return self.__calculate_height(node._left) - self.__calculate_height(node._right)

    def __rotate_right(self, node):
        temp_left_node = node._left
        t = node._left._right
        temp_left_node._right = node
        node._left = t
        temp_parent = node._parent
        temp_left_node._parent = temp_parent
        node._parent = temp_left_node
        if t:
            t._parent = node

        if temp_left_node._parent:
            if temp_left_node._parent._left == node:
                temp_left_node._parent._left = temp_left_node
            elif temp_left_node._parent._right == node:
                temp_left_node._parent._right = temp_left_node
        else:
            self.__root = temp_left_node

        node._height = max(self.__calculate_height(node._left), self.__calculate_height(node._right)) + 1
        temp_left_node._height - max(self.__calculate_height(temp_left_node._left), self.__calculate_height(temp_left_node._right)) + 1

    def __rotate_left(self, node):
        temp_right_node = node._right
        t = node._right._left
        temp_right_node._left = node
        node._right = t
        temp_parent = node._parent
        temp_right_node._parent = temp_parent
        node._parent = temp_right_node
        if t:
            t._parent = node
        if temp_right_node._parent:
            if temp_right_node._parent._left == node:
                temp_right_node._parent._left = temp_right_node
            elif temp_right_node._parent._right == node:
                temp_right_node._parent._right = temp_right_node
        else:
            self.__root = temp_right_node

        node._height = max(self.__calculate_height(node._left), self.__calculate_height(node._right)) + 1
        temp_right_node._height - max(self.__calculate_height(temp_right_node._left), self.__calculate_height(temp_right_node._right)) + 1


    def traverse(self):
        if self.__root:
            self.__inorder(self.__root)
        else:
            print('empty')
        
    def __inorder(self, node):
        if node._left:
            self.__inorder(node._left)
        print(node._data)
        if node._right:
            self.__inorder(node._right)

    def find(self, data):
        if self.__root:
            return self.__find_data(data, self.__root)

    def __find_data(self, data, node):
        try:
            if data < node._data:
                if node._left:
                    self.__find_data(data, node._left)
            elif data > node._data:
                if node._right:
                    self.__find_data(data, node._right)
            elif data == node._data:
                return True
            return False
        except TypeError:
            return 'wrong input'

    def min(self):
        if self.__root:
            return self.__find_min(self.__root)
    def __find_min(self, node):
        if node._left:
            return self.__find_min(node._left)
        return node._data

    def max(self):
        if self.__root:
            return self.__find_max(self.__root)
    def __find_max(self, node):
        if node._right:
            return self.__find_max(node._right)
        return node._data
        
if __name__ == "__main__":
    tree = AVL_Tree()

    tree.insert(12)
    tree.insert(24)
    tree.insert(10)
    tree.insert(0)
    tree.insert(-2)
    tree.insert(20)
    tree.insert(21)
    tree.insert(19)
    tree.insert(-6)
    tree.insert(-3)
    tree.insert(-10)
    tree.remove("sam")
    print(tree.find('-222'))
    print(f"min: {tree.min()}")
    print(f"max: {tree.max()}")


    tree.remove(12)




    tree.remove(24)
    tree.remove(10)
    tree.remove(0)
    tree.remove(-2)
    tree.remove(20)
    tree.remove(21)
    tree.remove(19)
    tree.remove(-6)
    tree.remove(-3)
    tree.remove(-10)

    print('-----------')
    tree.traverse()
