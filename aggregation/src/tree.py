import itertools
from typing import Dict, Set

from aggregation.src.node import Node


class Tree(object):
    def __init__(self, tree_name: str, root: Node):
        self._tree_name = tree_name
        self._root = root
        self._node_on_tree = {self._root.count_node_level(): {self._root.get_name_full(): self._root}}
        self._node_serial_num = None
        pass

    def is_node_on_tree(self, node: Node) -> bool:
        is_on_tree = self._root.__eq__(node.get_root())
        is_on_tree = is_on_tree and (self._root.__eq__(node.get_root()))
        is_on_tree = is_on_tree and (node.count_node_level() in self._node_on_tree)
        is_on_tree = is_on_tree and (node.get_name_full() in self._node_on_tree[node.count_node_level()].keys())
        return is_on_tree

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
            for child in node.get_children():
                if self.is_node_on_tree(child):
                    self.drop_node_from_tree(child)
            else:
                self._node_on_tree[node.count_node_level()].pop(node.get_name_full(), None)
        pass

    def scan_leaf_nodes(self) -> Dict[int, Set[Node]]:
        leaf_nodes = {}
        for level in self._node_on_tree.keys():
            ln = []
            for node in self._node_on_tree[level].values():
                if node.is_leaf():
                    ln.append(node)
            if ln.__len__() is not 0:
                leaf_nodes[level] = set(ln)
        return leaf_nodes

    def scan_parent_children_map(self) -> Dict[int, Dict[Node, Set[Node]]]:
        parent_children_map = {}
        for level in self._node_on_tree.keys():
            pcm = {}
            for parent_node in self._node_on_tree[level].values():
                children = []
                for child_node in parent_node.get_children():
                    if self.is_node_on_tree(child_node):
                        children.append(child_node)
                if children.__len__() is not 0:
                    pcm[parent_node] = set(children)
            if pcm.__len__() is not 0:
                parent_children_map[level] = pcm
        return parent_children_map

    def get_tree_depth_stack(self) -> list:
        return sorted(self._node_on_tree.keys())

    def get_node_serial_number(self, refresh: bool = False) -> Dict[Node, str]:
        if self._node_serial_num is None or refresh:
            self._node_serial_num = {}
            for level in sorted(self._node_on_tree.keys()):
                non_leaf_nodes = []
                leaf_nodes = []
                for node_name in sorted(self._node_on_tree[level]):
                    node = self._node_on_tree[level][node_name]
                    if node.is_leaf():
                        leaf_nodes.append(node)
                    else:
                        non_leaf_nodes.append(node)
                for idx, node in enumerate(itertools.chain(non_leaf_nodes, leaf_nodes)):
                    if node.is_root():
                        self._node_serial_num[node] = 'T'
                    else:
                        self._node_serial_num[node] = self._node_serial_num[node.get_parent()] + '.' + str(idx)
        return self._node_serial_num

    def __str__(self):
        return self._tree_name
