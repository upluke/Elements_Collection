# # init:
# def search_first_of_k(A, k):
#   L,R=0, len(A)-1

#   while L<=R:
#     M=L+(R-L)//2
#     if A[M]<k:
#       L=M+1
#     elif A[M]==k:
#       if A[M-1]!=k:
#         return M
#       else:
#         R-=1
#     else:
#       R=M-1

# print(search_first_of_k([-14, -10, 2, 108, 108, 243, 285, 285, 401], -108)) #3


# Time: O(log n) -- ths is because each iteration reduces the size of the candidate set by half
def search_first_of_k(A, k):
    left, right, result = 0, len(A)-1, -1
    # A[left:right +1] is the candidate set
    while left <= right:
        mid = (left+right)//2
        if A[mid] > k:
            right = mid-1
        elif A[mid] == k:
            result = mid
            right = mid-1  # Nothing to the right of mid can be solution
        else:  # A[mid]<k
            left = mid+1
    return result


print(search_first_of_k([-14, -10, 2, 108, 108, 243, 285, 285, 401], 108))  # 3
