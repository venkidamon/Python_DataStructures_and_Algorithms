


class _Node:
    __slots__ = '_data','_parent', '_height','_left','_right'
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
                node._left = _Node(data)
                self.__violation_handler(node._left)
        elif data > node._data:
            if node._right:
                self.__insert_data(data, node._right)
            else:
                node._right = _Node(data)
                self.__violation_handler(node._right)
    
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
        if self.__balance_factor(node) < -1:
            if self.__balance_factor(node._right) > 0:
                self.__rotate_right(node._right)
            self.__rotate_left(node)
        elif self.__balance_factor(node) > 1:
            if self.__balance_factor(node._left) < 0:
                self.__rotate_left(node.left)
            self.__rotate_right(node)

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
        node._height = max(self.__calculate_height(node._left),self.__calculate_height(node._right)) + 1
        temp_left_node._height = max(self.__calculate_height(temp_left_node._left), self.__calculate_height(temp_left_node._right)) + 1

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
            elif temp_right_node.parent._right == node:
                temp_right_node._parent._right = temp_right_node
        else:
            self.__root = temp_right_node
        
        node._height = max(self.__calculate_height(node._left),self.__calculate_height(node._right)) + 1
        temp_right_node._height = max(self.__calculate_height(temp_right_node._left), self.__calculate_height(temp_right_node._right)) + 1

    def traverse(self):
        if self.__root:
            self.__in_order(self.__root)


    def __in_order(self, node):
        if node._left:
            self.__in_order(node._left)
        print(node._data)
        if node._right:
            self.__in_order(node._right)


if __name__ == "__main__":
    tree = AVL_Tree()
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)
    tree.insert(80)
    tree.insert(55)
    tree.insert(65)
    tree.insert(75)
    tree.insert(85)

    tree.traverse()