from typing import Dict, Set

from numpy import ndarray

from aggregation.src.node import Node
from aggregation.src.tree import Tree


class Aggregator(object):
    def __init__(self, tree: Tree, leaf_values: Dict[Node, ndarray], nodes_for_store: Set[Node]):
        self._tree = tree
        self._leaf_values = leaf_values
        self._nodes_for_store = nodes_for_store

        self.roll_stack = tree.get_tree_depth_stack()
        self.__current_level = self.roll_stack.pop()

        pass

    def process(self):
        pass

    def roll_up(self):
        if self.roll_stack.__len__() > 0:
            pass
        pass

    def __source_leaf_values(self):
        pass

    def __aggregate(self):
        pass

    def __store_node_values(self):
        pass
