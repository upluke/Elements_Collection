# time complexity is given by T(n)=T(n/2)+c, where c is a constant. This solves to T(n)=O(log n) where n is the number of entries in the array
def bsearch(t, A):
    L, R = 0, len(A)-1
    while L <= R:
        M = L+(R-L)//2  # M=(L+R)//2 can potentially lead to overflow
        if A[M] < t:
            L = M+1
        elif A[M] == t:
            return M
        else:
            R = M-1
    return -1


print(bsearch(5, [1, 2, 3, 4, 5, 6, 7]))
