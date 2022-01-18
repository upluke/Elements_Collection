# 13.7 Merging intervals
# O(1) time per entry, time is O(n)
# https://leetcode.com/problems/insert-interval/

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

import collections

interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    # processes intervals in disjoint_intervals which come before new_interval
    while(i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right):
        i += 1

    # processes intervals in disjoint_intervals which overlap with new_interval
    while(i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left):
        # if [a,b] and [c,d] overlap, union is [min(a,c), max(b,d)]
        new_interval = interval(min(new_interval.left, disjoint_intervals[i].left), max(
            new_interval.right, disjoint_intervals[i].right))
        i += 1

    # processes intervals in disjoint_intervals which come after new_interval
    return result+[new_interval] + disjoint_intervals[i:]

    return disjoint_intervals


print(add_interval([[1, 3], [6, 9]], [2, 5]))
print(add_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


# Lc Solution 1: (7 lines, 88 ms)

# Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) before inserting it between left and right ones.

def insert(intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right


# Solution 2: (8 lines, 84 ms)
# Same algorithm as solution 1, but different implementation with only one pass and explicitly collecting the to-be-merged intervals.

def insert(intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    parts = merge, left, right = [], [], []
    for i in intervals:
        parts[(i.end < s) - (i.start > e)].append(i)
    if merge:
        s = min(s, merge[0].start)
        e = max(e, merge[-1].end)
    return left + [Interval(s, e)] + right


# Solution 3: (11 lines, 80 ms)
# Same again, but collect and merge while going over the intervals once.

def insert(intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right
