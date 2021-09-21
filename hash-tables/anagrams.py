# https://leetcode.com/problems/group-anagrams/

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


# def groupAnagramWords(strs):
#     d = {}
#     for w in sorted(strs):
#         key = tuple(sorted(w))
#         d[key] = d.get(key, []) + [w]
#     return d.values()


# print(groupAnagramWords(['abc','bcd','cba','cbd','efg']))
# ['abc', 'cba'], ['bcd', 'cbd'],['efg']

from collections import defaultdict

# when only return anagrams:
# the computation  consists of n callss to sort and n insertions into the hash table. Sorting all the keys has time complexity o(nm log m). The insertions add a time complexity of O(nm), yielding O(nm log m) time complexity in total.


def groupAnagrams(dictionary):
    sorted_string_to_anagrams = defaultdict(list)

    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


# [['eat', 'tea', 'ate'], ['tan', 'nat']]
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
