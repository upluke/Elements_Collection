# 9.3 Compute the lowest common ancestor in a binary tree
# Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not have a parent filed

# Example 1:
#            3
#          /   \
#         5     1
#        / \   / \
#       6   2 0   8
#          / \
#         7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# gfg:
# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2

# A binary tree node
import functools
import collections


class newNode:
    # Constructor to create a new binary node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree


def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's data, report
    #  the presence by returning root (Note that if a data is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.data == n1 or root.data == n2:
        return root

    # Look for datas in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one data
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


root = newNode(3)
root.left = newNode(5)
root.right = newNode(1)
root.left.left = newNode(6)
root.left.right = newNode(2)
root.right.left = newNode(0)
root.right.right = newNode(8)
root.left.right.left = newNode(7)
root.left.right.right = newNode(4)


print(findLCA(root, 5, 4).data)


# elelemt:
# The algorithm is structually similar to a recursive postorder traveral, and the complexities are the same. Specifically, the time complexity and space complexity are O(n) and O(h), respectively, where h is the height of the tree.


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def lca(tree, node0, node1):

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(num_target_nodes=0, ancestor=None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        num_target_nodes = (left_result.num_target_nodes +
                            right_result.num_target_nodes +
                            (node0, node1).count(tree))
        return Status(num_target_nodes,
                      tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


root = BinaryTreeNode(3)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(1)
root.left.left = BinaryTreeNode(6)
root.left.right = BinaryTreeNode(2)
root.right.left = BinaryTreeNode(0)
root.right.right = BinaryTreeNode(8)
root.left.right.left = BinaryTreeNode(7)
root.left.right.right = BinaryTreeNode(4)


print(lca(root, root.left, root.left.right.right).data)
