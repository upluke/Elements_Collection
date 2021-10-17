
#       A
#     /   \
#   B       C
#  / \       \
# D   E  一    F
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# Using a Python dictionary to act as an adjacency list

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        print("---", visited)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, 'A')

# graph basics:
# https://adonais0.github.io/20181119/leetcode-graph/
