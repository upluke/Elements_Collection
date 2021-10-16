# 17.0

# 0 // ANY NUMBER GREATER THAN 0 IS 0
# any number % any number greater than it is itself
# we perform 6 iterations, and each iteration does a constant amount of computation,
#  so the time complexity is O(1)
def change_making(cents):
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += cents//coin
        cents %= coin
    return num_coins


print(change_making(90))
