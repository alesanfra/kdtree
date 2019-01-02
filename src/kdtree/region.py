import copy


class Bound:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return str((self.lower, self.upper))

    def __repr__(self):
        return str((self.lower, self.upper))

    def include(self, coordinate):
        self.lower = min(self.lower, coordinate)
        self.upper = max(self.upper, coordinate)


class Region:
    def __init__(self, bounds):
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

    @classmethod
    def from_bounds_array(cls, bounds_array):
        return cls([Bound(bounds_array[i], bounds_array[i + 1]) for i in range(0, len(bounds_array), 2)])

    @classmethod
    def from_node(cls, node):
        return cls([Bound(k, k) for k in node.keys])

    def clone(self):
        return copy.deepcopy(self)

    def resize_to_contain_node(self, node):
        for bound, coordinate in zip(self._bounds, node.keys):
            bound.include(coordinate)

    def contains_node(self, node):
        for key, bound in zip(node.keys, self._bounds):
            if key < bound.lower or bound.upper < key:
                return False
        return True

    def intersects_region(self, other_region):
        for this_bound, other_bound in zip(self, other_region):
            if this_bound.lower > other_bound.upper or this_bound.upper < other_bound.lower:
                return False
        return True
