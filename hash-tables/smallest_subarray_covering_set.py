# 12.6 Find the smallest subarray covering all values
# Minimum Window Substring (LeetCode)
#  https://www.youtube.com/watch?v=U1q16AFcjKs
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.


# Follow up: Could you find an algorithm that runs in O(m + n) time?

# LC
# The time complexity of our solution is going to be big o of 2 times n plus m [O(2*N+M)] , so n is the length of string s and m is the length of string t. We must iterate over string t in order to create the map of counts in the worst case our I and j pointer could potentially touch every single character in s, so this could technically be written as n plus n plus m [O(N+N+M)], but since we drop constants it just becomes big O of n plus m [O(N+M)] . Our space complexity is going to be big O of n where n is the length of string t the only memory we initialize is the map and this will be the size of string t.
# import collections

# def minWindow(s, t):
#     hp, count = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         count -= hp[c] > 0
#         hp[c] -= 1
#         if not count:
#             while i < j and hp[s[i]] < 0:
#                 hp[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]


# print(minWindow("ADOBECODEBANC", "ABC"))


# Element:
# the complexity is O(n), where n is the length of the array, since for each of the two indices we spend O(1) time per advance, and each is advanced at most n-1 times.
import collections
Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1
        # keeeps advancing left until keywords_to_cover does not contain all keywords
        while remaining_to_cover == 0:
            if result == Subarray(start=-1, end=-1) or right-left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


print(find_smallest_subarray_covering_set(
    ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"], ["b", "c", "e"]	))

# array(string)	set(string)	int
# ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]	["b", "c", "e"]	6	TODO
# ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]	["a", "c"]	2	TODO
