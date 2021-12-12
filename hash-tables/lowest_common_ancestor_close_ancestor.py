# 12.4 Compute the LCA, optimizing for close ancestors
# Note that we're trading space for time. The algorithm for solution 9.4 on page 120 used 120 used O(1) space and O(h) time, whereas the algorithm presented above uses O(D0+D1) space and time, where D0 is the distance from the LCA to the first node, and D1 is the distance from the LCA to the second node. In the worst-case, the nodes are leaves whose LCA is the root, and we end up using O(h) space and time, where h is the height of tree.

# https://towardsdatascience.com/binary-tree-and-lowest-common-ancestor-58eddd433ac
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
'''
output:
6
'''

# ele:


def lca2(node0, node1):
    iter0, iter1 = node0, node1
    nodes_on_path_to_root = set()

    while iter0 or iter1:
        # ascend tree in tandem for these two nodes
        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent
    raise ValueError('node0 and node1 are not in the same tree')


lca1 = lca2(node_dict[9], node_dict[10])
print(lca1.value)
