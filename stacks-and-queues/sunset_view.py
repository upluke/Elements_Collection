# 8.5 Compute buildings with a sunset view
# you're given a series of buildings that have windows facing west. The buildings are in a straight line, and any building which is to the east of a building of equalor greater height cannnot view the sunset. Design an algorithm that processes buildings in east-to-west order and returns the set of buildings which view the sunset. Each building is specified by its height.

# although some individule steps may require amny pops, each building is pushed and popped at most once. THerefore, the run time to process n buildings is O(n), and the stack always holds precisely the buildings which currently have a view.
# https://www.geeksforgeeks.org/number-buildings-facing-sun/


# Input : arr[] = {7, 4, 8, 2, 9}
# Output: 3
# Explanation: As 7 is the first element, it can
# see the sunset.
# 4 can't see the sunset as 7 is hiding it.
# 8 can see.
# 2 can't see the sunset.
# 9 also can see the sunset.

# Input : arr[] = {2, 3, 4, 5}
# Output : 4


import collections
# ele:


def examine_buildings_with_sunset(sequence):
    tuple = collections.namedtuple('tuple', ('id', 'height'))

    temp = []
    for bldg_idx, bldg_height in enumerate(sequence):
        while temp and bldg_height >= temp[-1].height:
            temp.pop()
        temp.append(tuple(bldg_idx, bldg_height))

    return [c.id for c in reversed(temp)]


print(examine_buildings_with_sunset([2, 3, 4, 5]))


# gfg:
def countBuildings(arr, n):

    # Initialuze result (Note that first
    # building always sees sunlight)
    count = 1

    # Start traversing element
    curr_max = arr[0]
    for i in range(1, n):

        # If curr_element is maximum or
        # current element is equal,
        # update maximum and increment count
        if (arr[i] > curr_max or arr[i] == curr_max):

            count += 1
            curr_max = arr[i]

    return count


arr = [2, 3, 4, 5]
n = len(arr)
print(countBuildings(arr, n))
