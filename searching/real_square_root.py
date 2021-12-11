# 11.5 compute the real square root
# the time complexity is O(log x/s), where s is the tolerance.
# Implement a function which takes as input a floating point value and returns its square root.
# https://leetcode.com/problems/sqrtx/

# ele:
import math


def square_root(x):
    # decides the search range according to x's value relative to 1.0
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    print(left, right)
    # keeps searching as long as left != right
    while not math.isclose(left, right):
        mid = 0.5 * (left+right)
        mid_squared = mid*mid
        if mid_squared > x:
            right = mid
        else:
            left = mid

    return left


print(square_root(4.5))
