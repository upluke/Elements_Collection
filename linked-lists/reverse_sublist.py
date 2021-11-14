# 7.2 Reverse a single sublist

# https://www.geeksforgeeks.org/reverse-sublist-linked-list/
# [1, 2, 3]	1	2 =>	[2, 1, 3]
# [1, 2, 3]	1	3 =>	[3, 2, 1]
# [1, 2, 3]	3	3	=> [1, 2, 3]
# [1, 2, 3]	2	3	=> [1, 3, 2]

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def print_head(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next

    def append_node(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # reverses sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next, sublist_head.next, temp)
    return dummy_head.next


ll = LinkedList()
ll.append_node(1)
ll.append_node(2)
ll.append_node(3)
ll.print_node()
print("--------")
new_head = reverse_sublist(ll.head, 1, 3)
ll.print_head(new_head)
