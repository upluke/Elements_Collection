# 10.6 Compute the k largest elements in a max-heap
# Given a max heap as an array, implement List<Integer> peekTopK(int[] arr, int k) to find the top k elements. Do not modify the heap or copy entire heap to a different data structure. Example:

#            15
#        /        \
#      13         12
#    /   \       /
#  10     8     9
# Input: [15, 13, 12, 10, 8, 9], k = 5
# Output: [15, 13, 12, 10, 9]
import heapq


def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []
    # stores the (-value, index) -pair in candidate_max_heap. This heap is
    # ordered by value field. Uses the negative of value to get the effect of
    # a max heap.
    candidate_max_heap = []
    # the largest element in A is at index 0
    candidate_max_heap.append((-A[0], 0))
    print(candidate_max_heap)
    result = []
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2*candidate_idx+1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap,
                           (-A[left_child_idx], left_child_idx))
        right_child_idx = 2*candidate_idx+2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap,
                           (-A[right_child_idx], right_child_idx))
    return result


print(k_largest_in_binary_heap([15, 13, 12, 10, 8, 9], k=5))
