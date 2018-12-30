import copy
from typing import Optional

from kdtree import Bound
from kdtree.node import Node


class KDTree:
    def __init__(self, dimension: int):
        if not isinstance(dimension, int) or dimension < 1:
            raise ValueError("Dimension must be a positive integer")

        self.dimension = dimension
        self._root = None
        self._current_bounds = None

    def _update_current_bounds(self, keys):
        if self._current_bounds is None:
            self._current_bounds = [Bound(k, k) for k in keys]
        else:
            self._current_bounds = [Bound(lower=min(bound.lower, key), upper=max(bound.upper, key))
                                    for bound, key in zip(self._current_bounds, keys)]

    def set_root(self, node: Node):
        self._root = node
        self._root.disc = 0
        self._root.hison = None
        self._root.loson = None
        self._update_current_bounds(node.keys)

    def insert(self, node: Node) -> Optional[Node]:
        if self._root is None:
            self.set_root(node)
            return

        parent = None
        side = None
        son = self._root

        while son is not None:
            if son.keys == node.keys:
                return son  # Found the same node, return it

            # Move down
            parent = son
            son, side = son.successor(node)

        # Found leaf where to insert new node
        parent.add_son(node, side, self.dimension)
        self._update_current_bounds(node.keys)
        return

    def region_search(self, rectangle):
        if len(rectangle) != 2 * self.dimension:
            raise ValueError("Invalid bound array")

        rectangle = [Bound(rectangle[i], rectangle[i + 1]) for i in range(0, self.dimension * 2, 2)]
        return self._region_search(self._root, rectangle, self._current_bounds)

    def _region_search(self, node: Node, rectangle, bounds):
        if node is None or not self._bounds_intersect_region(bounds, rectangle):
            return []

        found = []
        if self._in_region(node, rectangle):
            found.append(node)

        bounds_l = copy.deepcopy(bounds)
        bounds_h = copy.deepcopy(bounds)
        j = node.disc

        bounds_l[j].upper = node.keys[j]  # current node is j-upper bound for LOSON
        bounds_h[j].lower = node.keys[j]  # current node is j-lower bound for HISON

        left = self._region_search(node.loson, rectangle, bounds_l)
        right = self._region_search(node.hison, rectangle, bounds_h)

        return found + left + right

    def _in_region(self, node, region):
        for i in range(self.dimension):
            if node.keys[i] < region[i].lower or region[i].upper < node.keys[i]:
                return False
        return True

    def _bounds_intersect_region(self, bounds, region):
        for i in range(self.dimension):
            if bounds[i].lower > region[i].upper or bounds[i].upper < region[i].lower:
                return False
        return True
