# 16.6 The knapsack problem
# the algorithm computes V[n-1][w] in O(nw)time, and uses O(nw) space.
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
import collections
import functools
from typing import List
Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:

    # Returns the optimum value when we choose from items[:k + 1] and have a
    # capacity of available_capacity.
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            # No items can be chosen.
            return 0

        without_curr_item = optimum_subject_to_item_and_capacity(
            k - 1, available_capacity)
        with_curr_item = (0 if available_capacity < items[k].weight else
                          (items[k].value +
                           optimum_subject_to_item_and_capacity(
                               k - 1, available_capacity - items[k].weight)))
        return max(without_curr_item, with_curr_item)

    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


print(optimum_subject_to_capacity(
    [[23, 49], [34, 84], [13, 15], [3, 44], [87, 27], [18, 40]], 134))

# array(tuple(int[weight], int[value]))	int[capacity]	int[result]
# [[23, 49], [34, 84], [13, 15], [3, 44], [87, 27], [18, 40]]	117	232	TODO
# [[64, 60], [88, 88], [19, 20]]	134	108	TODO


# dp:https://www.educative.io/blog/python-dynamic-programming-tutorial
def solveKnapsack(weights, prices, capacity, index, memo):
    # base case of when we have run out of capacity or objects
    if capacity <= 0 or index >= len(weights):
        return 0
    # check for solution in memo table
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    # if weight at index-th position is greater than capacity, skip this object
    if weights[index] > capacity:
        # store result in memo table
        memo[(capacity, index)] = solveKnapsack(
            weights, prices, capacity, index + 1, memo)
        return memo[(capacity, index)]
    # recursive call, either we can include the index-th object or we cannot, we check both possibilities and return the most optimal one using max
    memo[(capacity, index)] = max(prices[index]+solveKnapsack(weights, prices, capacity - weights[index], index+1, memo),
                                  solveKnapsack(weights, prices, capacity, index + 1, memo))
    return memo[(capacity, index)]


def knapsack(weights, prices, capacity):
    # create a memo dictionary
    memo = {}
    return solveKnapsack(weights, prices, capacity, 0, memo)


print(knapsack([2, 1, 1, 3], [2, 8, 1, 10], 4))


# You're trying to solve the Knapsack Problem- a common problem in computer science (and in many RPG video games!).
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# The problem has been solved- but recursively! Now we can't find values for Bags of Holding, which can hold unusually large amounts of weight. Adapt this solution to cache results and solve iteratively.

# val = [60, 100, 120]

# wt = [10, 20, 30]

# W = 50

# n = len(val)

# print knapSack(W , wt , val , n)

# liz:(init recursive)
# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
