from unittest import TestCase

from kdtree.node import Node
from kdtree.region import Region, Bound


class TestRegion(TestCase):
    def setUp(self):
        self.region = Region.from_bounds_array(1, 10, 1, 10)

    def test_create(self):
        region = Region(Bound(1, 10), Bound(2, 20))

        assert len(region._bounds) == 2
        assert isinstance(region[0], Bound)
        assert isinstance(region[1], Bound)
        assert region[0].lower == 1
        assert region[0].upper == 10
        assert region[1].lower == 2
        assert region[1].upper == 20

    def test_create_from_bounds_array(self):
        region = Region.from_bounds_array(1, 10, 2, 20)

        assert len(region._bounds) == 2
        assert isinstance(region[0], Bound)
        assert isinstance(region[1], Bound)
        assert region[0].lower == 1
        assert region[0].upper == 10
        assert region[1].lower == 2
        assert region[1].upper == 20

    def test_create_from_bounds_array_odd(self):
        with self.assertRaises(ValueError):
            Region.from_bounds_array(1, 10, 2)

    def test_create_from_node(self):
        region = Region.from_node(Node((1, 2, 4)))

        assert len(region._bounds) == 3
        assert isinstance(region[0], Bound)
        assert isinstance(region[1], Bound)
        assert isinstance(region[2], Bound)
        assert region[0].lower == 1
        assert region[0].upper == 1
        assert region[1].lower == 2
        assert region[1].upper == 2
        assert region[2].lower == 4
        assert region[2].upper == 4

    def test_resize_to_contain_node(self):
        assert self.region[0].upper == 10
        assert self.region[1].upper == 10

        self.region.resize_to_contain_node(Node((12, 13)))

        assert self.region[0].upper == 12
        assert self.region[1].upper == 13

    def test_contains_node(self):
        assert self.region.contains_node(Node((12, 13))) is False
        assert self.region.contains_node(Node((9, 9))) is True

    def test_intersects_region(self):
        r = Region.from_bounds_array(2, 4, 9, 13)

        assert self.region.intersects_region(r) is True

    def test_not_intersects_region(self):
        r = Region.from_bounds_array(2, 4, 11, 13)

        assert self.region.intersects_region(r) is False
