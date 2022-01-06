class _Node:
    __slots__ = '_element','_left','_right'
    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right
