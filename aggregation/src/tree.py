from aggregation.src.node import Node


class Tree(object):
    def __init__(self, tree_name: str, root: Node):
        self._tree_name = tree_name
        self._root = root
        self._node_on_tree = {self._root.count_node_level(): {self._root.get_name_full(): self._root}}
        pass

    def is_node_on_tree(self, node: Node):
        node_level = node.count_node_level()
        return self._root.__eq__(node.get_root()) and \
               node_level in self._node_on_tree and \
               node.get_name_full() in self._node_on_tree[node_level]

    def get_all_children_on_tree(self, node: Node):
        children_on_tree = []
        if not node.is_leaf():
            for child in node.get_children().values():
                if self.is_node_on_tree(child):
                    children_on_tree.append(child)
        return children_on_tree

    def add_node_to_tree(self, node: Node):
        if not self._root.__eq__(node.get_root()):
            raise ValueError('cannot add node from other tree')
        node_level = node.count_node_level()
        while not self.is_node_on_tree(node):
            parent_node = node.get_parent()
            if self.is_node_on_tree(parent_node):
                # add target node to the tree
                if node_level not in self._node_on_tree:
                    self._node_on_tree[node_level] = {}
                self._node_on_tree[node_level][node.get_name_full()] = node
                # update target parent node on tree
                parent_node_level = parent_node.count_node_level()
                self._node_on_tree[parent_node_level][parent_node.get_name_full()].add_child(node)
            else:
                self.add_node_to_tree(node.get_parent())
        pass

    def drop_node_from_tree(self, node: Node):
        while self.is_node_on_tree(node):
            level = node.count_node_level()
            on_tree_children = self.get_all_children_on_tree(node)
            if on_tree_children.__len__() > 0:
                for on_tree_child in on_tree_children:
                    self.drop_node_from_tree(on_tree_child)
            else:
                self._node_on_tree[level].pop(node.get_name_full(), None)
        pass
