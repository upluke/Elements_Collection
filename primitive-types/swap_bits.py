# 4.2 Swap Bits
# https://www.geeksforgeeks.org/how-to-swap-two-bits-in-a-given-integer/
# https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/
#time: O(1)

# example 1:
# Input: n = 28, p1 = 0, p2 = 3
# Output: 21
# 28 in binary is 11100. (count right to left)If we swap 0'th and 3rd digits,
# we get 10101 which is 21 in decimal.

# example 2:
# Input: n = 20, p1 = 2, p2 = 3
# Output: 24

# note:

# use n & 1 to tell odd or even

# XOR with 1 will toggle the bits
# 0 ^ 1 = 1
# 1 ^ 1 = 0

# XOR with 0 will have no impact
# 0 ^ 0 = 0
# 1 ^ 0 = 1

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will sawp them by flipping their values.
        # Select the bits to flip with bit_mask.
        # Since x^1=0 when x=1 and 1 when x=0, we can perform the flip XOR
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


print(swap_bits(28, 0, 3))  # 21

# https://www.techiedelight.com/swap-two-bits-given-position-integer/


# x>>i -> 28>>0 -> 1 1 1 0 0 >>0 = 1 1 1 0 0:28
# x>>j -> 28>>3 -> 1 1 1 0 0 >>3 = 0 0 0 1 1:3

# (x>>i) & 1 =0
#  11100:28
# &    1
# -------
#  00000

# (x>>j) & 1 =1
#  00011:3
# &    1
# -------
#  00001

# 1<<i:0 = 1
# 1<<j:3 = 8
# (1<<i)|(1<<j) -> 1|8 =9
#  00001
# |
#  01000
# -------
#  01001

# x:28 ^=bit_mask:9 =21
# 11100
# ^
# 01001
# -------
# 10101


# ol:
def swap(x, i, j):

    # if bits are different at position `i` and `j`
    if (((x & (1 << i)) >> j) ^ ((x & (1 << j)) >> j)) == 1:
        x ^= (1 << i)
        x ^= (1 << j)

    return x


print(swap_bits(28, 0, 3))  # 21
