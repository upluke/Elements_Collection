# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
# import heapq

# def kLargest(arr, k):
#   heapq.heapify(arr)
#   print(list(arr))
#   print(heapq.nlargest(k,arr))

# print(kLargest([1, 23, 12, 9, 30, 2, 50],3)) # 50 30 23


# ---------------------------------
import heapq
import itertools


def top_k(k, stream):
    # entries are compared by their lengths

    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # push next_string and pop the shortest string in min_heap
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


print(top_k(2, ['abc', 'a', 'abcd', 'ab']))
