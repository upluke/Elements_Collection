
# 9.2 Test if a binary tree is symmetric
# the time complexity and space complexity are O(n) and O(h), respectively, where n is the number of nodes in the tree and h is the height of the tree
# https://www.baeldung.com/cs/binary-tree-is-symmetric

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# is_tree_symmetric.py


def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(4)
root.right.left = newNode(4)
root.right.right = newNode(3)
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
print(is_symmetric(root))
