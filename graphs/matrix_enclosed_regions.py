# 18.3 Compute enclosed regions
# the time and space complexity are the same as those for BFS, namely O(mn), where m and n are the number of rows and columns in A.
# https://leetcode.com/problems/surrounded-regions/

# Example:
# X X X X          X X X X
# X O O X  =>      X X X X
# X X O X          X X X X
# X O X X          X O X X

# idx:
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
import collections


def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    q = collections.deque([(i, j) for k in range(n)
                          for i, j in ((k, 0), (k, m-1))] +
                          [(i, j) for k in range(m)
                          for i, j in ((0, k), (n-1, k))])
    print(q)
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'O':
            board[x][y] = 'T'
            q.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
    board[:] = [['X' if c != 'T' else 'O' for c in row] for row in board]
    return board


print(fill_surrounded_regions([["X", "X", "X", "X"], [
      "X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))

# gfg:
# Time Complexity of the above solution is O(MN). Note that every element of matrix is processed at most three times.
# https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/

# Size of given matrix is M x N
M = 6
N = 6

# A recursive function to replace previous
# value 'prevV' at '(x, y)' and all surrounding
# values of (x, y) with new value 'newV'.


def floodFillUtil(mat, x, y, prevV, newV):

    # Base Cases
    if (x < 0 or x >= M or y < 0 or y >= N):
        return

    if (mat[x][y] != prevV):
        return

    # Replace the color at (x, y)
    mat[x][y] = newV

    # Recur for north, east, south and west
    floodFillUtil(mat, x + 1, y, prevV, newV)
    floodFillUtil(mat, x - 1, y, prevV, newV)
    floodFillUtil(mat, x, y + 1, prevV, newV)
    floodFillUtil(mat, x, y - 1, prevV, newV)

# Returns size of maximum size subsquare
#  matrix surrounded by 'X'


def replaceSurrounded(mat):

    # Step 1: Replace all 'O's with '-'
    for i in range(M):
        for j in range(N):
            if (mat[i][j] == 'O'):
                mat[i][j] = '-'

    # Call floodFill for all '-'
    # lying on edges
            # Left Side
    for i in range(M):
        if (mat[i][0] == '-'):
            floodFillUtil(mat, i, 0, '-', 'O')

    # Right side
    for i in range(M):
        if (mat[i][N - 1] == '-'):
            floodFillUtil(mat, i, N - 1, '-', 'O')

    # Top side
    for i in range(N):
        if (mat[0][i] == '-'):
            floodFillUtil(mat, 0, i, '-', 'O')

    # Bottom side
    for i in range(N):
        if (mat[M - 1][i] == '-'):
            floodFillUtil(mat, M - 1, i, '-', 'O')

    # Step 3: Replace all '-' with 'X'
    for i in range(M):
        for j in range(N):
            if (mat[i][j] == '-'):
                mat[i][j] = 'X'


# Driver code
if __name__ == '__main__':

    mat = [['X', 'O', 'X', 'O', 'X', 'X'],
           ['X', 'O', 'X', 'X', 'O', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'X'],
           ['O', 'X', 'X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'O'],
           ['O', 'O', 'X', 'O', 'O', 'O']]

    replaceSurrounded(mat)

    for i in range(M):
        print(*mat[i])
