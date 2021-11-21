# 11.4 compute the integer squrare root
# the time complexity is that of binary serach over the interval [0,k], i.e.,O(logk)
# https://www.geeksforgeeks.org/square-root-of-an-integer/

# Input: x = 4
# Output: 2
# Explanation:  The square root of 4 is 2.

# Input: x = 11
# Output: 3
# Explanation:  The square root of 11 lies in between
# 3 and 4 so floor of the square root is 3.

def square_root(k):
    left, right = 0, k
    # candidate interval [left, right] where everything before left has square <=k, everything after right
    # has square >k
    while left <= right:
        mid = (left+right)//2
        mid_squared = mid*mid
        if mid_squared <= k:
            left = mid+1
        else:
            right = mid-1
        return left - 1


print(square_root(4))

# gfg 2
# The idea is to use Binary Search to solve the problem. The values of i * i is monotonically increasing, so the problem can be solved using binary search.
# Time complexity: O(log n).
# The time complexity of binary search is O(log n).
# Space Complexity: O(1).
# Constant extra space is needed.


def floorSqrt(x):
    if (x == 0 or x == 1):
        return x
    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x
    while (start <= end):
        mid = (start + end) // 2
        # If x is a perfect square
        if (mid*mid == x):
            return mid
        # Since we need floor, we update
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid < x):
            start = mid + 1
            ans = mid

        else:
            # If mid*mid is greater than x
            end = mid-1

    return ans


x = 11
print(floorSqrt(x))

# gfg1:  Babylonian Method
# To find the floor of the square root, try with all-natural numbers starting from 1. Continue incrementing the number until the square of that number is greater than the given number.
# Time Complexity: O(√ n).
# Only one traversal of the solution is needed, so the time complexity is O(√ n).
# Space Complexity: O(1).
# Constant extra space is needed.


def floorSqrt(x):

    # Base cases
    if (x == 0 or x == 1):
        return x

    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i

    return i - 1


x = 11
print(floorSqrt(x))
