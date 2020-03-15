from typing import Set


class Node(object):
    JOINER_NAME = "^"

    def __init__(self, name: str, parent=None, children: Set = None):
        self._name = name
        self._parent = parent
        self._children = children if children is not None else set()
        self.__name_full = None
        pass

    def get_parent(self):
        return self._parent

    def get_children(self) -> Set:
        return self._children

    def get_name(self) -> str:
        return self._name

    def get_name_full(self) -> str:
        if self.__name_full is None:
            full_name = self.get_name()
            if not self.is_root():
                full_name = self.get_parent().get_name_full() + Node.JOINER_NAME + full_name
            self.__name_full = full_name
        return self.__name_full

    def get_root(self):
        return self if self.is_root() else self.get_parent().get_root()

    def count_node_level(self) -> int:
        return 1 if self.is_root() else self.get_parent().count_node_level() + 1

    def create_child(self, child_name: str):
        child = Node(child_name, self, set())
        self._children.add(child)
        return child

    def add_child(self, node_child):
        if not isinstance(node_child, Node):
            raise ValueError('expect input as Node type')
        else:
            if node_child.is_my_parent(self) and not self.is_my_child(node_child):
                self._children.add(node_child)
                node_child._parent = self  # enforce bilateral reference
        pass

    def is_root(self) -> bool:
        return self._parent is None

    def is_leaf(self) -> bool:
        return self._children.__len__() == 0

    def is_my_parent(self, node) -> bool:
        return not self.is_root() and self.get_parent().__eq__(node)

    def is_my_child(self, node) -> bool:
        return self.__eq__(node.get_parent()) and node in self._children

    def __hash__(self):
        return hash(self.get_name_full())

    def __eq__(self, other):
        return other is not None and self.get_name_full() == other.get_name_full()

    def __str__(self):
        return self.get_name_full()
