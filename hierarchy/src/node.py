class Node(object):
    JOINER_NAME = "^"

    def __init__(self, name: str, parent=None, children: dict = None):
        self._name = name
        self._parent = parent
        self._children = children if children is not None else dict()
        pass

    def get_parent(self):
        return self._parent

    def get_children(self):
        return self._children

    def get_name(self):
        return self._name

    def get_name_full(self):
        name_full = self.get_name()
        if not self.is_root():
            name_full = self.get_parent().get_name_full() + Node.JOINER_NAME + name_full
        return name_full

    def get_root(self):
        if self.is_root():
            return self
        else:
            return self.get_parent().get_root()
        pass

    def count_node_level(self):
        if self.is_root():
            return 1
        else:
            return self.get_parent().count_node_level() + 1
        pass

    def create_child(self, child_name: str):
        child = Node(child_name, self, dict())
        self._children[child.get_name()] = child
        return child

    def is_root(self):
        return self._parent is None

    def is_leaf(self):
        return self._children.__len__() == 0

    def is_my_parent(self, node):
        return not self.is_root() and self.get_parent().__eq__(node)

    def is_my_child(self, node):
        return self.__eq__(node.get_parent())

    def __hash__(self):
        return hash(self.get_name_full())

    def __eq__(self, other):
        return other is not None and self.__hash__() == other.__hash__()
