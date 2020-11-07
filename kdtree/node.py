from enum import Enum, auto, unique
from typing import Tuple


@unique
class NodeSide(Enum):
    LOSON = auto()
    HISON = auto()


class Node:
    MAX_KEY_DIMENSION = 100000

    def __init__(self, keys: Tuple, discriminator=None):
        if not isinstance(keys, tuple):
            raise TypeError("keys must be a tuple")
        self.keys = keys
        self.discriminator = discriminator

        self.loson = None
        self.hison = None

    def __str__(self):
        return "<{}/{}>".format(str(self.keys), self.discriminator)

    def __repr__(self):
        return self.__str__()

    def super_key(self, discriminator: int):
        if discriminator < 0 or discriminator > (len(self.keys) - 1):
            raise ValueError("Invalid discriminator")
        return self.keys[discriminator:] + self.keys[:discriminator]

    def successor(self, q):
        if not isinstance(q, Node):
            raise TypeError("q must be an instance of Node")

        if len(self.keys) != len(q.keys):
            raise ValueError("nodes must have the same number of keys")

        j = self.discriminator

        if self.keys[j] > q.keys[j]:
            return self.loson, NodeSide.LOSON
        elif self.keys[j] < q.keys[j]:
            return self.hison, NodeSide.HISON
        elif self.super_key(j) > q.super_key(j):
            return self.loson, NodeSide.LOSON
        elif self.super_key(j) < q.super_key(j):
            return self.hison, NodeSide.HISON
        raise ValueError("Same node")

    def add_son(self, node):
        _, side = self.successor(node)

        if side is NodeSide.LOSON:
            self.loson = node
        else:
            self.hison = node

        node.discriminator = self.__next_discriminator()
        node.loson = node.hison = None

    def __next_discriminator(self):
        return (self.discriminator + 1) % len(self.keys)
