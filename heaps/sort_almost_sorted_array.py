# 10.3 Sort an almost-sorted array
# the time complexity is O(nlogk). THe space complexity is O(k)
# https://www.geeksforgeeks.org/nearly-sorted-algorithm/

from heapq import heappop, heappush, heapify
import itertools
import heapq


# element: doesn't work, needs to be fixed

def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


k = 3
arr = [2, 6, 3, 12, 56, 8]
print(sort_approximately_sorted_array(arr, k), "---")


# gfg:
# We can use Insertion Sort to sort the elements efficiently. Following is the C code for standard Insertion Sort.
# Function to sort an array using insertion sort

# The inner loop will run at most k times. To move every element to its correct place, at most k elements need to be moved. So overall complexity will be O(nk).

def insertionSort(A, size):
    i, key, j = 0, 0, 0
    for i in range(size):
        key = A[i]
        j = i-1

        # Move elements of A[0..i-1], that are
        # greater than key, to one position
        # ahead of their current position.
        # This loop will run at most k times
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


k = 3
arr = [2, 6, 3, 12, 56, 8]
print(insertionSort(arr, k))


# We can sort such arrays more efficiently with the help of Heap data structure. Following is the detailed process that uses Heap.
# 1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time (See this GFact)
# 2) One by one remove min element from heap, put it in result array, and add a new element to heap from remaining elements.
# Removing an element and adding a new element to min heap will take log k time. So overall complexity will be O(k) + O((n-k) * log(k)).
# The Min Heap based method takes O(k) + O((m) * log(k)) time where m = n – k and uses O(k) auxiliary space.


# # Given an array of size n, where every
# # element is k away from its target
# # position, sorts the array in O(nLogk) time.


def sort_k(arr: list, n: int, k: int):
    # List of first k+1 items
    heap = arr[:k + 1]

    # using heapify to convert list into heap(or min heap)
    heapify(heap)

    # "rem_elmnts_index" is index for remaining elements in arr and "target_index" is
    # target index of for current minimum element in Min Heap "heap".
    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        # Pop and return the smallest item from the heap
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1

    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1


arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
k = 3
sort_k(arr, n, k)
