# 4.0
# t:O(n)

# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/


def count_bits(x: int) -> int:
    # init:
    # count = 0
    # binary = str(bin(x))
    # count += binary.count("1")
    # return count

    count = 0
    while (x):
        count += x & 1
        x >>= 1
    return count


print(count_bits(6))  # 2
