# 7.3 Test for cyclicity
# Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create a cycle in a linked list by making the next filed of an element reference to one of the earlier nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

# ele:
# let F be the number of nodes to the start of the cycle, C the number of nodes on the cycle, and n the total number of nodes. Then the time complexity is O(F)+O(C)=O(n)-O(E) for both pointers to reach the cycle, and O(C) for them to overlap once the slower one enters the cycle.


def has_cycle(self, head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # finds the start of the cycle
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it  # iter is the start of cycle
    return None  # no cycle


ll = LinkedList()
ll.append_node(2)
ll.append_node(4)
ll.append_node(8)

# liz:
# implement this method
# return true if there is a cycle in this linked list
# do not modify this class


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# do not modify this class, or any of the methods in it, other than has_cycle()
# you may insert new methods if you like


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node

    def extend(self, array):
        for element in array:
            self.append(element)


def has_cycle(self):
    visited = {}
    curr = self.head
    while curr != None and not visited.get(curr):
        visited[curr] = True
        curr = curr.next
    return curr != None

# Variant: the following progarm purports to compute the beginning of the cycle wihout determining the length of the cycle; it has the benmefit of being more succinct than the code listed above. Is the program corret?


def has_cycle(self, head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:  # there is a cycle
            # tries to find the start of the cycle
            slow = head
            # both pointers advance at the same time
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow  # slow is the start of cycle
    return None  # no cycle
