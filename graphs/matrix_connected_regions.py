
# 18.2 Paint a boolean matrix
# The time complexity is the same as that of BFS, i.e., O(mn). The space complexity is a little better than the worse-case for BFS, since there are at most O(m+n) vertices that are at the same distance from a given entry
# https://www.cesar-jimenez.com/post/2020-06-06-solving-matrix-boolean-bfs/

import collections


def flip_color(x, y, image):

    color = image[x][y]
    q = collections.deque([(x, y)])
    print(q)
    image[x][y] = not image[x][y]  # Flips.
    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            print("&&", next_x, next_y)
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
                    and image[next_x][next_y] == color):
                # Flips the color.
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))
    return image


image = [[True, True, True], [True, True, False], [True, False, True]]
print(flip_color(1, 1, image))

#  00     01    02
# True   True   True
#  10     11    12
# True   True   False
#  20     21    22
# True   False  True


# recursion:
# time complexity is the same as that of DFS
def flip_color(x, y, image):
    color = image[x], [y]
    image[x][y] = not image[x][y]  # flips
    for next_x, next_y in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
                and image[next_x][next_y] == color):
            flip_color(next_x, next_y, image)


image = [[True, True, True], [True, True, False], [True, False, True]]
print(flip_color(1, 1, image))
