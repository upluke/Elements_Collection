# 8.4 normalize pathnames

#https://leetcode.com/problems/simplify-path/#
# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.

# Example 2:
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

# Example 3:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

# Example 4:
# Input: path = "/a/./b/../../c/"
# Output: "/c"


# time: O(n), where n is the length of the pathname.
def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Empty string is not a valid path.')

    path_names = []  # Uses list as a stack.
    # Special case: starts with '/', which is an absolute path.
    if path[0] == '/':
        path_names.append('/')

    for token in (token for token in path.split('/')
                  if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else:  # Must be a name.
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):]  # Avoid starting '//'.


print(shortest_equivalent_path("/home/"))  # "/home"
# print(shortest_equivalent_path("/../")) # "/"
print(shortest_equivalent_path("/home//foo/"))  # "/home/foo"

print(shortest_equivalent_path("/a/./b/../../c/"))  # "/c"


# lc:
def simplifyPath(path):
    sp = path.split('/')
    stack = []
    for s in sp:
        if s:
            if s == '..':
                stack = stack[:-1]  # cut off the last one
            elif s != '.':
                stack.append(s)
    return '/' + '/'.join(stack)


print(simplifyPath("/a//b////c/d//././/.."))


# liz:
def simplifyPath(path):
    stack = []
    for token in path.split('/'):
        if token in ('', '.'):
            pass
        elif token == '..':
            if stack:
                stack.pop()
        else:
            stack.append(token)
    return '/' + '/'.join(stack)


simplifyPath("/a//b////c/d//././/..")


# init
def simplifyPath(path):
    arr = []
    res = ""
    splitPath = path.split("/")
    for sp in splitPath:
        if sp != '.' and sp != '..' and sp != '':
            arr.append(sp)
        elif sp == '..':
            if len(arr):
                arr.pop()
            continue
    for a in arr:
        res += "/"+a
    if res == "":
        return "/"
    else:
        return res


print(simplifyPath("/home/"))  # "/home"
print(simplifyPath("/../"))  # "/"
print(simplifyPath("/home//foo/"))  # "/home/foo"

print(simplifyPath("/a/./b/../../c/"))  # "/c"
