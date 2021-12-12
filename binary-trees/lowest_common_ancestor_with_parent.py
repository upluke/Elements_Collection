
# 9.4 Compute the LCA when nodes have parent pointers
# The time and space complexity are that of computing the depth, namely O(h) and O(1), respectively.
# Lowest Common Ancestor of a Binary Tree III - LeetCode
#

# https://towardsdatascience.com/binary-tree-and-lowest-common-ancestor-58eddd433ac

# ele:
from collections import deque


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def add_to_dict(self, node_dict):

        node_dict[self.value] = self


def create_bt(value_queue):
    """create binary tree"""

    if len(value_queue) <= 0:
        return None, None

    node_dict = {}

    root = Node(value_queue.popleft())

    root.add_to_dict(node_dict)

    current_queue = deque()

    current_queue.append(root)

    while len(current_queue) > 0 and len(value_queue) > 0:

        current_node = current_queue.popleft()

        left = value_queue.popleft()
        if left is not None:
            current_node.left = Node(left, parent=current_node)
            current_node.left.add_to_dict(node_dict)
            current_queue.append(current_node.left)

        right = value_queue.popleft()
        if right is not None:
            current_node.right = Node(right, parent=current_node)
            current_node.right.add_to_dict(node_dict)
            current_queue.append(current_node.right)

    return root, node_dict


def create_bt_fls(value_list):
    """create binary create from list"""

    return create_bt(deque(value_list))


def lca(node1, node2):

    parents = set()

    cur_parent = node1
    while cur_parent is not None:
        parents.add(cur_parent)
        cur_parent = cur_parent.parent

    cur_parent = node2
    while cur_parent is not None:
        if cur_parent in parents:
            return cur_parent
        cur_parent = cur_parent.parent

    return None


ls1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 9, 10]
bt1, node_dict = create_bt_fls(ls1)
lca1 = lca(node_dict[9], node_dict[10])
print(lca1.value)

# ele:


def lca2(node0,
         node1):
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    # Makes node0 as the deeper node in order to simplify the code.
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


lca2 = lca2(node_dict[9], node_dict[10])
print(lca2.value)

# ol:
# for more solutions: https://nicksma.medium.com/lowest-common-ancestors-and-variations-493588b699f3


class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def find_lca(n1, n2):
    def get_depth(node):
        depth = 0
        while node and node.parent:
            node = node.parent
            depth += 1
        return depth

    d1 = get_depth(n1)
    d2 = get_depth(n2)

    while d1 > d2:
        n1 = n1.parent
        d1 -= 1

    while d2 > d1:
        n2 = n2.parent
        d2 -= 1

    while n1 != n2 and d1 > 0:
        d1 -= 1
        n1 = n1.parent
        n2 = n2.parent

    return n1.data
