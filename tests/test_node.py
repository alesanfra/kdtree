import pytest

from kdtree import Node, NodeSide


class TestNode:
    @pytest.fixture
    def node(self):
        return Node((20, 30, 40, 50), discriminator=0)

    def test_create_only_key(self):
        node = Node((1, 2, 3, 4))

        assert node.keys == (1, 2, 3, 4)
        assert node.discriminator is None
        assert node.loson is None
        assert node.hison is None

    def test_create_fail(self):
        with pytest.raises(TypeError):
            Node("a string")

    def test_super_key(self, node):
        assert node.super_key(0) == (20, 30, 40, 50)
        assert node.super_key(1) == (30, 40, 50, 20)
        assert node.super_key(2) == (40, 50, 20, 30)
        assert node.super_key(3) == (50, 20, 30, 40)

    def test_super_key_negative(self, node):
        with pytest.raises(ValueError):
            node.super_key(-1)

    def test_super_key_too_big(self, node):
        with pytest.raises(ValueError):
            node.super_key(4)

    def test_successor_loson(self, node):
        q = Node((10, 1, 1, 1))

        successor, side = node.successor(q)

        assert successor is None
        assert side is NodeSide.LOSON

    def test_successor_loson_equal(self, node):
        q = Node((20, 1, 1, 1))

        successor, side = node.successor(q)

        assert successor is None
        assert side is NodeSide.LOSON

    def test_successor_hison(self, node):
        q = Node((21, 1, 1, 1))

        successor, side = node.successor(q)

        assert successor is None
        assert side is NodeSide.HISON

    def test_successor_fail_different_dimensions(self, node):
        q = Node((21, 1))

        with pytest.raises(ValueError):
            node.successor(q)

    def test_successor_fail_not_a_node(self, node):
        with pytest.raises(TypeError):
            node.successor("not a node")

    def test_add_son_loson(self, node):
        q = Node((17, 1, 1, 1))

        node.add_son(q)

        assert node.loson is q

    def test_add_son_hison(self, node):
        q = Node((23, 1, 1, 1))

        node.add_son(q)

        assert node.hison is q

    def test_add_son_fail_different_dimensions(self, node):
        q = Node((21, 1))

        with pytest.raises(ValueError):
            node.add_son(q)

    def test_add_son_fail_not_a_node(self, node):
        with pytest.raises(TypeError):
            node.add_son("not a node")
