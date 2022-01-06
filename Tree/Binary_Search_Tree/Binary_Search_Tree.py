from Node import _Node


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

