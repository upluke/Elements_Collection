
# 15.6 Generate all subsets of size k

# https://algorithms.tutorialhorizon.com/print-all-combinations-of-subset-of-size-k-from-given-array/


# ele:
# There are two possibilities for a subset-- it doesn't contain 1, or it does contain 1. In the frist case, we return all subsets of size k of [2,3,...,n]; in thesecond case, we compute all k-1 sized subsets of [2,3,...,n] and add 1 to each of them.
# For example, if n =4 andk =2, then we compute all subsets of size 2 from [2,3,4], and all subsets of size 1 from [2,3,4]. We add 1 to each of the latter, and the result is the union of the two sets of subsets, i.e., {{2,3}, {3,4}, {3,4}} U {{1,3}, {1,3}, {1,4}}.
# the time complexity is O(n(^n _k)); the reasoning is analogous to that for the recursive solution enumerating the powerset (Page 233)

def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(partial_combination.copy())
            return
        # generate remaining combinations over {offset, ..., n-1} of size num_remaining
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n-i + 1:
            directed_combinations(i+1, partial_combination + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return result


# [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
print(combinations(5, 2))


# Ol:
# Problem: Generate all subsets of size k
#    Ex. given n = 5 and k =2 generate [1, 2] [1, 3] [1, 4] [1, 5] [2, 3] [2, 4] [2, 5] [3, 4] [3, 5] [4, 5]
#    Solution: This is backtracking problem in which you pass start index + 1 to next iteration of backtrack

def combinations(n, k):

    def helper(n, k, startIndex, res, path):
        if len(path) == k:
            res.append(path)
            return
        for i in range(startIndex, n+1):
            helper(n, k, i+1, res, path+[i])

    res = []
    helper(n, k, 1, res, [])
    return res


# [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
print(combinations(5, 2))
