class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    if root:
        # preoder: Processes the root before the traversals of left and right children
        print('Preorder-----: %d' % root.data)
        tree_traversal(root.left)
        # inorder: processes the root after the traversal of left child and before the traversal of right child
        print('inorder>>>>>: %d' % root.data)
        tree_traversal(root.right)
        # Postorder: processes the root after the traversals of left and right chidlren
        print('Postorder@@@@@: %d' % root.data)


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

tree_traversal(root)
