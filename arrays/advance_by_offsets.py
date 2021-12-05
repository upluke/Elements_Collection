# 5.4 Advancing through an array
# the time complexity is O(n), and the additonal space complexity (beyond what is used for A) is three integer variables, i.e., O(1)
# https://leetcode.com/problems/jump-game/

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# element:
def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A)-1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i]+i)
        i += 1
    return furthest_reach_so_far >= last_index


print(can_reach_end([3, 2, 1, 0, 4]))
# print(can_reach_end([1,1,1,0]))
# print(can_reach_end([1,0,1,0]))


# lc:
# 1-6 lines, O(n) time, O(1) space

# Solution 1
def canJump(nums):
    temp = 0
    for i, n in enumerate(nums):
        if i > temp:
            return False
        temp = max(temp, i+n)
    return True


print(canJump([3, 2, 1, 0, 4]))
# Solution 2

# One-liner version:
# def canJump(nums):
#     return reduce(lambda temp, (i, n): max(temp, i+n) * (i <= temp), enumerate(nums, 1), 1) > 0
# print(canJump([3,2,1,0,4]))
