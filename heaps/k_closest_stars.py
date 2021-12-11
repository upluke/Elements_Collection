# 10.4 compute the k closest stars
# The time complexity is O(n log k) and the space complexity is O(k)
# https://www.geeksforgeeks.org/find-the-k-closest-points-to-origin-using-priority-queue/

# Input: [(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)], K = 3
# Output: [(1, 0), (2, 1), (1, -4)]
# Explanation:
# Square of Distances of points from origin are
# (1, 0) : 1
# (2, 1) : 5
# (3, 6) : 45
# (-5, 2) : 29
# (1, -4) : 17
# Hence for K = 3, the closest 3 points are (1, 0), (2, 1) & (1, -4).

# Input: [(1, 3), (-2, 2)], K = 1
# Output: [(-2, 2)]
# Explanation:
# Square of Distances of points from origin are
# (1, 3) : 10
# (-2, 2) : 8
# Hence for K = 1, the closest point is (-2, 2).


# ele:
import heapq
import heapq as hq
import heapq
import math


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_stars(stars, k):
    # max_heap to store the closest k stars seen so far
    max_heap = []
    for star in stars:
        # Add each star to the max-heap. If the max-heap size exceeds k, remove
        # the maximum element from the max-heap.
        # As python has only min-heap, insert tuple (negative of distance, star)
        # to sort in reversed distance order.
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)

    # Iteratively extract from teh max-heap, which yields the stars sorted
    # according from furthest to closest
    return [s[1] for s in heapq.nlargest(k, max_heap)]


print(find_closest_k_stars([(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)], 3))


# gfg:
# Time Complexity: O(N + K * log(N))
# Auxiliary Space: O(N)

# Function to find the K closest points


def kClosestPoints(x, y, n, k):
    # Create a priority queue
    pq = []

    # Pushing all the points
    # in the queue
    for i in range(n):
        hq.heappush(pq, (x[i]*x[i]+y[i]*y[i], x[i], y[i]))

    print(pq)
    # Print the first K elements
    # of the queue
    for i in range(k):

        # Store the top of the queue
        # in a temporary pair
        p = hq.heappop(pq)

        # Print the first (x)
        # and second (y) of pair
        print("{} {}".format(p[1], p[2]))


# Driver code
if __name__ == '__main__':
    # x coordinate of points
    x = [1, -2]

    # y coordinate of points
    y = [3, 2]
    K = 1

    n = len(x)

    kClosestPoints(x, y, n, K)


# init:


def find_closest_k_stars(stars, k):
    hp = {}
    look_up = []
    res = []
    for idx, value in enumerate(stars):
        temp = value[0]**2 + value[1]**2
        hp[temp] = stars[idx]
        look_up.append(temp)

    heapq.heapify(look_up)
    smallest = heapq.nsmallest(3, look_up)

    for s in smallest:
        res.append(hp[s])

    return res


print(find_closest_k_stars([(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)], 3))
