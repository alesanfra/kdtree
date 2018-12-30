from unittest import TestCase

from kdtree import KDTree, Node


class TestRegionalSearch(TestCase):
    def setUp(self):
        self.tree = KDTree(2)
        self.tree.insert(Node(keys=(50, 50)))
        self.tree.insert(Node(keys=(10, 70)))
        self.tree.insert(Node(keys=(80, 85)))
        self.tree.insert(Node(keys=(25, 20)))
        self.tree.insert(Node(keys=(40, 85)))
        self.tree.insert(Node(keys=(70, 85)))
        self.tree.insert(Node(keys=(10, 60)))

    def test_search(self):
        nodes = self.tree.region_search((69, 71, 84, 86))

        assert len(nodes) == 1
        assert nodes[0].keys == (70, 85)
