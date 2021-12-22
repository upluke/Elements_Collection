# 17.4 the 3-sum problem
# the addtional space needed is O(1), and the tiem complexity is the sum of of the time taken to sort, O(n log n), and then to run the O(n) algorithm to find a pair in a sorted array that sums to a specified value, which is O(n^2) overall.

def has_three_sum(A, t):
    A.sort()

    def has_two_sum(A, t):
        l, r = 0, len(A)-1
        while l <= r:
            # if there're two sum
            if A[l] + A[r] == t:
                return True
            elif A[l]+A[r] > t:
                r -= 1
            else:
                l += 1
        return False
    # finds if the sum of two numbers in A equals to t-a
    return any(has_two_sum(A, t-a) for a in A)


print(has_three_sum([11, 2, 5, 7, 3], 21))


# two_sum.py
# with sorted array:
# def has_two_sum(A, t):
#   l, r=0, len(A)-1

#   while l<=r:
#     # if there're two sum
#     if A[l] +A[r]==t:
#       return [l, r]
#     elif A[l]+A[r]>t:
#       r-=1
#     else:
#       l+=1
#   return -1

# print(has_two_sum([-2, 1, 2, 4, 7, 11], 13))
