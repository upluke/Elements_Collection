# 9.6 Find a root to leaf path with specified sum
# https://leetcode.com/problems/path-sum/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def hasPathSum(root, target):
    if not root:
        return False
    if not root.left and not root.right:  # leaf
        return target == root.val
    # Non-leaf
    return hasPathSum(root.left, target-root.val) or hasPathSum(root.right, target-root.val)

# lc:
# def hasPathSum(root,target):
#     if not root:
#       return False
#     if not root.left and not root.right and root.val==target:
#       return True
#     target -=root.val
#     return hasPathSum(root.left, target) or hasPathSum(root.right,target)


node = Node(5)
node.left = Node(3)
node.right = Node(7)

print(hasPathSum(node, 8))
