from kdtree.node import Node
from kdtree.region import Region, Bound
from kdtree.tree import BinSearchTree


def main():
    # create a new tree with dimension 2
    tree = BinSearchTree(2)

    # insert nodes into the tree
    tree.insert(Node((50, 50)))
    tree.insert(Node((10, 70)))
    tree.insert(Node((80, 85)))
    tree.insert(Node((25, 20)))
    tree.insert(Node((40, 85)))
    tree.insert(Node((70, 85)))
    tree.insert(Node((10, 60)))

    # create rectangle from a bound array as described in the article
    # element 2*j is lower bound and element (2*j)+1 is upper bound of dimension j
    rectangle1 = Region.from_bounds_array(69, 71, 84, 86)

    # create rectanglse as a list of Bound object
    rectangle2 = Region(Bound(69, 71), Bound(84, 86))

    # Search
    nodes = tree.regional_search(rectangle1)
    print("First search result {}".format(nodes))

    nodes = tree.regional_search(rectangle2)
    print("Second search result {}".format(nodes))


if __name__ == '__main__':
    main()
