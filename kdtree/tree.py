from typing import List, Optional

from .node import Node
from .region import Region


class BinSearchTree:
    def __init__(self, dimension: int):
        if not isinstance(dimension, int) or dimension < 1:
            raise ValueError("Dimension must be a positive integer")

        if dimension > Node.MAX_KEY_DIMENSION:
            raise ValueError("Maximum allowed dimension for node keys: {}".format(Node.MAX_KEY_DIMENSION))

        self.dimension = dimension
        self._root = None
        self._current_bounds = None

    def insert(self, node: Node) -> Optional[Node]:
        """Insert a node into the tree

        :param node: a Node having the same number of keys of the Tree
        :return: if the given node is already in the tree the method returns it, None otherwise
        """
        if len(node.keys) != self.dimension:
            raise ValueError("Node must have the same number of keys of the tree")

        if self._root is None:
            # setting the given node as root of the tree
            self._root = node
            self._root.discriminator = 0
            self._root.hison = None
            self._root.loson = None
            self._current_bounds = Region.from_node(node)
            return None

        parent = None
        son = self._root

        while son is not None:
            if son.keys == node.keys:
                return son  # Found the same node, return it

            # Move down
            parent = son
            son, _ = parent.successor(node)

        # Found a leaf where to insert new node
        parent.add_son(node)
        self._current_bounds.resize_to_contain_node(node)
        return None

    def regional_search(self, rectangle: Region) -> List[Node]:
        """Searches and returns all the nodes in the tree that fall within an (n-dimensional) rectangle given as input

        :param rectangle: n-dimensional Region passed as
        :return: list of nodes found the given region
        """
        if not isinstance(rectangle, Region):
            raise TypeError("rectangle must be an instance of Region")

        if rectangle.dimension != self.dimension:
            raise ValueError("Invalid bound array")

        return self.__regional_search(self._root, rectangle, self._current_bounds)

    def __regional_search(self, node: Node, rectangle: Region, subtree_bounds: Region) -> List[Node]:
        if node is None or not rectangle.intersects_region(subtree_bounds):
            return []

        found = []
        if node in rectangle:
            found.append(node)

        bounds_l = subtree_bounds.clone()
        bounds_h = subtree_bounds.clone()
        j = node.discriminator

        bounds_l[j].upper = node.keys[j]  # current node is j-upper bound for LOSON
        bounds_h[j].lower = node.keys[j]  # current node is j-lower bound for HISON

        left = self.__regional_search(node.loson, rectangle, bounds_l)
        right = self.__regional_search(node.hison, rectangle, bounds_h)

        return found + left + right
