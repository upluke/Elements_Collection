# 4.3 reverse bits
# time:O(n/L), for n-bit integers and L-bit cache keys.
# refer back to the original code for PRECOMPUTED_REVERSE

def reverse_bits(x) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size)
            | PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] <<
            (2 * mask_size) |
            PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size
            | PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask])

# print(reverse_bits(10))
# 1351510410656	405942121183313920
# 1351510410656 in binary is 0b10011101010101100010011000100010110100000, and its reverse in binary is 0b10110100010001100100011010101011100100000000000000000000000


# lc:
# https://leetcode.com/problems/reverse-bits/
def reverseBits(n):
    res = 0
    for i in range(32):
        res = (res << 1) ^ (n & 1)
        n >>= 1
#     return res
# print(reverseBits(00000010100101000001111010011100))
