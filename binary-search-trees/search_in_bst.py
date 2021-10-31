# 14.0
class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None


class BST:
    def __init__(self):
        self.root = None

    def search_bst(self, tree, key):
        return (tree if not tree or tree.data == key
                else self.search_bst(tree.left, key)
                if key < tree.data else self.search_bst(tree.right, key))


tree = BST()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)


print(tree.search_bst(tree.root, 7).data)
