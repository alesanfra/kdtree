from kdtree import BinSearchTree, Bound, Node, Region


def test_integration():
    # create a new tree with dimension == 2
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
    rectangle_1 = Region.from_bounds_array(69, 71, 84, 86)

    # create rectangles as a list of Bound object
    rectangle_2 = Region(Bound(69, 71), Bound(84, 86))

    # Search
    nodes = tree.regional_search(rectangle_1)
    print("First search result {}".format(nodes))

    nodes = tree.regional_search(rectangle_2)
    print("Second search result {}".format(nodes))
