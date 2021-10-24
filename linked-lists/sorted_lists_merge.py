# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def append_node(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

# sorted_lists_merge


def merge_two_sorted_lists(L1, L2):
    # creates a placeholder for the result
    dummy_head = tail = ListNode(0)

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


l1 = LinkedList()
l1.append_node(1)
l1.append_node(3)
l1.append_node(5)
# ls1.print_node()

l2 = LinkedList()
l2.append_node(2)
l2.append_node(4)
l2.append_node(6)
# ls2.print_node()


l1.head = merge_two_sorted_lists(l1.head, l2.head)
l1.print_node()
