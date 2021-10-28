# 11.3 search a cyclically sorted array
# the time complexity is the same as that of binary search, namely O(logn)

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def search_smallest(A):
    left, right = 0, len(A)-1
    while left < right:

        mid = (left+right)//2

        if A[mid] > A[right]:
            # minimum must be in A[mid +1: right +1]
            left = mid+1
        else:  # A[mid] <A[right]
            # minimum can't be in A[mid +1: right +1] so it must be
            # in A[left: mid+1]
            right = mid
    # loop ends when left ==right
    return left


print(search_smallest([3, 4, 5, 1, 2]))  # 3
print(search_smallest([378, 478, 550, 631, 103, 203, 220, 234, 279, 368]))  # 4
