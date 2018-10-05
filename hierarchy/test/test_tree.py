from unittest import TestCase
from hierarchy.src.node import Node
from hierarchy.src.tree import Tree


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
