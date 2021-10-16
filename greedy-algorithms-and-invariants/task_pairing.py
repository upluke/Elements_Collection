# 17.1 Compute an optimum assignment of tasks
# the time is dominated by the time to sort, i.e.,O(nlogn)

import collections

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):

    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]


print(optimum_task_assignment([3, 4, 2, 1]))  # [[1,4], [2,3]]


# variant https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
# Example 1:
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.

# Example 2:
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.

# Time:  O(k^n * logr), the real complexity shoud be much less, but hard to analyze
# Space: O(n + k)

#  https://shareablecode.com/snippets/find-minimum-time-to-finish-all-jobs-python-solution-leetcode-
def minimumTimeRequired(jobs, k):
    """
    :type jobs: List[int]
    :type k: int
    :rtype: int
    """
    def backtracking(jobs, i, cap, counts):
        if i == len(jobs):
            return True
        for j in range(len(counts)):
            if counts[j]+jobs[i] <= cap:
                counts[j] += jobs[i]
                if backtracking(jobs, i+1, cap, counts):
                    return True
                counts[j] -= jobs[i]
            if counts[j] == 0:
                break
        return False

    jobs.sort(reverse=True)
    left, right = max(jobs), sum(jobs)
    while left <= right:
        mid = left + (right-left)//2
        if backtracking(jobs, 0, mid, [0]*k):
            right = mid-1
        else:
            left = mid+1
    return left


print(minimumTimeRequired([1, 2, 4, 7, 8], 2))

# Time:  O(k * k^n), the real complexity shoud be less, but hard to analyze
# Space: O(n + k)


def minimumTimeRequired2(jobs, k):
    """
    :type jobs: List[int]
    :type k: int
    :rtype: int
    """
    def backtracking(jobs, i, counts, result):
        if i == len(jobs):
            result[0] = min(result[0], max(counts))
            return
        for j in range(len(counts)):
            if counts[j]+jobs[i] <= result[0]:
                counts[j] += jobs[i]
                backtracking(jobs, i+1, counts, result)
                counts[j] -= jobs[i]
            if counts[j] == 0:
                break

    jobs.sort(reverse=False)
    result = [sum(jobs)]
    backtracking(jobs, 0, [0]*k, result)
    return result[0]


print(minimumTimeRequired([1, 2, 4, 7, 8], 2))
