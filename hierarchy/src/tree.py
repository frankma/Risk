from hierarchy.src.node import Node


class Tree(object):
    def __init__(self, tree_name: str, root: Node):
        self._tree_name = tree_name
        self._root = root
        self._node_on_tree = {0: {self._root.get_name_full(), self._root}}
        pass

    def is_node_on_tree(self, node: Node):
        node_level = node.count_node_level()
        is_on_tree = self._root.__eq__(node.get_root())
        is_on_tree &= self._node_on_tree.__contains__(node_level)
        is_on_tree &= self._node_on_tree[node_level].__contains__(node.get_name_full())
        return is_on_tree

    def add_node_to_tree(self, node: Node):
        if not self._root.__eq__(node.get_root()):
            raise ValueError('cannot add node from other tree')
        node_level = node.count_node_level()
        while not self.is_node_on_tree(node):
            if self.is_node_on_tree(node.get_parent()):
                self._node_on_tree[node_level][node.get_name_full()] = node
            else:
                self.add_node_to_tree(node.get_parent())
        pass

    def drop_node_from_tree(self, node: Node):
        pass
