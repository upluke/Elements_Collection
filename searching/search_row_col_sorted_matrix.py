# 11.6 Search in a 2D sorted array
# https://leetcode.com/problems/search-a-2d-matrix/

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# ele:
# In each iteration, we remove a row or a column, which means we inspect at most m+n-1 elements, yielding an O(m+n) time complexity.
def matrix_search(A, x):

    row, col = 0, len(A[0])-1
    # keeps searching while there are unclassified rows and columns
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1  # eliminate this row
        else:  # A[row][col]>x
            col -= 1  # eliminate this column

    return False


print(matrix_search([[-2, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9,
      22], [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]], 8))


# lc: O(log mn)

# [mid/n][mid%n] explain:
# Suppose m = number of rows, n = number of columns. Since the matrix is ordered, we can treat the matrix as a m*n 1D array (Flatten the 2D array). The matrix[mid/n][mid%n] is just operate the 2D matrix as an 1D array.

# For example, m = 3, n = 4, m*n = 12, lo = 0, hi = 11
# mat 0 1 2 3
# 0 | 1 2 3 4
# 1 | 5 6 7 8
# 2 | 9 10 11 12
# we can treat it as
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, with index from 0 to 11.

# Now imagine we want to locate the (lo + hi)/2 elements in this imaginary array (Actually, just flatten it). That is the fifth element in this array, which is 6 (0-index).
# Let us look at the original matrix, we can see that 06 located at mat[1][1], which is mat[ 5/4 ][ 5%4 ].
def searchMatrix(self, matrix, target):
    n = len(matrix[0])
    lo, hi = 0, len(matrix) * n
    while lo < hi:
        mid = (lo + hi) / 2
        x = matrix[mid/n][mid % n]
        if x < target:
            lo = mid + 1
        elif x > target:
            hi = mid
        else:
            return True
    return False


print(matrix_search([[-2, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9,
      22], [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]], 8))


# init:
# def matrix_search (A, x):
#   nums=[]
#   for a in A:
#     nums+=a

#   if x in nums:
#     return True
#   else:
#     return False


# print(matrix_search([[-2,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24], [6, 8,9,12,25], [8,10,12,13,40]], 8))
