# 17.3 The interval covering problem
# since we spend O(1) time per index, the time complexity after the initial sort is O(n), where n is the number of intervals. Therefore, the time taken is dominated by the initial sort, i.e., O(nlogn)
# similar concept: Problem: In an old car tunnel there are some lamps located unevenly throughout the tunnel. Each lamp has a different lighting range. The task is to light up the whole tunnel while using as few lamps as possible.
import collections
import operator


Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):

    # Sort intervals based on the right endpoints.
    print("before", intervals)
    intervals.sort(key=operator.attrgetter('right'))
    print("after", intervals)
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            # The current right endpoint, last_visit_time, will not cover any
            # more intervals.
            last_visit_time = interval.right
            num_visits += 1
    return num_visits


print(find_minimum_visits([Interval(0, 3), Interval(
    2, 6), Interval(3, 4), Interval(6, 9)]))  # 3,6
# print(find_minimum_visits([Interval(1,2),Interval(2,3),Interval(3,4),Interval(2,3),Interval(3,4),Interval(4,5)])) # 2,4

# array(tuple(int, int))	int
# [[1, 4], [2, 8], [3, 6], [3, 5], [7, 10], [9, 11]]	2	TODO
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]	3	TODO
# [[1, 5], [2, 3], [3, 4]]	1	TODO
# [[0, 10], [0, 14]]	1	TODO
