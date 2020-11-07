import pytest

from kdtree import BinSearchTree


class TestCreateTree:
    @pytest.mark.parametrize("dimension", [1, 2, 100000])
    def test_create_tree(self, dimension):
        tree = BinSearchTree(dimension)

        assert tree.dimension == dimension

    @pytest.mark.parametrize("dimension", [1000001, 0, -1, 2.2, "3"])
    def test_create_tree_fails(self, dimension):
        with pytest.raises(ValueError):
            BinSearchTree(dimension)
