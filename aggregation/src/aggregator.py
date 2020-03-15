import logging
from typing import Dict, Set

from numpy import ndarray

from aggregation.src.node import Node
from aggregation.src.tree import Tree

logger = logging.getLogger(__name__)


class Aggregator(object):
    def __init__(self, tree: Tree, leaf_values: Dict[Node, ndarray], nodes_for_store: Set[Node]):
        self._tree = tree
        self._leaf_values = leaf_values
        self._nodes_for_store = nodes_for_store

        self._stored_values = {}
        self._roll_stack = tree.get_tree_depth_stack()
        self.__parent_children_map = tree.scan_parent_children_map()
        self.__leaf_nodes = tree.scan_leaf_nodes()

        self.__current_level = self._roll_stack.pop()
        self.__current_level_values = self.__source_leaf_values()
        self.__store_node_values(self.__current_level_values)
        pass

    def process(self):
        while self._roll_stack.__len__() > 0:
            self.roll_up()
        pass

    def roll_up(self):
        if self._roll_stack.__len__() > 0:
            self.__current_level = self._roll_stack.pop()
            self.__current_level_values = self.__aggregate(self.__parent_children_map[self.__current_level])
            self.__current_level_values.update(self.__source_leaf_values())
            self.__store_node_values(self.__current_level_values)
            pass
        pass

    def __source_leaf_values(self) -> Dict[Node, ndarray]:
        leaf_values = {}
        nodes = self.__leaf_nodes[self.__current_level] if self.__leaf_nodes.__contains__(self.__current_level) else {}
        # TODO: make parallel loading here
        for node in nodes:
            if self._leaf_values.__contains__(node):
                leaf_values[node] = self._leaf_values.pop(node)
        return leaf_values

    def __aggregate(self, parent_children: Dict[Node, Set[Node]]) -> Dict[Node, ndarray]:
        agg_values = {}
        # TODO: make parallel aggregation here
        for parent_node in parent_children:
            parent_value = None
            children_nodes = parent_children[parent_node]
            for child_node in children_nodes:
                if not self.__current_level_values.__contains__(child_node):
                    logger.info('%s node %s value unavailable, ignored'
                                % ('leaf' if child_node.is_leaf() else 'agg', child_node.get_name_full()))
                    continue
                child_value = self.__current_level_values[child_node]
                if parent_value is None:
                    parent_value = child_value
                else:
                    parent_value += child_value
            if parent_value is not None:
                agg_values[parent_node] = parent_value
        return agg_values

    def __store_node_values(self, node_values: Dict[Node, ndarray]):
        nfs = self._nodes_for_store & node_values.keys()
        # TODO: make parallel storage
        for node in nfs:
            self._stored_values[node] = node_values[node]
        self._nodes_for_store = self._nodes_for_store - nfs  # short list for efficiency
        pass
