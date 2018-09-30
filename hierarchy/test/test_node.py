from unittest import TestCase
from hierarchy.src.node import Node


class TestNode(TestCase):
    def test_init(self):
        name = 'root'
        root = Node(name)
        self.assertIsInstance(root, Node)
        pass

    def test_is_root(self):
        root = Node('root')
        child = root.create_child('child')
        self.assertTrue(root.is_root())
        self.assertFalse(child.is_root())
        pass

    def test_get_name_full(self):
        name_root = 'root'
        name_child = 'child'
        root = Node(name_root)
        child = root.create_child(name_child)
        self.assertEqual(name_root, root.get_name())
        self.assertEqual(name_root, root.get_name_full())
        self.assertEqual(name_child, child.get_name())
        self.assertEqual(name_root + Node.JOINER_NAME + name_child, child.get_name_full())

    def test_is_my_child(self):
        root = Node('root')
        child1 = root.create_child('child1')
        child2 = root.create_child('child2')
        grandchild = child1.create_child('grandchild')

        root_other = Node('other_root')
        child_other = root_other.create_child('child_1')

        self.assertFalse(root.is_my_child(root))
        self.assertFalse(root.is_my_child(child1))
        self.assertFalse(root.is_my_child(child2))
        self.assertFalse(root.is_my_child(grandchild))
        self.assertFalse(root.is_my_child(root_other))
        self.assertFalse(root.is_my_child(child_other))
        self.assertFalse(root.is_my_child(child1))

        pass