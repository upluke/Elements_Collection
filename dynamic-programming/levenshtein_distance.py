# 16.2 Compute the levenshtein distance
# The value E(A[0, a-1], B[0, b-1]) takes time O(1) to compute once E(A[0,k], B[0,l]) is known for all k<a and l<b. This implies O(ab) time complexity for the algorithm. Our implementation uses O(ab) space
import functools


def levenshtein_distance(A, B):
    @functools.lru_cache(None)
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            # A is empty so add all of B's characters
            return B_idx+1
        elif B_idx < 0:
            # B is empty so delete all of A's characters
            return A_idx+1

        if A[A_idx] == B[B_idx]:
            return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

        substitute_last = compute_distance_between_prefixes(
            A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx-1, B_idx)
        delete_last = compute_distance_between_prefixes(A_idx-1, B_idx)
        return 1 + min(substitute_last, add_last, delete_last)

    return compute_distance_between_prefixes(len(A)-1, len(B)-1)


print(levenshtein_distance("horse", "ros"))


# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# lc 1:
def minDistance(word1, word2):
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)

    if word1[0] == word2[0]:
        return minDistance(word1[1:], word2[1:])

    insert = 1+minDistance(word1, word2[1:])
    delete = 1+minDistance(word1[1:], word2)
    replace = 1+minDistance(word1[1:], word2[1:]
                            )
    return min(insert, delete, replace)


print(minDistance("horse", "ros"))


# lc 2: (caching)

def minDistance(word1, word2, i, j, memo):
    """Memoized solution"""
    if i == len(word1) and j == len(word2):
        return 0
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i

    if (i, j) not in memo:
        if word1[i] == word2[j]:
            ans = minDistance(word1, word2, i + 1, j + 1, memo)
        else:
            insert = 1 + minDistance(word1, word2, i, j + 1, memo)
            delete = 1 + minDistance(word1, word2, i + 1, j, memo)
            replace = 1 + minDistance(word1, word2, i + 1, j + 1, memo)
            ans = min(insert, delete, replace)
        memo[(i, j)] = ans
    return memo[(i, j)]

# lc3: (dynamic)


def minDistance(word1, word2):
    """Dynamic programming solution"""
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j],
                                      table[i][j - 1], table[i - 1][j - 1])
    return table[-1][-1]


# liz:
def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1,
               LD(s[:-1], t[:-1]) + cost])
    return res


# print(LD("home", "haome"))
print(LD("Python", "JavaScript"))
