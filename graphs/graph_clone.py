# 18.5 Clone a graph
# the space complexity is O(|V|+|E|), which is the space taken by the result. Excluding the space for the result, the space complexity is O(|V|) -- this comes form the hash table, as well as the BFS queue.
# https://leetcode.com/problems/clone-graph/
# https://www.youtube.com/watch?v=e5tNvT1iUXs
import collections


class GraphVertex():
    def __init__(self, label):
        self.label = label
        self.edges = []


def clone_graph(graph: GraphVertex) -> GraphVertex:

    if graph is None:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}
    while q:
        v = q.popleft()
        for e in v.edges:
            # Try to copy vertex e.
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            # Copy edge.
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[graph]


n0, n1, n2 = GraphVertex(0), GraphVertex(1), GraphVertex(2)
n3, n4 = GraphVertex(3), GraphVertex(4)
n0.edges.append(n1)
n0.edges.append(n2)
n1.edges.append(n2)
n1.edges.append(n3)
n1.edges.append(n4)
n2.edges.append(n3)
n3.edges.append(n4)

print(clone_graph(n0))

# int[k]	array(tuple(int[from], int[to])[edge])	void

# 4	[[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 1], [1, 3]]	TODO

# 5	[[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]]	TODO


# gfg:
# Python program to clone a directed acyclic graph.
#  https://www.geeksforgeeks.org/clone-directed-acyclic-graph/
class Node():

    # key is the value of the node
    # adj will be holding a dynamic
    # list of all Node type neighboring
    # nodes
    def __init__(self, key=None, adj=None):
        self.key = key
        self.adj = adj

# Function to print a graph, depth-wise, recursively


def printGraph(startNode, visited):

    # Visit only those nodes who have any
    # neighboring nodes to be traversed
    if startNode.adj is not None:

        # Loop through the neighboring nodes
        # of this node. If source node not already
        # visited, print edge from source to
        # neighboring nodes. After visiting all
        # neighbors of source node, mark its visited
        # flag to true
        for i in startNode.adj:
            if visited[startNode.key] == False:
                print("edge %s-%s:%s-%s" %
                      (hex(id(startNode)), hex(id(i)), startNode.key, i.key))
                if visited[i.key] == False:
                    printGraph(i, visited)
                    visited[i.key] = True

# Function to clone a graph. To do this, we start
# reading the original graph depth-wise, recursively
# If we encounter an unvisited node in original graph,
# we initialize a new instance of Node for
# cloned graph with key of original node


def cloneGraph(oldSource, newSource, visited):
    clone = None
    if visited[oldSource.key] is False and oldSource.adj is not None:
        for old in oldSource.adj:

            # Below check is for backtracking, so new
            # nodes don't get initialized everytime
            if clone is None or (clone is not None and clone.key != old.key):
                clone = Node(old.key, [])
            newSource.adj.append(clone)
            cloneGraph(old, clone, visited)

            # Once, all neighbors for that particular node
            # are created in cloned graph, code backtracks
            # and exits from that node, mark the node as
            # visited in original graph, and traverse the
            # next unvisited
            visited[old.key] = True
    return newSource

# Creating DAG to be cloned
# In Python, we can do as many assignments of
# variables in one single line by using commas

# Input :

# 0 - - - > 1 - - - -> 4
# |        /  \        ^
# |       /    \       |
# |      /      \      |
# |     /        \     |
# |    /          \    |
# |   /            \   |
# v  v              v  |
# 2 - - - - - - - - -> 3


# Output : Printing the output of the cloned graph gives:
# 0-1
# 1-2
# 2-3
# 3-4
# 1-3
# 1-4
# 0-2

n0, n1, n2 = Node(0, []), Node(1, []), Node(2, [])
n3, n4 = Node(3, []), Node(4)
n0.adj.append(n1)
n0.adj.append(n2)
n1.adj.append(n2)
n1.adj.append(n3)
n1.adj.append(n4)
n2.adj.append(n3)
n3.adj.append(n4)

# flag to check if a node is already visited.
# Stops indefinite looping during recursion
visited = [False] * (5)
print("Graph Before Cloning:-")
printGraph(n0, visited)

visited = [False] * (5)
print("\nCloning Process Starts")
clonedGraphHead = cloneGraph(n0, Node(n0.key, []), visited)
print("Cloning Process Completes.")

visited = [False]*(5)
print("\nGraph After Cloning:-")
printGraph(clonedGraphHead, visited)
