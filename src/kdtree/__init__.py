from kdtree.node import Node


class Bound:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return str((self.lower, self.upper))

    def __repr__(self):
        return str((self.lower, self.upper))
