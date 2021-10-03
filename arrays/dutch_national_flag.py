# 5.1

# # method 3.0
# time: O(n)
# space:O(1)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal: larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    # keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal]>pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A


# the pivot has to be greater or equal half of size
print(dutch_flag_partition(3, [2, 0, 2, 1, 1, 0]))

# # # method 2.0
# # time: O(n)
# # space:O(1)
# def dutch_flag_partition(pivot_index, A):
#   pivot=A[pivot_index]
#   # first pass: group elements smaller than pivot
#   smaller=0
#   for i in range(len(A)):
#     if A[i]<pivot:
#         A[i],A[smaller]=A[smaller], A[i]
#         smaller+=1

#   # second pass: group elements larger than pivot
#   larger=len(A)-1
#   for i in reversed(range(len(A))):
#     if A[i]>pivot:
#         A[i],A[larger]=A[larger], A[i]
#         larger-=1
#   return A

# # the pivot has to be greater or equal half of size
# print(dutch_flag_partition(3, [2,0,2,1,1,0]))


# # method 1.0
# # time: O(n^2)
# # space:O(1)
# def dutch_flag_partition(pivot_index, A):
#   pivot=A[pivot_index]
#   # first pass: group elements smaller than pivot
#   for i in range(len(A)):
#     # look for a samller element
#     for j in range(i+1, len(A)):
#       if A[j]<pivot:
#         A[i],A[j]=A[j], A[i]
#         break
#   print(A)
#   # second pass: group elements larger than pivot
#   for i in reversed(range(len(A))):
#     # look for a larger element. Stop when we reach an element less than
#     # pivot, since first pass has moved them to the start of A
#     for j in reversed(range(i)):
#       if A[j]>pivot:
#         A[i],A[j]=A[j], A[i]
#         break
#   return A

# # the pivot has to be greater or equal half of size
# print(dutch_flag_partition(3, [2,0,2,1,1,0]))


# Sort Colors
# Dutch National Flag too
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Example 3:
# Input: nums = [0]
# Output: [0]

# Example 4:
# Input: nums = [1]
# Output: [1]

def sortColors(nums):
    low, mid, hi = 0, 0, len(nums)-1

    while mid <= hi:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            nums[hi], nums[mid] = nums[mid], nums[hi]
            hi -= 1

    return nums


print(sortColors([2, 0, 1]))


# this question is used to sort three parts of a list with 3 variables, refer to even_odd_array.py to see
# sorting two parts of a list with 2 variables
