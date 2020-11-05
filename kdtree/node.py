from typing import Tuple


class Node:
    MAX_KEY_DIMENSION = 100000
    LOSON = object()
    HISON = object()

    def __init__(self, keys: Tuple, loson=None, hison=None, disc=None):
        if not isinstance(keys, tuple):
            raise TypeError("keys must be a tuple")
        self.keys = keys
        self.loson = loson
        self.hison = hison
        self.disc = disc

    def __str__(self):
        return "<{}/{}>".format(str(self.keys), self.disc)

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

        j = self.disc

        if self.keys[j] > q.keys[j]:
            return self.loson, self.LOSON
        elif self.keys[j] < q.keys[j]:
            return self.hison, self.HISON
        elif self.super_key(j) > q.super_key(j):
            return self.loson, self.LOSON
        elif self.super_key(j) < q.super_key(j):
            return self.hison, self.HISON
        raise ValueError("Same node")

    def add_son(self, node):
        _, side = self.successor(node)

        if side is Node.LOSON:
            self.loson = node
        else:
            self.hison = node

        node.disc = self.__next_discriminator()
        node.loson = node.hison = None

    def __next_discriminator(self):
        return (self.disc + 1) % len(self.keys)
