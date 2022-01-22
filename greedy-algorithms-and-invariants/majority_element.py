# 17.5 Find the majority element
# Since we spend O(1) time per entry, the time complexity is O(n). The additional space complexity is O(1).
# https://leetcode.com/problems/majority-element/

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# ele:
def majority_search(stream):
    candidate_count = 0
    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count+1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate


print(majority_search([3, 2, 3]))


# lc:
def majorityElement1(nums):
    nums.sort()
    return nums[len(nums)//2]
    # return sorted(num)[len(num)/2]


def majorityElement2(nums):
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums)//2:
            return n

# init: (with hint from ele) O(1) space
# We have a candidate for the majority element, and track its count. It is initialized to the first entry. We iterate through remaining entries. Each time we see an entry equal to the candidate, we increment the count. If the entry is different, we decrement the count. If the count becomes zero, we set the next entry to tbe the candidate.


def majorityElement(nums):
    count = 1
    temp = nums[0]

    for i in range(1, len(nums)):
        if count == 0:
            temp = nums[i]
            count = 0
        if temp == nums[i]:
            count += 1
        else:
            count -= 1

    return temp


print(majorityElement([3, 2, 3]))
