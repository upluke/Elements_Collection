
# 8.6 Compute binary tree nodes in order of incresing depth
# Since each node is enqueued and dequeued exactly once, the time complexity is O(n). The s

# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binary_tree_depth_order(root):
    result = []
    if not root:
        return result

    curr_depth_nodes = [root]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]
    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(binary_tree_depth_order(root))


# gfg:
# https://www.geeksforgeeks.org/level-order-tree-traversal/
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getHeight(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = getHeight(node.left)
        rheight = getHeight(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# Print nodes at a current level


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


def binary_tree_depth_order2(root):
    h = getHeight(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

binary_tree_depth_order2(root)
