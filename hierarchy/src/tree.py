from hierarchy.src.node import Node


class Tree(object):
    def __init__(self, tree_name: str, root: Node):
        self._tree_name = tree_name
        self._root = root
        self._node_on_tree = {0: {self._root.get_name_full(), self._root}}
        pass

    def is_node_on_tree(self, node: Node):
        pass

    def add_node_to_tree(self, node: Node):
        pass

    def drop_node_from_tree(self, node: Node):
        pass
