# 7.5 Test for overlapping lists -- List may have cycles
# the algorithm has time complexity O(n), where n is the total number of nodes in the two input lists, and space complexity O(1)


# ele:

def overlapping_lists(l0, l1):

    # Store the start of cycle if any.
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root0 and not root1:
        # Both lists don't have cycles.
        return overlapping_no_cycle_lists(l0, l1)
    elif (root0 and not root1) or (not root0 and root1):
        # One list has cycle, one list has no cycle.
        return None
    # Both lists have cycles.
    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break

    return root1 if temp is root0 else None


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


def overlapping_no_cycle_lists(l0, l1):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l0_len, l1_len = length(l0), length(l1)
    if l0_len > l1_len:
        l0, l1 = l1, l0  # l1 is the longer list
    # advances the longer list to get equal length lists
    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0  # None implies there is no overlap between l0 and l1
