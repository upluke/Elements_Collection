# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# time:O(n)
# space:O(1)

def maxSubArray(nums):
    max_seen = max_end = 0
    for n in nums:
        max_end = max(n, n + max_end)
        max_seen = max(max_seen, max_end)

    return max_seen


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
