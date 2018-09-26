from hierarchy.src.node import Node


class Tree(object):
    def __init__(self, tree_name: str, root: Node):
        self._tree_name = tree_name
        self._root = root
        root_level = root.get_node_level()
        root_tags_str = root.get_tags_string()
        self._nodes = {root_tags_str: root}
        self._node_layer_lookup = {root_level: [root_tags_str]}  # sole root and sole layer
        pass

    def is_node_on_tree(self, node: Node):
        return self._nodes.__contains__(node.get_tags_string())

    def add_node_to_tree(self, node: Node):
        while not self.is_node_on_tree(node):
            parent_node = node.get_parent()
            if self.is_node_on_tree(parent_node):
                node_level = node.get_node_level()
                node_tags_string = node.get_tags_string()
                self._nodes[node_tags_string] = node
                if not self._node_layer_lookup.__contains__(node_level):
                    self._node_layer_lookup[node_level] = []
                self._node_layer_lookup[node_level].append(node_tags_string)
            else:
                self.add_node_to_tree(parent_node)
        pass

    def drop_node_from_tree(self, node: Node):
        while self.is_node_on_tree(node):
            node_children = node.get_children()
            node_children_on_tree = []
            for node_child in node_children:
                if self.is_node_on_tree(node_child):
                    node_children_on_tree.append(node_child)
            if node_children_on_tree.__len__() == 0:
                node_level = node.get_node_level()
                node_tags_str = node.get_tags_string()
                self._nodes.pop(node_tags_str)
                self._node_layer_lookup[node_level].remove(node_tags_str)
            else:
                for child in node_children_on_tree:
                    self.drop_node_from_tree(child)
        pass
