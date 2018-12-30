import copy
from typing import Optional, List, Tuple


class Bound:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


class Node:
    LOSON = 'LOSON'
    HISON = 'HISON'

    def __init__(self, keys: Tuple, loson=None, hison=None, disc=None):
        if not isinstance(keys, tuple):
            raise TypeError("keys must be a tuple")
        self.keys = keys
        self.loson = loson
        self.hison = hison
        self.disc = disc

    def super_key(self, discriminator):
        return self.keys[discriminator:] + self.keys[:discriminator]


class KDTree:
    def __init__(self, dimension: int, root: Node = None):
        if dimension < 1:
            raise ValueError("Dimension must be a positive integer")

        self.dimension = dimension
        self.root = root

    def insert(self, node: Node) -> Optional[Node]:
        if self.root is None:
            self.root = node
            self.root.disc = 0
            self.root.hison = None
            self.root.loson = None
            return None

        q = self.root
        while q is not None:
            if q.keys == node.keys:
                return q

            son, side = self._successor(q, node)

            if son is None:
                node.disc = self._next_disc(q.disc)
                node.loson = None
                node.hison = None
                if side is Node.LOSON:
                    q.loson = node
                else:
                    q.hison = node
                return None
            q = son

    def _next_disc(self, disc):
        return (disc + 1) % self.dimension

    @staticmethod
    def _successor(p: Node, q: Node):
        j = p.disc

        if p.keys[j] > q.keys[j]:
            return p.loson, Node.LOSON
        elif p.keys[j] < q.keys[j]:
            return p.hison, Node.HISON
        elif p.super_key(j) > q.super_key(j):
            return p.loson, Node.LOSON
        elif p.super_key(j) < q.super_key(j):
            return p.hison, Node.HISON
        raise ValueError("Same node")

    def region_search(self, rectangle):
        if len(rectangle) != 2 * self.dimension:
            raise ValueError("Invalid bound array")

        rectangle = [Bound(rectangle[i], rectangle[i + 1]) for i in range(0, self.dimension * 2, 2)]
        bounds = [Bound(-float('Inf'), float('Inf')) for _ in range(self.dimension)]
        return self._region_search(self.root, rectangle, bounds)

    def _region_search(self, node: Node, rectangle, bounds):
        found = []
        if self._in_region(node, rectangle):
            found.append(node)

        bounds_l = copy.deepcopy(bounds)
        bounds_h = copy.deepcopy(bounds)
        j = node.disc

        bounds_l[j].upper = node.keys[j]  # current node is j-upper bound for LOSON
        bounds_h[j].lower = node.keys[j]  # current node is j-lower bound for HISON

        if node.loson and self._bounds_intersect_region(bounds_l, rectangle):
            found += self._region_search(node.loson, rectangle, bounds_l)

        if node.hison and self._bounds_intersect_region(bounds_h, rectangle):
            found += self._region_search(node.hison, rectangle, bounds_h)

        return found

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
