"""
    Implementation of an AVL tree

    KEY POINTS:
    1) It is a balanced binary search tree.
    2) The worst case scenario of a binary tree is a linked list; complexity becomes O(N)
    3) AVL trees solve this problem!
    4) We have to maintain the "height" of each node and its children.
    5) The height of any node is the number of layers in the tree; longest path from the parent node to the leaf node.
       "height = max(left child's height, right child's height) + 1", to compensate the None(None = -1)
    6) The difference(balance factor) in the heights of the left sub-tree and the right sub-tree cannot be more than 1.
    7) If the difference is more than 1, we rotate the node to the left or the right, to keep the tree balanced.
    8) We have 4 conditions to take care of:
       A) left-left heavy; Left child's height - Right child's height > 1, node rotated to the right
       B) left-right heavy; balance factor of node.left is < -1 or 0
       C) right-right heavy; Left child's height - Right child's height < -1, node rotated to the left
       D) right-left heavy; balance factor of node.right is > 1 or 0

       a) LEFT LEFT         b) LEFT RIGHT           c) RIGHT RIGHT          d) RIGHT LEFT
             1                    1                         1                       1
           2                    2                             2                       2
         3                        3                             3                   3

             2                     1                        2                       1
          3     1                3                       1     3                       3
                               2                                                          2

                                  3                                                  3
                                2    1                                            1     2

"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.__root = None

    def insert(self, data):
        # if there is no "root node"
        if not self.__root:
            self.__root = Node(data)   # not passing the parent, as the root node has no parent
        # if the rot node exists
        else:
            self.__insert_data(data, self.__root)

    def remove(self, data):
        try:
            if not self.__root:
                print("No data!")
            else:
                self.__remove_data(data, self.__root)
        except TypeError:
            print("Incorrect Type!")

    def __insert_data(self, data, node):
        if data < node.data:
            if node.left:
                self.__insert_data(data, node.left)
            else:
                node.left = Node(data, node)
                self.__violation_handler(node.left)
        if data > node.data:
            if node.right:
                self.__insert_data(data, node.right)
            else:
                node.right = Node(data, node)
                self.__violation_handler(node.right)

    def __remove_data(self, data, node):
        # first we have to find the data
        if data < node.data:
            if node.left:
                self.__remove_data(data, node.left)
        elif data > node.data:
            if node.right:
                self.__remove_data(data, node.right)
        elif data == node.data:
            # 1) when the node to be removed has no child; leaf node
            if not node.left and not node.right:
                parent_node = node.parent
                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = None
                    elif parent_node.right == node:
                        parent_node.right = None
                # if the node is the root node
                else:
                    self.__root = None
                del node
                self.__violation_handler(parent_node)
            # 2) when the left child exists
            elif node.left and not node.right:
                parent_node = node.parent
                # parent to child relationship
                if parent_node:
                    if parent_node.left == node:  # which we want to remove
                        parent_node.left = node.left
                    elif parent_node.right == node:
                        parent_node.right = node.left
                else:
                    self.__root = node.left
                # child to parent relationship
                node.left.parent = parent_node
                del node
                self.__violation_handler(parent_node)
            # 3) when right child exists
            elif node.right and not node.left:
                parent_node = node.parent
                # parent to child relationship
                if parent_node:
                    if parent_node.left == node:  # which we want to remove
                        parent_node.left = node.right
                    elif parent_node.right == node:
                        parent_node.right = node.right
                else:
                    self.__root = node.right
                # child to parent relationship
                node.right.parent = parent_node
                del node
                self.__violation_handler(parent_node)
            # 4) when the node has two children
            # a) we have to find either the predecessor node or the successor node
            # b) swap the values of the node and either of the above mentioned nodes
            # c) delete the predecessor or the successor
            elif node.left and node.right:
                # successor node: the smallest node in the right subtree of the "node"
                successor_node = self.__find_successor(node.right)
                successor_node.data, node.data = node.data, successor_node.data
                self.__remove_data(successor_node.data, node.right)

    def __find_successor(self, node):
        if node.left:
            return self.__find_successor(node.left)
        return node

    def __violation_handler(self, node):
        while node:  # while the node is not a None.
            node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
            self.__violation_fix(node)
            node = node.parent   # to traverse up to the root node

    def __calculate_height(self, node):
        """"height = max(left child's height, right child's height) + 1"""
        if not node:
            return -1
        return node.height

    def __violation_fix(self, node):
        # left left heavy
        if self.__balance_factor(node) > 1:
            # left right heavy
            if self.__balance_factor(node.left) < 0:  # -1 gave me an infinite loop
                self.__rotate_left(node.left)
            self.__rotate_right(node)
        # right right heavy
        if self.__balance_factor(node) < -1:
            # right left heavy
            if self.__balance_factor(node.right) > 0:  # avoid the infinite loop
                self.__rotate_right(node.right)
            self.__rotate_left(node)

    def __balance_factor(self, node):
        """The difference between the left child's height and the right child's height"""
        if not node:
            return 0
        return self.__calculate_height(node.left) - self.__calculate_height(node.right)

    def __rotate_left(self, node):
        temp_right_node = node.right
        t = node.right.left

        # updating the references
        temp_right_node.left = node
        node.right = t

        # update child to parent relationship
        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node
        if t:
            t.parent = node

        # update parent to child relationship
        if temp_right_node.parent:   # it is not the root node
            if temp_right_node.parent.left == node:
                temp_right_node.parent.left = temp_right_node
            elif temp_right_node.parent.right == node:
                temp_right_node.parent.right = temp_right_node
        # if it is a root node
        else:
            self.__root = temp_right_node

        # update the height of the nodes
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_right_node.height = max(self.__calculate_height(temp_right_node.left),
                                     self.__calculate_height(temp_right_node.right)) + 1

        print(f"left rotation on {node.data}...")

    def __rotate_right(self, node):
        temp_left_node = node.left
        t = node.left.right

        # update the references
        temp_left_node.right = node
        node.left = t

        # child to parent
        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node
        if t:
            t.parent = node

        # parent to child
        if temp_left_node.parent:
            if temp_left_node.parent.left == node:
                temp_left_node.parent.left = temp_left_node
            elif temp_left_node.parent.right == node:
                temp_left_node.parent.right = temp_left_node
        else:
            self.__root = temp_left_node

        # update the height of the nodes
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_left_node.height = max(self.__calculate_height(temp_left_node.left),
                                    self.__calculate_height(temp_left_node.right)) + 1

        print(f"right rotation on {node.data}...")

    def traverse(self):
        if self.__root:
            self.__in_order(self.__root)

    def __in_order(self, node):
        """left -> parent -> right"""
        if node.left:
            self.__in_order(node.left)

        print(node.data)

        if node.right:
            self.__in_order(node.right)

    def find(self, data):
        if self.__root:
            return self.__find_data(data, self.__root)

    def __find_data(self, data, node):
        try:
            # we look for the data
            if data < node.data:
                if node.left:
                    return self.__find_data(data, node.left)
            elif data > node.data:
                if node.right:
                    return self.__find_data(data, node.right)
            elif data == node.data:
                return True
            return False
        except TypeError:
            return "Incorrect Type!"

    def min(self):
        if self.__root:
            return self.__find_min(self.__root)

    def __find_min(self, node):
        """we need to find the left mode node"""
        if node.left:
            return self.__find_min(node.left)
        return node.data

    def max(self):
        if self.__root:
            return self.__find_max(self.__root)

    def __find_max(self, node):
        """we need to find the right most node"""
        if node.right:
            return self.__find_max(node.right)
        return node.data


if __name__ == "__main__":
    tree = AVLTree()

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
    tree.traverse()