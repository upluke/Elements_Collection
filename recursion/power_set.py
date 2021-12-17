# 15.5 Generate the power set
# The number of recursive calls, C(n) satisfies the recurrence C(n)=2C(n-1), which solves to C(n)=O(2^n). Since we spend O(n) time within a call, the time complexity is O(n2^n). The space complexity is O(n2^n), since there are 2^n subsets, the average subset size is n/2. If we just want to print the subsets, rather than returning all of them, we simply perform a print instead of adding the subset to the result, which reduces the space complexity to O(n) -- the time complexity remians the same.

# https://leetcode.com/problems/subsets/
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

#   def helper(A, path, res):
#     if len(A)==0:
#       res.append(path)

#     for i in range(len(A)):
#       helper(A[:i]+A[i+1:], path+[A[i]], res)

# ele1:
import math


def generate_power_set(input_set):
    # generate all subsets whose intersection with input_set[0]
    # input_set[to_be_selected -1] is exactly selected_so_far
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return
        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain input_set[to_be_selected]
        directed_power_set(to_be_selected+1, selected_so_far +
                           [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set


print(generate_power_set([1, 2, 3]))


# readable ver:
def generate_power_set(nums):

    def helper(i, path):
        if i == len(nums):
            res.append(path)
            return
        helper(i + 1, path)
        helper(i+1, path + [nums[i]])

    res = []
    helper(0, [])
    return res


print(generate_power_set([1, 2, 3]))

# ele2:
# for a given ordering of the elemtns of S, there exists a one-to-one correspondence between the 2^n bit arrays of length n and the set of all  subsets of S--the 1s in the n-length bit array v indicate the elements of S in the subset corresponding to v. For example, if S={a,b,c,d}, the bit array <1,0,1,1> denotes the subset {a,c,d}. This observation can be used to derive a nonrecursive algorithm for enumerating subsets.
# In particular, when n is less than or equal to the width of an integer on the architecture we are working on, we can enumerate bit arrays by enumerating integers in [0, 2^n -1] and examining the indices of bits set in these integers. These indices are determined by first isolating the lowest set bit by computing y=x&~(x-1), which is described on Page 25, and then getting the index by computing log y.


def generate_power_set(input_set):
    power_set = []
    for int_for_subset in range(1 << len(input_set)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(
                input_set[int(math.log2(bit_array & ~(bit_array - 1)))])
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set


print(generate_power_set([1, 2, 3]))


# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).
#lc: recursively


def subsets(nums):
    def dfs(nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], res)
    res = []
    dfs(nums, [], res)
    return res


print(subsets([1, 2, 3]))

# Bit Manipulation


def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1 << len(nums)):
        tmp = []
        for j in range(len(nums)):

            if i & 1 << j:  # if i >> j & 1:
                # print(i, j, 1<<j, i & 1 << j , "in", nums[j])
                tmp.append(nums[j])
        res.append(tmp)
    return res


print(subsets2([1, 2, 3]))

# i          j          1<<j     i&1<<j          nums[j]
# 0          0         1:0010      0
# 0          1         2:0010      0
# 0          2         4:0100      0
# 1:0001     0         1:0001      1               1
# 1:0001     1         2:0010      0
# 1:0001     2         4:0100      0
# 2:0010     0         1:0001      0
# 2:0010     1         2:0010      2               2


# lc:Iteratively
def subsets3(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res


print(subsets3([1, 2, 3]))
