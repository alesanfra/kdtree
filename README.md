![Build](https://github.com/alesanfra/kdtree/workflows/Build%20and%20Test/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alesanfra_kdtree&metric=alert_status)](https://sonarcloud.io/dashboard?id=alesanfra_kdtree)
[![codecov](https://codecov.io/gh/alesanfra/kdtree/branch/master/graph/badge.svg?token=GA5KCLADD6)](https://codecov.io/gh/alesanfra/kdtree)

# KDTree

Implementation of a multidimensional binary search tree for associative searching

## References

Jon Louis Bentley. Multidimensional binary search tree used for associative searching. September 1975.

## Usage

```python
from kdtree import BinSearchTree, Bound, Node, Region


# Create a new tree
tree = BinSearchTree(dimension=2)

# Insert some nodes into the tree
tree.insert(Node((50, 50)))
tree.insert(Node((10, 70)))
tree.insert(Node((80, 85)))
tree.insert(Node((25, 20)))
tree.insert(Node((40, 85)))
tree.insert(Node((70, 85)))
tree.insert(Node((10, 60)))

# Create rectangle from a bound array as described in the article
# Element 2*j is lower bound and element (2*j)+1 is upper bound of dimension j
rectangle_1 = Region.from_bounds_array(69, 71, 84, 86)

# Create rectangles as a list of Bound object
rectangle_2 = Region(Bound(69, 71), Bound(84, 86))

# Search
nodes = tree.regional_search(rectangle_1)
print("Nodes within region:", nodes)
```