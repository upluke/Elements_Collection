
# 10.2 Sort an increasing-decreasing array
# generalizing, we could first reverse the order of each of the decreasing subarrays. We could decompose A into four sorted arrays -<57,131,493>,<221, 294>,<339,418,452>, and <190,442>. Now we can use the techniques in solution 10.1 on page 137 to merge these.
# Just as in Solution 10.1 on page 137, the time complexity is O(n log k) time.

# https://www.geeksforgeeks.org/sort-an-increasing-decreasing-array/
import itertools
import heapq


def sort_k_increasing_decreasing_array(A):

    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or  # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == decreasing) or
                (A[i - 1] >= A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (decreasing
                             if subarray_type == increasing else increasing)
    return merge_sorted_arrays(sorted_subarrays)


def merge_sorted_arrays(sorted_arrays):

    min_heap = []
    # Builds a list of iterators for each array in sorted_arrays.
    # The iter() function creates an object which can be iterated one element at a time.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap.
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


print(sort_k_increasing_decreasing_array(
    [57, 131, 493, 294, 221, 339, 418, 458, 442, 190]))

# Pythonic solution, uses a stateful object to trace the monotonic subarrays.


def sort_k_increasing_decreasing_array_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])


# init:


def sort_k_increasing_decreasing_array(list):
    res = []
    heapq.heapify(list)
    while len(list):
        # heappop pops from smallest to largest
        res.append(heapq.heappop(list))

    return res


print(sort_k_increasing_decreasing_array(
    [57, 131, 493, 294, 221, 339, 418, 458, 442, 190]))
