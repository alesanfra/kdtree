from typing import Tuple


class Node:
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

    def super_key(self, discriminator):
        return self.keys[discriminator:] + self.keys[:discriminator]

    def successor(self, q):
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
