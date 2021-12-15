# 13.5 Samllest nonconstructible value
# Time Complexity:O(nlogn) for sorting, O(n) for searching.
# Space Complexity:O(1)
# https://lei-d.gitbook.io/leetcode/math/smallest-non-constructible-value


# Input: A = [1, 2, 4]
# Output: 8
# Explanation: With subsets of A, we can construct values 1, 2, 3, 4, 5, 6, 7.

# Input: A = [1, 2, 5]
# Output: 4
# Explanation: With subsets of A, we can construct values 1, 2, 3, 5, 6, 7, 8.

# ele:
def smallest_nonconstructible_value(A):

    max_constructible = 0
    for a in sorted(A):
        if a > max_constructible+1:
            break
        max_constructible += a
    return max_constructible+1


# smallest_nonconstructible_value([1, 1, 1, 1, 1, 5, 10, 25]) # 21
print(smallest_nonconstructible_value([1, 2, 5]))
