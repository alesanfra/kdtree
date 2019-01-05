from unittest import TestCase

from kdtree.node import Node
from kdtree.tree import BinSearchTree


class TestRegionalSearch(TestCase):
    def setUp(self):
        self.tree = BinSearchTree(2)
        self.tree.insert(Node(keys=(50, 50)))
        self.tree.insert(Node(keys=(10, 70)))
        self.tree.insert(Node(keys=(80, 85)))
        self.tree.insert(Node(keys=(25, 20)))
        self.tree.insert(Node(keys=(40, 85)))
        self.tree.insert(Node(keys=(70, 85)))
        self.tree.insert(Node(keys=(10, 60)))

    def test_search_one(self):
        nodes = self.tree.regional_search((69, 71, 84, 86))

        assert len(nodes) == 1
        assert nodes[0].keys == (70, 85)

    def test_search_all(self):
        nodes = self.tree.regional_search((0, 100, 0, 100))

        assert len(nodes) == 7
        assert nodes[0].keys == (50, 50)
        assert nodes[1].keys == (10, 70)
        assert nodes[2].keys == (25, 20)

    def test_search_two(self):
        nodes = self.tree.regional_search((40, 70, 70, 90))

        assert len(nodes) == 2
        assert nodes[0].keys == (40, 85)
        assert nodes[1].keys == (70, 85)

    def test_search_three(self):
        nodes = self.tree.regional_search((10, 40, 60, 85))

        assert len(nodes) == 3
        assert nodes[0].keys == (10, 70)
        assert nodes[1].keys == (10, 60)
        assert nodes[2].keys == (40, 85)

    def test_search_root(self):
        nodes = self.tree.regional_search((50, 50, 50, 50))

        assert len(nodes) == 1
        assert nodes[0].keys == (50, 50)
