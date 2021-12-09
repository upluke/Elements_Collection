
# 9.4 Compute the LCA when nodes have parent pointers
# Lowest Common Ancestor of a Binary Tree III - LeetCode
#

# ele:
class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def lca(node0,
        node1):
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    # Makes node0 as the deeper node in order to simplify the code.
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


# ol:
# for more solutions: https://nicksma.medium.com/lowest-common-ancestors-and-variations-493588b699f3

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def find_lca(n1: BinaryTreeNode, n2: BinaryTreeNode) -> BinaryTreeNode:
    def get_depth(node: BinaryTreeNode) -> int:
        depth = 0
        while node and node.parent:
            node = node.parent
            depth += 1
        return depth

    d1 = get_depth(n1)
    d2 = get_depth(n2)

    while d1 > d2:
        n1 = n1.parent
        d1 -= 1

    while d2 > d1:
        n2 = n2.parent
        d2 -= 1

    while n1 != n2 and d1 > 0:
        d1 -= 1
        n1 = n1.parent
        n2 = n2.parent

    return n1.data
