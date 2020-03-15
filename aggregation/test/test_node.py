from unittest import TestCase

from aggregation.src.node import Node


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
        pass

    def test_node_level(self):
        root = Node('root')
        child = root.create_child('child')
        grand_child = child.create_child('grandchild')
        self.assertEqual(1, root.count_node_level())
        self.assertEqual(2, child.count_node_level())
        self.assertEqual(3, grand_child.count_node_level())
        pass

    def test_is_my_child(self):
        root = Node('root')
        child1 = root.create_child('child1')
        child2 = root.create_child('child2')
        grandchild = child1.create_child('grandchild')

        root_other = Node('other_root')
        child_other = root_other.create_child('child_1')

        self.assertFalse(root.is_my_child(root))
        self.assertTrue(root.is_my_child(child1))
        self.assertTrue(root.is_my_child(child2))
        self.assertFalse(root.is_my_child(grandchild))
        self.assertFalse(root.is_my_child(root_other))
        self.assertFalse(root.is_my_child(child_other))

        self.assertFalse(child1.is_my_child(root))
        self.assertFalse(child1.is_my_child(child1))
        self.assertFalse(child1.is_my_child(child2))
        self.assertTrue(child1.is_my_child(grandchild))
        self.assertFalse(child1.is_my_child(root_other))
        self.assertFalse(child1.is_my_child(child_other))

        self.assertFalse(child2.is_my_child(root))
        self.assertFalse(child2.is_my_child(child1))
        self.assertFalse(child2.is_my_child(child2))
        self.assertFalse(child2.is_my_child(grandchild))
        self.assertFalse(child2.is_my_child(root_other))
        self.assertFalse(child2.is_my_child(child_other))

        self.assertFalse(grandchild.is_my_child(root))
        self.assertFalse(grandchild.is_my_child(child1))
        self.assertFalse(grandchild.is_my_child(child2))
        self.assertFalse(grandchild.is_my_child(grandchild))
        self.assertFalse(grandchild.is_my_child(root_other))
        self.assertFalse(grandchild.is_my_child(child_other))

        pass

    def test_is_my_parent(self):
        root = Node('root')
        child1 = root.create_child('child1')
        child2 = root.create_child('child2')
        grandchild = child1.create_child('grandchild')

        root_other = Node('other_root')
        child_other = root_other.create_child('child_1')

        self.assertFalse(root.is_my_parent(root))
        self.assertFalse(root.is_my_parent(child1))
        self.assertFalse(root.is_my_parent(child2))
        self.assertFalse(root.is_my_parent(grandchild))
        self.assertFalse(root.is_my_parent(root_other))
        self.assertFalse(root.is_my_parent(child_other))

        self.assertTrue(child1.is_my_parent(root))
        self.assertFalse(child1.is_my_parent(child1))
        self.assertFalse(child1.is_my_parent(child2))
        self.assertFalse(child1.is_my_parent(grandchild))
        self.assertFalse(child1.is_my_parent(root_other))
        self.assertFalse(child1.is_my_parent(child_other))

        self.assertTrue(child2.is_my_parent(root))
        self.assertFalse(child2.is_my_parent(child1))
        self.assertFalse(child2.is_my_parent(child2))
        self.assertFalse(child2.is_my_parent(grandchild))
        self.assertFalse(child2.is_my_parent(root_other))
        self.assertFalse(child2.is_my_parent(child_other))

        self.assertFalse(grandchild.is_my_parent(root))
        self.assertTrue(grandchild.is_my_parent(child1))
        self.assertFalse(grandchild.is_my_parent(child2))
        self.assertFalse(grandchild.is_my_parent(grandchild))
        self.assertFalse(grandchild.is_my_parent(root_other))
        self.assertFalse(grandchild.is_my_parent(child_other))

        pass

    def test_add_node(self):
        root = Node('root', None, None)
        child_linked = root.create_child('child_linked')
        child_unlinked = Node('child', root, None)

        self.assertTrue(root.is_my_child(child_linked))
        self.assertTrue(child_linked.is_my_parent(root))
        self.assertFalse(root.is_my_child(child_unlinked))
        self.assertTrue(child_unlinked.is_my_parent(root))

        root.add_child(child_unlinked)
        self.assertTrue(root.is_my_child(child_linked))
        self.assertTrue(child_linked.is_my_parent(root))
        self.assertTrue(root.is_my_child(child_unlinked))
        self.assertTrue(child_unlinked.is_my_parent(root))

        pass
