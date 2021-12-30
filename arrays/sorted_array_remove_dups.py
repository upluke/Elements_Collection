# 5.5 Delete duplicates from a sorted array
# the time complexity is O(n), and the sapce complexity is O(1), since all that is needed is the two additional variables
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


# ele:

# return the number of v alid entries after deletion
def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index-1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))


# init:
def delete_duplicates(A):
    idx = 0

    for i in range(1, len(A)):
        if A[idx] != A[i]:
            idx += 1
            A[idx], A[i] = A[i], A[idx]

    # return len(nums[:idx+1])
    return A[:idx+1] + (len(A)-idx-1)*['_']


# print(delete_duplicates([0,0,1,1,1,2,2,3,3,4]))
# print(delete_duplicates([1,1,2]))
print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))
