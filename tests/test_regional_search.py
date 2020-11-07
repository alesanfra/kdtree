import pytest

from kdtree import BinSearchTree, Node, Region


class TestRegionalSearch:
    @pytest.fixture
    def tree(self):
        tree = BinSearchTree(2)
        tree.insert(Node(keys=(50, 50)))
        tree.insert(Node(keys=(10, 70)))
        tree.insert(Node(keys=(80, 85)))
        tree.insert(Node(keys=(25, 20)))
        tree.insert(Node(keys=(40, 85)))
        tree.insert(Node(keys=(70, 85)))
        tree.insert(Node(keys=(10, 60)))
        return tree

    def test_search_one(self, tree):
        nodes = tree.regional_search(Region.from_bounds_array(69, 71, 84, 86))

        assert len(nodes) == 1
        assert nodes[0].keys == (70, 85)

    def test_search_all(self, tree):
        nodes = tree.regional_search(Region.from_bounds_array(0, 100, 0, 100))

        assert len(nodes) == 7
        assert nodes[0].keys == (50, 50)
        assert nodes[1].keys == (10, 70)
        assert nodes[2].keys == (25, 20)

    def test_search_two(self, tree):
        nodes = tree.regional_search(Region.from_bounds_array(40, 70, 70, 90))

        assert len(nodes) == 2
        assert nodes[0].keys == (40, 85)
        assert nodes[1].keys == (70, 85)

    def test_search_three(self, tree):
        nodes = tree.regional_search(Region.from_bounds_array(10, 40, 60, 85))

        assert len(nodes) == 3
        assert nodes[0].keys == (10, 70)
        assert nodes[1].keys == (10, 60)
        assert nodes[2].keys == (40, 85)

    def test_search_root(self, tree):
        nodes = tree.regional_search(Region.from_bounds_array(50, 50, 50, 50))

        assert len(nodes) == 1
        assert nodes[0].keys == (50, 50)

    def test_search_fail_different_dimensions(self, tree):
        with pytest.raises(ValueError):
            tree.regional_search(Region.from_bounds_array(50, 50, 50, 50, 30, 30))

    def test_search_fail_not_a_region(self, tree):
        with pytest.raises(TypeError):
            tree.regional_search("not a region")
