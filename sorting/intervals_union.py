# 13.8 Compute the union of intervals
# https://leetcode.com/problems/interval-list-intersections/
# solution: https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams
# Example 1:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Example 2:
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []

# [0,2],[5,10],[13,23],[24,25]]
# [1,5],[8,12],[15,24],[25,26]]
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

import collections


def intervalIntersection(A, B):
    i = 0
    j = 0

    result = []
    while i < len(A) and j < len(B):
        a_start, a_end = A[i]
        b_start, b_end = B[j]
        if a_start <= b_end and b_start <= a_end:                       # Criss-cross lock
            # Squeezing
            result.append([max(a_start, b_start), min(a_end, b_end)])

        if a_end <= b_end:         # Exhausted this range in A
            i += 1               # Point to next range in A
        else:                      # Exhausted this range in B
            j += 1               # Point to next range in B
    return result


print(intervalIntersection([[0, 2], [5, 10], [13, 23], [
      24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
print(intervalIntersection([[1, 3], [5, 9]], []))
print(intervalIntersection([[1, 7]], [[3, 10]]))
print(intervalIntersection([[5, 10]], [[3, 10]]))
print(intervalIntersection([[5, 10]], [[5, 10]]))

print(intervalIntersection([[5, 10]], [[5, 6]]))
print(intervalIntersection([[14, 16]], [[7, 13], [16, 20]]))


# element
# O(nlogn)

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):

    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or
                          (i.left.val == result[-1].right.val and
                           (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or
                    (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result
