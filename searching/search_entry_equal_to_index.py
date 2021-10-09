
# 11.2 search a sorted array for entry equal to its index
# the time complexity is the same as that for binary search, i.e., O(logn), where n is the length of A

# https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/


#   Input: arr[] = {-10, -5, 0, 3, 7}
#   Output: 3  // arr[3] == 3

#   Input: arr[] = {0, 2, 5, 8, 17}
#   Output: 0  // arr[0] == 0


#   Input: arr[] = {-10, -5, 3, 4, 7, 9}
#   Output: -1  // No Fixed Point


def search_entry_equal_to_its_index(A):
    left, right = 0, len(A)-1
    while left <= right:
        mid = (left+right)//2
        difference = A[mid]-mid
        # A[mid]==mid if and only if difference ==0
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid+1
    return -1


print(search_entry_equal_to_its_index([-10, -5, 0, 3, 7]))  # 3


# gfg
def linearSearch(arr, n):
    for i in range(n):
        if arr[i] is i:
            return i
    # If no fixed point present then return -1
    return -1


# Driver program to check above functions
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr, n)))

# #init:
# def search_entry_equal_to_its_index(A):
#   for i, num in enumerate(A):
#     if i==num:
#       return i
#   return -1

# print(search_entry_equal_to_its_index([-10, -5, 0, 3, 7]))


# Variant: solve the same problem when A is sorted but may contain duplicates
# https://www.geeksforgeeks.org/find-fixed-point-value-equal-index-given-array-duplicates-allowed/

# Input: arr[] = {-10, -5, 0, 3, 7}
# Output: 3  // arr[3] == 3

# Input: arr[] = {-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13}
# Output: 2  // arr[2] == 2

# Input: arr[] = {-10, -5, 3, 4, 7, 9}
# Output: -1  // No Fixed Point

def search_entry_equal_to_its_index_with_duplicates(A):
    pass

# ---------------------

# bonus:
# https://leetcode.com/problems/find-pivot-index/

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0


def pivotIndex(nums):
    # Time: O(n)
    # Space: O(1)
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
