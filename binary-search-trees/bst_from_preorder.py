# 14.5 Reconstruct a BST from traversal data

# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/


class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# ele 2:
# the worst-case time complexity is O(n), since it performs a constant amount of work per node. Note the similarity to solution 24.19 on page 390

def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] + 1
        # Note that rebuild_bst_from_preorder_on_value_range updates root_idx[0]
        # So the order of following two calls are critical
        left_subtree = rebuild_bst_from_preorder_on_value_range(
            lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(
            root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0]  # tracks current subtree
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))


# ele 1:
# the worst_case input for this algorithm is the pre-order sequence corresponding to a left-skewed tree. The worst-case time complexity satisfies the recurrence W(n)= W(n-1) +O(n), which solves to O(n2). The best-case input is a sequence corresponding to a right-skewed tree, and the correspoinding time complexity is O(n). When the sequence corresponds to a balanced BST, the time complexity is given by B(n) =2B(n/2) +O(n), which solves to O(nlogn).

def rebuild_bst_from_preorder(preorder_sequence):

    if not preorder_sequence:
        return None

    transition_point = next(
        (i
         for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]),
        len(preorder_sequence))
    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:]))


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# gfg:
# Time Complexity: O(n)
# We will soon publish a O(n) iterative solution as a separate post.
# Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.


INT_MIN = float("-infinity")
INT_MAX = float("infinity")


# Methods to get and set the value of static variable
# constructTreeUtil.preIndex for function construcTreeUtil()


def getPreIndex():
    return constructTreeUtil.preIndex


def incrementPreIndex():
    constructTreeUtil.preIndex += 1

# A recursive function to construct BST from pre[].
# preIndex is used to keep track of index in pre[]


def constructTreeUtil(pre, key, mini, maxi, size):

    # Base Case
    if(getPreIndex() >= size):
        return None

    root = None

    # If current element of pre[] is in range, then
    # only it is part of current subtree
    if(key > mini and key < maxi):

        # Allocate memory for root of this subtree
        # and increment constructTreeUtil.preIndex
        root = Node(key)
        incrementPreIndex()

        if(getPreIndex() < size):

            # Construct the subtree under root
            # All nodes which are in range {min.. key} will
            # go in left subtree, and first such node will
            # be root of left subtree
            root.left = constructTreeUtil(pre,
                                          pre[getPreIndex()],
                                          mini, key, size)
        if(getPreIndex() < size):

            # All nodes which are in range{key..max} will
            # go to right subtree, and first such node will
            # be root of right subtree
            root.right = constructTreeUtil(pre,
                                           pre[getPreIndex()],
                                           key, maxi, size)

    return root

# This is the main function to construct BST from given
# preorder traversal. This function mainly uses
# constructTreeUtil()


def constructTree(pre):
    constructTreeUtil.preIndex = 0
    size = len(pre)
    return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)


# A utility function to print inorder traversal of Binary Tree
def printInorder(node):

    if node is None:
        return
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)


# Driver code
pre = [10, 5, 1, 7, 40, 50]

# Function call
root = constructTree(pre)

print("Inorder traversal of the constructed tree: ")
printInorder(root)


# init:
def rebuild_bst_from_preorder3(preorder_sequence):

    root = Node(preorder_sequence[0])

    divider_idx = -1
    for i, num in enumerate(preorder_sequence):
        if num > root.data:
            divider_idx = i
            break
    lhs = preorder_sequence[1:divider_idx]
    rhs = preorder_sequence[divider_idx:]

    root.left = Node(lhs[0])
    for i in range(1, len(lhs)):
        build_bst(root.left, lhs[i])

    root.right = Node(rhs[0])
    for i in range(1, len(rhs)):
        build_bst(root.right, rhs[i])

    print_nodes(root)
    return root


def build_bst(root, node_data):
    if root.data > node_data:
        root.left = Node(node_data)
    else:
        root.right = Node(node_data)


def print_nodes(root):
    if root.left:
        print_nodes(root.left)
    print(root.data)
    if root.right:
        print_nodes(root.right)


pre = [10, 5, 1, 7, 40, 50]
print(rebuild_bst_from_preorder3(pre))  # 1 5 7 10 40 50
