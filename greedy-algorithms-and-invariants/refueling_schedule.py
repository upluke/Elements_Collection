# 17.6 The gasup problem
# https://leetcode.com/problems/gas-station/
# https://www.youtube.com/watch?v=lJwbPZGo05A

# ele:
import collections


def find_ample_city(gallons, distances):
    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple(
        'CityAndRemainingGas', ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i-1] - distances[i-1]
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons)
    return city_remaining_gallons_pair.city


print(find_ample_city([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(find_ample_city([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2]))

# lc:


def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i]-cost[i])
        if total < 0:
            total = 0
            res = i+1
    return res


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2]))
