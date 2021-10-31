# 15.3 generate all nonattacking placements of n-queens
# the time complexity is at tleast the number of nonattacking placemnet. Nobody knows how many nonattacking placements there are as a funciton of n, but it increases very repidly with n, and is no more than n!(since each queen must be on a diffirent row)
# https://www.youtube.com/watch?v=Ph95IHmRp5M
# https://leetcode.com/problems/n-queens/
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]


def n_quees(n):
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement.copy())
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            if all(
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result


print(n_quees(4))


# yt: backtracking
def n_quees(n):
    col = set()
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)

    res = []
    board = [["."]*n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        # go through every row see which positions are we allowed to place a queen
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
    backtrack(0)
    return res


print(n_quees(4))
