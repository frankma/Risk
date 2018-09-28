from typing import List


class Node(object):
    JOINER_NAME = "#^#"
    JOINER_TAGS = "."

    def __init__(self, name: str, tags: List, parent, children: List):
        self._name = name
        self._tags = tags
        self._parent = parent
        self._children = children
        self._next_child_seq = children.__len__()  # allow bypassing for possible prune of children
        pass

    def get_node_level(self):
        return self._tags.__len__()

    def get_tags(self):
        return self._tags

    def get_tags_string(self):
        tags_string = ["%s" % x for x in self._tags]
        return Node.JOINER_TAGS.join(tags_string)

    def get_parent(self):
        return self._parent

    def get_children(self):
        return self._children

    def get_name(self):
        return self._name

    def get_name_full(self):
        name_full = self.get_name()
        if self.is_root():
            name_full = self.get_parent().get_name_full() + Node.JOINER_NAME + name_full
        return name_full

    def get_root(self):
        if self.is_root():
            return self
        else:
            return self.get_parent().get_root()
        pass

    def __hash__(self):
        return hash(self.get_tags_string())

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def create_child(self, child_name: str):
        child_tags = self._tags.copy()
        child_tags.append(self._next_child_seq)
        child = Node(child_name, child_tags, self, [])
        self._children.append(child)
        self._next_child_seq += 1
        return child

    def add_child(self, node):
        if self.is_my_child(node) and not self.is_child_added(node):
            self._children.append(node)
            self._next_child_seq = max(node.get_tags()[-1], self._next_child_seq) + 1
        pass

    def is_root(self):
        return self._tags.__len__() == 1

    def is_my_child(self, node):
        return self.__eq__(node.get_parent())

    def is_child_added(self, node):
        is_added = False
        for child in self._children:
            is_added |= child.__eq__(node)
        return is_added

    def check_self_consistency(self):
        is_consistent = True
        self_level = self.get_node_level()
        is_consistent &= self.get_name_full().split(Node.JOINER_NAME).__len__() == self_level
        child_num_collection = []
        for child in self._children:
            is_consistent &= child.get_parent().get_name_full() == self.get_name_full()
            is_consistent &= child.get_node_level() == self_level + 1
            child_num_collection.__add__(child.get_tags()[-1])
        child_num_collection.sort()
        # TODO: find uniqueness for the child
        return is_consistent
