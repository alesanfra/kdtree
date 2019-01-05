from unittest import TestCase

from kdtree.tree import BinSearchTree


class TestCreateTree(TestCase):
    def test_create_1_dimension(self):
        tree = BinSearchTree(1)

        assert tree.dimension == 1

    def test_create_2_dimensions(self):
        tree = BinSearchTree(2)

        assert tree.dimension == 2

    def test_create_max_dimensions(self):
        tree = BinSearchTree(100000)

        assert tree.dimension == 100000

    def test_create_fail_too_big(self):
        with self.assertRaises(ValueError):
            BinSearchTree(1000001)

    def test_create_fail_zero(self):
        with self.assertRaises(ValueError):
            BinSearchTree(0)

    def test_create_fail_negative(self):
        with self.assertRaises(ValueError):
            BinSearchTree(-1)

    def test_create_fail_float(self):
        with self.assertRaises(ValueError):
            BinSearchTree(2.2)

    def test_create_fail_not_int(self):
        with self.assertRaises(ValueError):
            BinSearchTree('3')
