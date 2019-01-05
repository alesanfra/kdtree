from random import randint
from unittest import TestCase

from kdtree.node import Node
from kdtree.tree import BinSearchTree


class TestInsertNode(TestCase):
    def test_insert_empty(self):
        tree = BinSearchTree(2)
        node = Node(keys=(1, 2))

        r = tree.insert(node)

        assert r is None
        assert tree._root is node
        assert tree._root.super_key(0) == node.super_key(0)
        assert node.disc == 0
        assert node.loson is None
        assert node.hison is None

    def test_insert_two_nodes(self):
        tree = BinSearchTree(2)
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

    def test_insert_wrong_dimension(self):
        tree = BinSearchTree(3)
        node1 = Node(keys=(50, 50))

        with self.assertRaises(ValueError):
            tree.insert(node1)

    def test_insert_100_dimension_nodes(self):
        tree = BinSearchTree(100)
        node1 = Node(keys=tuple(i for i in range(1, 101)))
        node2 = Node(keys=tuple(i for i in range(2, 102)))

        r = tree.insert(node1)
        assert r is None
        assert tree._root is node1
        assert node1.disc == 0
        assert node1.loson is None
        assert node1.hison is None

        r = tree.insert(node2)
        assert r is None
        assert tree._root is node1
        assert tree._root.hison is node2
        assert node2.disc == 1
        assert node2.loson is None
        assert node2.hison is None

    def test_insert_1000_nodes(self):
        tree = BinSearchTree(3)
        nodes = []

        for i in range(1000):
            keys = randint(-10000, 10000), randint(-10000, 10000), randint(-10000, 10000)
            node = Node(keys=keys)
            nodes.append(node)
            tree.insert(node)

        assert tree._root == nodes[0]

    def test_max_dimension_tree(self):
        tree = BinSearchTree(100000)
        node1 = Node(keys=tuple(i for i in range(1, 100001)))
        node2 = Node(keys=tuple(i for i in range(2, 100002)))

        r = tree.insert(node1)
        assert r is None
        assert tree._root is node1
        assert node1.disc == 0
        assert node1.loson is None
        assert node1.hison is None

        r = tree.insert(node2)
        assert r is None
        assert tree._root is node1
        assert tree._root.hison is node2
        assert node2.disc == 1
        assert node2.loson is None
        assert node2.hison is None
