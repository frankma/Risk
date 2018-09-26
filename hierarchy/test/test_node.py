from unittest import TestCase
from hierarchy.src.node import Node


class TestNode(TestCase):
    def test_get_name_full(self):
        nodes = []

        root = Node("first generation - root", [0], None, [])
        nodes.append(root)

        child_1 = root.create_child("second generation - first child")
        child_2 = root.create_child("second generation - second child")
        nodes.append(child_1)
        nodes.append(child_2)

        grand_child_1 = child_1.create_child("third generation - first child")
        grand_child_2 = child_1.create_child("third generation - second child")
        grand_child_3 = child_2.create_child("third generation - third child")
        grand_child_4 = child_1.create_child("third generation - fourth child")
        nodes.append(grand_child_1)
        nodes.append(grand_child_2)
        nodes.append(grand_child_3)
        nodes.append(grand_child_4)

        grand_grand_child_1 = grand_child_3.create_child("fourth generation first child")
        nodes.append(grand_grand_child_1)

        for node in nodes:
            print(node.get_name_full())
        for node in nodes:
            print(node.get_tags())

        name_full = root.get_name_full()
        name_full_split = name_full.split(Node.JOINER_NAME)
        self.assertEquals(root.get_node_level(), name_full_split.__len__(), root.get_tags().__len__())

        for node in [child_1, child_2]:
            name_full = node.get_name_full()
            name_full_split = name_full.split(Node.JOINER_NAME)
            self.assertEquals(node.get_node_level(), name_full_split.__len__(), node.get_tags().__len__())

        for node in [grand_child_1, grand_child_2, grand_child_3, grand_child_4]:
            name_full = node.get_name_full()
            name_full_split = name_full.split(Node.JOINER_NAME)
            self.assertEquals(node.get_node_level(), name_full_split.__len__(), node.get_tags().__len__())

        for node in [grand_grand_child_1]:
            name_full = node.get_name_full()
            name_full_split = name_full.split(Node.JOINER_NAME)
            self.assertEquals(node.get_node_level(), name_full_split.__len__(), node.get_tags().__len__())
        pass

    def test_get_root(self):
        root = Node("root", [0], None, [])
        child = root.create_child("child")
        grandchild = child.create_child("grandchild")

        self.assertEqual(child.get_root().get_name_full(), grandchild.get_root().get_name_full())
        self.assertEquals(1, child.get_root().get_node_level(), grandchild.get_root().get_node_level())
        pass

    def test_check_self_consistency(self):
        root = Node("root", [0], None, [])
        # a properly created child
        child_consistent = root.create_child("child_consistent")
        # grandchild indeed but set to child level
        child_inconsistent = Node("child_inconsistent", [0, 2], child_consistent, [])
        self.assertTrue(root.check_self_consistency())
        self.assertTrue(child_consistent.check_self_consistency())
        self.assertFalse(child_inconsistent.check_self_consistency())
        pass

    def test_is_my_child(self):
        root = Node("root", [0], None, [])

        pass
