
# 16.5 Search for a sequence in a 2d array
# the time complexity is O(nml), hwere n and m are the dimensions of A, and l is the length of S -- we do a constant amount of work within each call to the recursive function, not including the time spent in recursive subcalls, and the number of acalls is not more than l times the number of entries in the 2D array. The cache itself cannot have more than nml keys, so the space complexity is O(nml).
# https://stackoverflow.com/questions/39584214/search-for-a-sequence-in-a-2d-array-visit-each-entry-only-once
import functools


def is_pattern_contained_in_grid(grid, pattern):
    @functools.lru_cache(None)
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if len(pattern) == offset:
            # Nothing left to complete.
            return True

        # Early return if (x, y) lies outside the grid or the character
        # does not match or we have already tried this combination.
        if (not (0 <= x < len(grid) and 0 <= y < len(grid[x]))
                or grid[x][y] != pattern[offset]):
            return False

        return any(
            is_pattern_suffix_contained_starting_at_xy(*next_xy, offset + 1)
            for next_xy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

    return any(
        is_pattern_suffix_contained_starting_at_xy(i, j, offset=0)
        for i in range(len(grid)) for j in range(len(grid[i])))


# [[1, 2, 3],
#  [3, 4, 5],
#  [5, 6, 7]]
print(is_pattern_contained_in_grid(
    [[1, 2, 3], [3, 4, 5], [5, 6, 7]],  [1, 3, 4, 6]))  # true
# is_pattern_contained_in_grid([[1, 2, 3],[3, 4, 5],[5, 6, 7]],  [1, 2, 3, 4]) # false
