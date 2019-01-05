from unittest import TestCase

from kdtree.node import Node


class TestNode(TestCase):
    def setUp(self):
        self.node = Node((20, 30, 40, 50), disc=0)

    def test_create_only_key(self):
        node = Node((1, 2, 3, 4))

        assert node.keys == (1, 2, 3, 4)
        assert node.disc is None
        assert node.loson is None
        assert node.hison is None

    def test_create_fail(self):
        with self.assertRaises(TypeError):
            Node('a string')

    def test_super_key(self):
        assert self.node.super_key(0) == (20, 30, 40, 50)
        assert self.node.super_key(1) == (30, 40, 50, 20)
        assert self.node.super_key(2) == (40, 50, 20, 30)
        assert self.node.super_key(3) == (50, 20, 30, 40)

    def test_super_key_negative(self):
        with self.assertRaises(ValueError):
            self.node.super_key(-1)

    def test_super_key_too_big(self):
        with self.assertRaises(ValueError):
            self.node.super_key(4)

    def test_successor_loson(self):
        q = Node((10, 1, 1, 1))

        successor, side = self.node.successor(q)

        assert successor is None
        assert side is Node.LOSON

    def test_successor_loson_equal(self):
        q = Node((20, 1, 1, 1))

        successor, side = self.node.successor(q)

        assert successor is None
        assert side is Node.LOSON

    def test_successor_hison(self):
        q = Node((21, 1, 1, 1))

        successor, side = self.node.successor(q)

        assert successor is None
        assert side is Node.HISON

    def test_successor_fail_different_dimensions(self):
        q = Node((21, 1))

        with self.assertRaises(ValueError):
            self.node.successor(q)

    def test_successor_fail_not_a_node(self):
        with self.assertRaises(TypeError):
            self.node.successor('not a node')

    def test_add_son_loson(self):
        q = Node((17, 1, 1, 1))

        self.node.add_son(q)

        assert self.node.loson is q

    def test_add_son_hison(self):
        q = Node((23, 1, 1, 1))

        self.node.add_son(q)

        assert self.node.hison is q

    def test_add_son_fail_different_dimensions(self):
        q = Node((21, 1))

        with self.assertRaises(ValueError):
            self.node.add_son(q)

    def test_add_son_fail_not_a_node(self):
        with self.assertRaises(TypeError):
            self.node.add_son('not a node')
