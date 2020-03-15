from unittest import TestCase

import numpy as np

from aggregation.src.aggregator import Aggregator
from aggregation.src.node import Node
from aggregation.src.tree import Tree


class TestAggregator(TestCase):
    def test_init(self):
        root = Node("root", None, None)
        child_1 = root.create_child("child1")
        grandchild_1 = child_1.create_child("grandchild1")
        grandchild_2 = child_1.create_child("grandchild2")
        child_2 = root.create_child("child2")
        child_3 = root.create_child("child3")
        grandchild_3 = child_3.create_child("grandchild3")

        tree = Tree("tree", root)
        tree.add_node_to_tree(grandchild_1)
        tree.add_node_to_tree(grandchild_2)
        tree.add_node_to_tree(child_2)
        tree.add_node_to_tree(grandchild_3)

        leaf_values = {grandchild_1: np.array([1.0, 2.0, 3.0]),
                       grandchild_2: np.array([1.0, 2.0, 3.0]),
                       grandchild_3: np.array([1.0, 2.0, 3.0]),
                       child_2: np.array([1.0, 2.0, 3.0])}

        nodes_for_store = {root, child_1, child_3}

        agg = Aggregator(tree, leaf_values, nodes_for_store)
        agg.process()
        pass

    pass
