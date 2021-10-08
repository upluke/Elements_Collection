
# 10.1 merge sorted files
# let ke be the number of input sequences.
# Then there are no more than k elements in the min-heap.
# Both extract-min and insert take O(logk)time Hence,
#  we can do the merge in O(nlogk) time.
# The space complexity is O(k) beyond the space needed to write the final result.
import heapq


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


print(merge_sorted_arrays([[3, 5, 7], [0, 6], [0, 6, 28]]))
# [0,0,3,5,6,6,7,2,8]


# pythonic solution, uses the heapq.erge()method which takes multiple inputs
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


print(merge_sorted_arrays_pythonic([[3, 5, 7], [0, 6], [0, 6, 28]]))
# [0,0,3,5,6,6,7,2,8]


# # int:
# def merge_sorted_arrays(sorted_arrays):
#   res, temp=[], []
#   temp=[s for sa in sorted_arrays for s in sa]

#   heapq.heapify(temp)

#   while len(temp):
#     res.append(heapq.heappop(temp))

#   return res

# print(merge_sorted_arrays([[3,5,7],[0,6],[0,6,28]]))
# # [0,0,3,5,6,6,7,2,8]
