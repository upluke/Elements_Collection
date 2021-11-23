
# 13.4 remove first-name duplicates
# time: O(nlogn) space: O(1)http://talk.elementsofprogramminginterviews.com/t/remove-first-name-duplicates/808/2
import itertools


def eliminate_duplicate(A):

    A.sort()  # Makes identical elements become neighbors.
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx - 1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]


eliminate_duplicate([["Lan", "Botham"], ["David", "Gower"], [
                    "Lan", "Bell"], ["Lan", "Chappell"]])


def eliminate_duplicate_pythonic(A):
    A.sort()
    write_idx = 0
    for cand, _ in itertools.groupby(A):
        A[write_idx] = cand
        write_idx += 1
    del A[write_idx:]


eliminate_duplicate_pythonic([["Lan", "Botham"], ["David", "Gower"], [
                             "Lan", "Bell"], ["Lan", "Chappell"]])


# init:
def eliminate_duplicate(A):
    hp = {}
    for name in A:
        key = tuple(name)
        hp[name[0]] = hp.get(key, [])+name
    print(hp.values())


eliminate_duplicate([["Lan", "Botham"], ["David", "Gower"], [
                    "Lan", "Bell"], ["Lan", "Chappell"]])
