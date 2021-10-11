# 13.2 Merge two sorted arrays
# time: O(m+n) space: O(1) additional space
# similar concept, solution 6.4 page 74, replace_and_remove.py
def merge_two_sorted_arrays(A, m, B, n):
    i, j, write_idx = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[write_idx] = A[i]
            i -= 1
        else:
            A[write_idx] = B[j]
            j -= 1
        write_idx -= 1
    while j >= 0:
        A[write_idx] = B[j]
        write_idx, j = write_idx - 1, j - 1
    return A


print(merge_two_sorted_arrays(
    [3, 13, 17, 0, 0, 0, 0, 0], 3, [3, 7, 11, 19], 4))  # [3, 3, 7, 11, 13, 17, 19, 0]
