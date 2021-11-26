# 15.4 Generate permuations
# THe time complexity is determinded by the numebr of recursive calls, since within each function the time spent is O(1), not including the time in the subcalls. The number of funciton calls, C(n) satisfies the recurrence C(n)=1+nC(n-1) for n>=1, with C(0)=1. Expanding this, we see C(n)=1+n+n(n-1)+n(n-1)(n-2)+...+n!=n!(1/n! +1/(n-1)!+1/(n-2)!+...+1/1!). The sum (1+1/1!+1/2!+...+1/n!) tends to Euler's number e, so C(n) tends to (e-1)n!, i.e., O(n!). THe time complexity T(n) is O(nxn!), since we do O(n) computation per call outside of the recursive calls.

# element1: (refer to page55 for more explanation)
def permutations(A):
    def directed_permutations(i):
        if i == len(A)-1:
            result.append(A.copy())
            return

        # try every possibility for A[i]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # generate all permutations for A[i+i:]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result


print(permutations([1, 2, 3]))


# init:
# def permutations(A):
#   path, res=[],[]
#   def helper(A, path, res):
#     if len(A)==0:
#       res.append(path)

#     for i in range(len(A)):
#       helper(A[:i]+A[i+1:], path+[A[i]], res)

#   helper(A, path, res)
#   return res

# print(permutations([1,2,3]))
