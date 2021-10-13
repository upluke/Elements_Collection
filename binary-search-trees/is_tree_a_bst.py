import collections


class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None


class BST:
    def __init__(self):
        self.root = None

    #  14.2 Test if a binary tree satisfies the BST property
    # time: O(n), and the addtional space complexity is O(h), where h is the height of the tree

    def is_binary_tree_bst(self, tree):
        def are_keys_in_range(tree,
                              low_range=float('-inf'),
                              high_range=float('inf')):
            if not tree:
                return True
            elif not low_range <= tree.data <= high_range:
                return False
            return (are_keys_in_range(tree.left, low_range, tree.data)
                    and are_keys_in_range(tree.right, tree.data, high_range))

        return are_keys_in_range(tree)

    # similar online:
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))

    def check_bst(self, node, minimum, maximum):
        if not node:
            return True

        if not minimum < node.data < maximum:
            return False

        return (self.check_bst(node.left, minimum, node.data)
                and self.check_bst(node.right, node.data, maximum))

    # alternative solution:
    # we can use the fact that an inorder traversal visits keys in sorted order. Furthermore, if an inorder traversal of a binary tree visits keys in sorted order, then that binary tree must be a BST.(This follows directly from the definition of a BST and the definition of an inorder walk.) Thus we can check the BST property by performing an inorder traversal, recording the key stored at the last visited node. Each time a new node is visited, its key is compared with the key of the previously visited node. If at any step in the walk, the key at the previously visited node is greater than the node currently being visited, we have a violation of the BST property. All these approaches explore the left subtree frist. THerefore, even if the BST property doest not hold at a node which is close to the root(eg., the key stored at the right child is less than the key stored at the root), their time complexity is still O(n)
    def is_binary_tree_bst_alternative(self, tree):
        def inorder_traversal(tree):
            if not tree:
                return True
            elif not inorder_traversal(tree.left):
                return False
            elif prev[0] and prev[0].data > tree.data:
                return False
            prev[0] = tree
            return inorder_traversal(tree.right)

        prev = [None]
        return inorder_traversal(tree)

    # queue solution:
    # specifically, we use a queue, where each queue entry contains a node, as well as an upper and a lower bound on the keys stored at the subtree rooted at that node. The queue is initialized to the root, with lower bound -∞ and upper bound ∞. We iteratively check the constaraint on each node. If it violates the constraint we stop - the BST property has been violated. Otherwise, we add its children along with the corresponding constraint.
    # time is O(n), and addtional space complexity is O(n)

    def is_binary_tree_bst_queue(self, tree):
        QueueEntry = collections.namedtuple(
            'QueueEntry', ('node', 'lower', 'upper'))
        bfs_queue = collections.deque(
            [QueueEntry(tree, float('-inf'), float('inf'))])

        while bfs_queue:
            front = bfs_queue.popleft()
            if front.node:
                if not front.lower <= front.node.data <= front.upper:
                    return False
                bfs_queue.extend(
                    (QueueEntry(front.node.left, front.lower, front.node.data),
                     QueueEntry(front.node.right, front.node.data, front.upper)
                     )
                )
        return True


tree = BST()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)


print(tree.isValidBST(tree.root))
print(tree.is_binary_tree_bst(tree.root))
print(tree.is_binary_tree_bst_alternative(tree.root))
print(tree.is_binary_tree_bst_queue(tree.root))
