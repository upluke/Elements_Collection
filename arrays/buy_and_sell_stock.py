# 5.6 Buy and sell a stock once
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# ele:
# the time complexity is O(n) and the space complexity is O(1), where n is the length of the array
def buy_and_sell_sock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price-min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


print(buy_and_sell_sock_once([7, 1, 5, 3, 6, 4]))

# readable ver:


def max_profit(prices):
    min_price, res = float('inf'), 0.0
    for price in prices:
        diff = price-min_price
        res = max(res, diff)
        min_price = min(min_price, price)
    return res


print(max_profit([7, 1, 5, 3, 6, 4]))

# init：


def maxProfit(prices):
    prev, diff = prices[0], 0

    for i in range(1, len(prices)):
        if prices[i] < prev:
            prev = prices[i]
        else:
            diff = max(diff, prices[i]-prev)
    return diff


print(maxProfit([2, 4, 1]))
