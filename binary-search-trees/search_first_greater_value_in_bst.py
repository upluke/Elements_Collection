
# 14.2 Find the first key greater than a given value in a BST
# time: O(h), where h is the height of the tree
# space: O*=(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def find_first_greater_than_k(self, tree, k):
        subtree, lager_so_far = tree, None

        while subtree:
            if lager_so_far:
                print(subtree.data, "----", lager_so_far.data)
            if subtree.data > k:
                lager_so_far, subtree = subtree, subtree.left
            else:
                subtree = subtree.right
        return lager_so_far.data


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

print(tree.find_first_greater_than_k(tree.root, 3))
