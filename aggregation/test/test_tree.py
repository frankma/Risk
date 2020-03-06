from unittest import TestCase

from aggregation.src.node import Node
from aggregation.src.tree import Tree


class TestTree(TestCase):
    def test_is_node_on_tree(self):
        root = Node("root", None, None)
        child = root.create_child("child")
        grandchild = child.create_child("grandchild")

        tree = Tree("tree", root)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertFalse(tree.is_node_on_tree(child))
        self.assertFalse(tree.is_node_on_tree(grandchild))
        pass

    def test_add_node_to_tree(self):
        root = Node("root", None, None)
        child = root.create_child("child")
        grandchild = child.create_child("grandchild")

        tree = Tree("tree", root)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertFalse(tree.is_node_on_tree(child))
        self.assertFalse(tree.is_node_on_tree(grandchild))

        tree.add_node_to_tree(grandchild)
        self.assertTrue(tree.is_node_on_tree(child))
        self.assertTrue(tree.is_node_on_tree(grandchild))

        tree.add_node_to_tree(child)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertTrue(tree.is_node_on_tree(child))
        self.assertTrue(tree.is_node_on_tree(grandchild))
        pass

    def test_drop_node_from_tree(self):
        root = Node("root", None, None)
        child = root.create_child("child")
        grandchild_1 = child.create_child("grandchild1")
        grandchild_2 = child.create_child("grandchild2")

        tree = Tree("tree", root)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertFalse(tree.is_node_on_tree(child))
        self.assertFalse(tree.is_node_on_tree(grandchild_1))
        self.assertFalse(tree.is_node_on_tree(grandchild_2))

        tree.add_node_to_tree(grandchild_1)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertTrue(tree.is_node_on_tree(child))
        self.assertTrue(tree.is_node_on_tree(grandchild_1))
        self.assertFalse(tree.is_node_on_tree(grandchild_2))
        tree.add_node_to_tree(grandchild_2)
        self.assertTrue(tree.is_node_on_tree(grandchild_2))

        tree.drop_node_from_tree(grandchild_2)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertTrue(tree.is_node_on_tree(child))
        self.assertTrue(tree.is_node_on_tree(grandchild_1))
        self.assertFalse(tree.is_node_on_tree(grandchild_2))

        tree.drop_node_from_tree(child)
        self.assertTrue(tree.is_node_on_tree(root))
        self.assertFalse(tree.is_node_on_tree(child))
        self.assertFalse(tree.is_node_on_tree(grandchild_1))
        self.assertFalse(tree.is_node_on_tree(grandchild_2))

        pass

    def test_scan_leaf_nodes(self):
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

        v = tree.scan_leaf_nodes()

        pass

    def test_parent_children_map(self):
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

        v = tree.scan_parent_children_map()

        pass

    def test_gen_node_serial_number(self):
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

        tree.get_node_serial_number()

        pass
