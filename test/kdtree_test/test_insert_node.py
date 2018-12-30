from unittest import TestCase

from kdtree.node import Node
from kdtree.tree import KDTree


class TestInsertNode(TestCase):
    def test_insert_empty(self):
        tree = KDTree(2)
        node = Node(keys=(1, 2))

        r = tree.insert(node)

        assert r is None
        assert tree._root is node
        assert tree._root.super_key(0) == node.super_key(0)
        assert node.disc == 0
        assert node.loson is None
        assert node.hison is None

    def test_insert_two_nodes(self):
        tree = KDTree(2)
        node1 = Node(keys=(50, 50))
        node2 = Node(keys=(10, 70))

        tree.insert(node1)
        r = tree.insert(node2)

        assert r is None
        assert tree._root is node1
        assert tree._root.loson is node2
        assert node2.disc == 1
        assert node2.loson is None
        assert node2.hison is None
