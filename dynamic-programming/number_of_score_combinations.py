# time complexity is O(sn) (two loops, one to s, the other to n) and the space complexity is O(sn) (the size of the 2d array)
def num_combinations_for_final_score(final_score, individual_play_scores):
    # One way to reach 0
    num_combinations_for_final_score = [
        [1]+[0]*final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score+1):
            without_this_play = (
                num_combinations_for_final_score[i-1][j] if i >= 1 else 0)

            with_this_play = (
                num_combinations_for_final_score[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)

            num_combinations_for_final_score[i][j] = (
                without_this_play+with_this_play)
    return num_combinations_for_final_score[-1][-1]


print(num_combinations_for_final_score(12, [2, 3, 7]))


# lc:(back tracking)
def combinationSum(candidates, target):
    res = []
    backtrack(candidates, target, [], res)
    return res


def backtrack(candidates, target, temp, res):
    if target < 0:
        return
    if target == 0:
        res.append(temp)
        return

    for i in range(len(candidates)):
        backtrack(candidates[i:], target-candidates[i],
                  temp+[candidates[i]], res)


print(combinationSum([2, 3, 5], 8))


# yt: (DP)
def combinationSum(candidates, target):
    dp = [[] for _ in range(target+1)]

    for c in candidates:
        for i in range(1, target+1):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])
            else:
                for blist in dp[i-c]:
                    dp[i].append(blist+[c])

    return dp[target]


print(combinationSum([2, 3, 5], 8))
