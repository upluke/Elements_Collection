# 10.5 Compute the median of online data
# The time complexity per entry is O(log n), corresponding to insertion and extraction from a heap
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
import heapq


def online_median(sequence):
    # min_heap stores the larger half seen so far
    min_heap = []
    # max_heap stores the smaller half seen so far
    # values in max_heap are negative
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        # ensure min_heap and max_heap have equal number of elements if an even
        # number of elelments is read; otherwise, min_heap must have one more element than max_heap
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0]))
                      if len(min_heap) == len(max_heap) else min_heap[0])

    return result


sequence = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
print(online_median(sequence))
