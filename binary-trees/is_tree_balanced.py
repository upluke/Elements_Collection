# 9.1 Test if a binary tree is height-balanced
# The program implements a postorder traversal with some calls possibly being eliminated because of early termination. Specifically, if any left subtree is not height-balanced we do not need to visit the corresponding right subtree. The function call stack corresponds to a sequence of calls from the root through the unique path to the current node, and the stack height is therefore bounded by the height of the tree, leading to an O(h) space bound. The time complexity is the same as that for a postorder traversal, namely O(n).
#
# how to tell a unbalanced tree: https://cs.stackexchange.com/questions/54171/is-a-balanced-binary-tree-a-complete-binary-tree
# namedtuple: https://realpython.com/python-namedtuple/
import collections


class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_balanced_binary_tree(tree):
    balancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    # first value of the return value indictaes if tree is balanced, and if balanced the second value of the return value is the height of tree

    def check_balanced(tree):
        if not tree:
            return balancedStatusWithHeight(balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height)+1
        return balancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
print(is_balanced_binary_tree(root))


"""
gfg:
Python3 program to check if a tree is height-balanced
"""
# A binary tree Node


class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to find height of binary tree


def height(root):

    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# function to check if tree is height-balanced or not


def isBalanced(root):

    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    print(lh, rh)
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True

    # if we reach here means tree is not
    # height-balanced tree
    return False


# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")

# This code is contributed by Shweta Singh


#          1
#         / \
#        2   3
#       / \
#      4   5
#     /
#    8
