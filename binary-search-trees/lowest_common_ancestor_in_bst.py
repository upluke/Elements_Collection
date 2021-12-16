# 14.4 Compute the LCA in a BST
# Since we descend one level with each iteration, the time complexity is O(h),
# where h is the height of the tree.
# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

# Input: LCA of 10 and 14
# Output:  12
# Explanation: 12 is the closest node to both 10 and 14
# which is a ancestor of both the nodes.

# Input: LCA of 8 and 14
# Output:  8
# Explanation: 8 is the closest node to both 8 and 14
# which is a ancestor of both the nodes.

# Input: LCA of 10 and 22
# Output:  20
# Explanation: 20 is the closest node to both 10 and 22
# which is a ancestor of both the nodes.

# ele:
# input nodes are nonempty and the key at s is less than or equal to that at b
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


def find_lca(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right  # LCA must be in tree's right child
        while tree.data > b.data:
            tree = tree.left  # LCA must be in tree's left child
    # now, s.data <=tree.data && tree.data <=b.data
    return tree.data


#     9
#    / \
#   5   11
#  / \
# 3   7
tree = BST()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

print(find_lca(tree.root, tree.root.left.left, tree.root.right))  # 9, 3, 11


# gfg:
# Time Complexity: O(h).
# The time Complexity of the above solution is O(h), where h is the height of the tree.
# Space Complexity: O(h).
# If recursive stack space is ignored, the space complexity of the above solution is constant.


class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1, n2):

    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root

#            20
#           /  \
#          8    22
#         / \
#        4  12
#           / \
#          10  14


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print(t.data)


# gfg:
# Time Complexity: O(h).
# The Time Complexity of the above solution is O(h), where h is the height of the tree.
# Space Complexity: O(1).
# The space complexity of the above solution is constant.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find LCA of n1 and n2.
# The function assumes that both
# n1 and n2 are present in BST


def lca(root, n1, n2):
    while root:
        # If both n1 and n2 are smaller than root,
        # then LCA lies in left
        if root.data > n1 and root.data > n2:
            root = root.left

        # If both n1 and n2 are greater than root,
        # then LCA lies in right
        elif root.data < n1 and root.data < n2:
            root = root.right

        else:
            break

    return root


#            20
#           /  \
#          8    22
#         / \
#        4  12
#           / \
#          10  14


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print(t.data)

n1 = 8
n2 = 14
t = lca(root, n1, n2)
print(t.data)

n1 = 10
n2 = 22
t = lca(root, n1, n2)
print(t.data)
