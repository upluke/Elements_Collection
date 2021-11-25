# 14.3 Find the k largest elements in a BST
# The time complexity is O(h+k), which can be much better than performing a conventional inorder walk, e.g., when the tree is balanced and k is small. The complexity bound comes from the observation that the number of times the program desends in the tree can be at most h more than the number of times it ascends the tree, and each ascent happens after we visit a node in the result. After k nodes have been added to the result, the program stops.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        # Perform reverse inorder traversal.
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


# .    9
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


print(find_k_largest_in_bst(tree.root, 2))  # [11, 9]
# binary_tree(int)	int	array(int)
# [3, 2, 5, 1, null, 4, 6]	2	[6, 5]	TODO
# [1]	1	[1]	TODO
# [5, 1]	2	[5, 1]	TODO
# [3, 1, 5]	2	[5, 3]	TODO
# [7, 3, 10, 1]	2	[10, 7]	TODO
# [11, 6, 14, 1, 10]	5	[14, 11, 10, 6, 1]	TODO


# varient:
# https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
