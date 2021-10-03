

# time:O(n)
# space:O(1)

from numpy import random


def even_odd(A):

    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


nums = random.randint(10, size=(8))

print("---", nums)

print(even_odd(nums))


# def even_odd(A):
#   # two pointers
#     l,r=0,len(A)-1
#   # iterate over the array
#     while l<=r:
#   # w/ 2pts, decide which element is even/odd
#       if A[r]%2==0 and A[l]%2==1:
#         A[l],A[r]=A[r],A[l]
#         l+=1
#         r-=1
#       elif A[l]%2==0:
#         l+=1
#       elif A[r]%2==1:
#         r-=1

#     return A


#   # switch odd and even

# from numpy import random
# nums=random.randint(10, size=(8))

# print(nums)

# print(even_odd(nums))

# 437 Move all negative elements to end (similar problem )
# Input :
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output :
# 1  3  2  11  6  -1  -7  -5

# Input :
# N=8
# arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output :
# 7  9  10  11  -5  -3  -4  -1


# gfg:

def move(arr, n):
    j = 0
    for i in range(n):
        if arr[i] >= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


# Driver program
arr = [1, -1, -3, -2, 7, 5, 11, 6]
n = len(arr)
print(move(arr, n))
