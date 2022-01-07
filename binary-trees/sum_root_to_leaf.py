
# 9.5 Sum the root-to-leaf paths in a binary tree
# The time complexity and space complexity are O(n) and O(h), respectively.
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# ele:
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_root_to_leaf(tree):

    def sum_root_to_leaf_helper(tree, partial_path_num=0):
        if not tree:
            return 0

        partial_path_num = partial_path_num*2+tree.data
        if not tree.left and not tree.right:  # leaf
            return partial_path_num
        # non-leaf
        return (sum_root_to_leaf_helper(tree.left, partial_path_num) + sum_root_to_leaf_helper(tree.right, partial_path_num))

    return sum_root_to_leaf_helper(tree)


root = Node(1)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(1)


print(sum_root_to_leaf(root))


# lc: Approach 1: Iterative Preorder Traversal.:
# Time complexity: O(N), where NN is a number of nodes, since one has to visit each node.
# Space complexity: up to O(H) to keep the stack, where HH is a tree height.

# Prerequisites: Bitwise Trick
# If you work with decimal representation, the conversion of 1->2 into 12 is easy. You start from curr_number = 1, then shift one register to the left and add the next digit: curr_number = 1 * 10 + 2 = 12.
# If you work with binaries 1 -> 1 -> 3, it's the same. You start from curr_number = 1, then shift one register to the left and add the next digit: curr_number = (1 << 1) | 1 = 3.
# remark* (1<<1):0010
#         |
#              1:0001
#         =    0011:3

# Intuition:
# Here we implement standard iterative preorder traversal with the stack:
# Push root into stack.
# While stack is not empty:
# Pop out a node from stack and update the current number.
# If the node is a leaf, update root-to-leaf sum.
# Push right and left child nodes into stack.
# Return root-to-leaf sum.

class Node2:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_root_to_leaf2(root):
    root_to_leaf = 0
    stack = [(root, 0)]

    while stack:
        root, curr_number = stack.pop()
        if root is not None:
            curr_number = (curr_number << 1) | root.data
            # if it's a leaf, update root-to-leaf sum
            if root.left is None and root.right is None:
                root_to_leaf += curr_number
            else:
                stack.append((root.right, curr_number))
                stack.append((root.left, curr_number))

    return root_to_leaf

#            1
#           / \
#          0   1
#         / \ / \
#        0  1 0  1

# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


root = Node2(1)
root.left = Node2(0)
root.right = Node2(1)
root.left.left = Node2(0)
root.left.right = Node2(1)
root.right.left = Node2(0)
root.right.right = Node2(1)


print(sum_root_to_leaf2(root))

# variant:
# https://www.geeksforgeeks.org/find-all-root-to-leaf-path-sum-of-a-binary-tree/
