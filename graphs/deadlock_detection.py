# 18.4 Deadlock detection
# THe time complexity of DFS is O(|V|+|E|): we iterate over all vertices, and spend a constant amount of time per edge. The space complexity is O(|V|), which is the maximum stack depth -- if we go deeper than |V| calls, some vertex must repeat, implying a cycle in the garph, which leads to early termination.

class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self) -> None:

        self.color = GraphVertex.WHITE

        self.edges = []


def is_deadlocked(graph) -> bool:
    def has_cycle(cur):
        # Visiting a gray vertex means a cycle.
        if cur.color == GraphVertex.GRAY:
            return True

        cur.color = GraphVertex.GRAY  # Marks current vertex as a gray one.
        # Traverse the neighbor vertices.
        if any(next.color != GraphVertex.BLACK and has_cycle(next)
               for next in cur.edges):
            return True
        cur.color = GraphVertex.BLACK  # Marks current vertex as black.
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex)
               for vertex in graph)

# int	array(tuple(int[from], int[to])[edge])[graph]	bool
# 2	[[0, 1], [1, 0]]	true	A simple two nodes cycle
# 3	[[0, 1], [1, 2], [2, 0]]	true	A simple three nodes cycle
# 4	[[0, 1], [0, 2], [0, 3]]	false	A star tree
# 4	[[0, 1], [1, 2], [2, 3]]	false	A line
# 4	[[0, 1], [1, 2], [2, 3], [3, 1]]	true	A line

# variant: Course Schedule
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# liz:
def canFinish(numCourses, prerequisites):
    # setting up the graph
    courses = [[] for i in range(numCourses)]

    for pair in prerequisites:
        courses[pair[0]].append(pair[1])

    # recursive visit function, to detect loops in the graph
    # if there is a loop in the graph, then that means that the courses in that loop cannot be completed
    def visit(course, history):
        # if we have previously visited this course, then we have detected a loop and we return false
        if history[course]:
            return False
        else:
            # mark this course as visited
            history[course] = True
            # visit each prerequisite course
            for prereq in courses[course]:
                if not visit(prereq, history):
                    return False
            history[course] = False
        return True

    # now create the history array, and visit each course
    history = [False for i in range(numCourses)]

    for course in range(numCourses):
        if not visit(course, history):
            return False

    return True

# print(canFinish(2, [[1,0]] ))
