import collections


WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    ss = s(x=0, y=4)  # not sure it's a correct setup
    ee = e(x=4, y=4)  # not sure it's a correct setup

    # Perform DFS to find a feasible path.
    def search_maze_helper(cur):
        # Checks cur is within maze and is a white pixel.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == ee:
            return True

        if any(
                map(
                    search_maze_helper,
                    map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
                        (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True
        # Cannot find a path, remove the entry added in path.append(cur).
        del path[-1]
        return False

    path = []
    search_maze_helper(ss)
    return path


maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

maze2 = [[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]]


# not sure it's a correct setup
start = collections.namedtuple('Coordinate', ('x', 'y'))
# not sure it's a correct setup
des = collections.namedtuple('Coordinate', ('x', 'y'))


print(search_maze(maze, start, des))


# the Maze -- letcode
# https://www.youtube.com/watch?v=eZWBLcurY8g
# *it won’t stop rolling until hitting a wall!

# Input 1: a maze represented by a 2D array
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.


def haspath(maze, start, des):

    queue = collections.deque()
    # put starting position into queue
    queue.append((start[0], start[1]))

    # cache visited position
    visited = set()
    visited.add((start[0], start[1]))

    # boundaries of maze
    m, n = len(maze), len(maze[0])

    while queue:  # starting BFS

        # pop out what we have in the initial posiitoin, which are the coordinates we hash in
        i, j = queue.popleft()

        if [i, j] == des:
            return True

        # check four directions
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            # record inital position
            x, y = i, j
            # keep rolling until hit the wall:
            # two conditions,1: keep rolling within the white spaces; 2: ball can't go out of hte boundary
            # {check x and left and right boundary} and {check y and up and down boundary}  and {check white space}
            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                # keep rolling
                x += dx
                y += dy
            # when hit the wall, backtrack one step to stop position
            x -= dx
            y -= dy
            # pick the next direction by putting the position back into the queue and reprocess it
            # if not processed, put the position into the queue and process it
            if (x, y) not in visited:
                queue.append([x, y])
                # cache it into hash set
                visited.add((x, y))


maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(haspath(maze, [0, 4], [4, 4]))
