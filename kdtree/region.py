import copy

from .node import Node


class Bound:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return str((self.lower, self.upper))

    def __repr__(self):
        return str((self.lower, self.upper))

    def extend_to_include_point(self, coordinate):
        self.lower = min(self.lower, coordinate)
        self.upper = max(self.upper, coordinate)


class Region:
    def __init__(self, *bounds):
        self._bounds = bounds

    def __contains__(self, item):
        return self.contains_node(item)

    def __iter__(self):
        for b in self._bounds:
            yield b

    def __getitem__(self, item):
        return self._bounds[item]

    def __str__(self):
        return str(self._bounds)

    def __repr__(self):
        return str(self._bounds)

    @property
    def dimension(self):
        return len(self._bounds)

    @classmethod
    def from_bounds_array(cls, *bounds_array):
        if len(bounds_array) % 2 != 0:
            raise ValueError("bounds_array must have an even number of elements")

        return cls(*[Bound(bounds_array[i], bounds_array[i + 1]) for i in range(0, len(bounds_array), 2)])

    @classmethod
    def from_node(cls, node: Node):
        cls._check_node_type(node)

        return cls(*[Bound(k, k) for k in node.keys])

    def clone(self):
        return copy.deepcopy(self)

    def resize_to_contain_node(self, node: Node):
        self._check_node_type(node)

        for bound, coordinate in zip(self._bounds, node.keys):
            bound.extend_to_include_point(coordinate)

    def contains_node(self, node: Node):
        self._check_node_type(node)

        for key, bound in zip(node.keys, self._bounds):
            if key < bound.lower or bound.upper < key:
                return False
        return True

    def intersects_region(self, other_region):
        if not isinstance(other_region, Region):
            raise TypeError("other_region must be in instance of Region")

        for this_bound, other_bound in zip(self, other_region):
            if this_bound.lower > other_bound.upper or this_bound.upper < other_bound.lower:
                return False
        return True

    @classmethod
    def _check_node_type(cls, node):
        if not isinstance(node, Node):
            raise TypeError("node must be an instance of Node")
