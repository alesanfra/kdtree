from typing import Optional, List

from kdtree.node import Node
from kdtree.region import Region


class BinSearchTree:
    def __init__(self, dimension: int):
        if not isinstance(dimension, int) or dimension < 1:
            raise ValueError("Dimension must be a positive integer")

        self.dimension = dimension
        self._root = None
        self._current_bounds = None

    def set_root(self, node: Node):
        self._root = node
        self._root.disc = 0
        self._root.hison = None
        self._root.loson = None
        self._current_bounds = Region.from_node(node)

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
        self._current_bounds.resize_to_contain_node(node)
        return

    def region_search(self, rectangle) -> List[Node]:
        if len(rectangle) != 2 * self.dimension:
            raise ValueError("Invalid bound array")

        return self._region_search(self._root, Region.from_bounds_array(rectangle), self._current_bounds)

    def _region_search(self, node: Node, rectangle: Region, subtree_bounds: Region) -> List[Node]:
        if node is None or not rectangle.intersects_region(subtree_bounds):
            return []

        found = []
        if node in rectangle:
            found.append(node)

        bounds_l = subtree_bounds.clone()
        bounds_h = subtree_bounds.clone()
        j = node.disc

        bounds_l[j].upper = node.keys[j]  # current node is j-upper bound for LOSON
        bounds_h[j].lower = node.keys[j]  # current node is j-lower bound for HISON

        left = self._region_search(node.loson, rectangle, bounds_l)
        right = self._region_search(node.hison, rectangle, bounds_h)

        return found + left + right
