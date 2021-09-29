# 4.1 computing the parity of a word
# https://loctv.wordpress.com/2017/12/23/compute-the-parity-of-a-word-python3/
# parity checks are used to detect single bit errors in data storage and communicaiton

# 1 bruteforce algorithm
# Time complexity: O(n) with n is number of bits of the given number.
import parity1


def parity(x):
    result = 0
    while x:
        result ^= x & 1  # 1st step: x & 1    2nd step: result ^=...
        x >>= 1
    return result


print(parity(13))

# 13:1101
# &
# 1: 0001
# ------------
#       1


# 13: 1101     13&1=1   result:0 ^ 1=1
# 6:  0110     6&1=0    result:1 ^ 0=1
# 3:  0011     3&1=1    result:1 ^ 1=0
# 1:  0001     1&1=1    result:0 ^ 1=1


# 2 Improved brute force
# Time complexity: O(k), with k is the number of lowest set bit.
# erase the lowest set bit in a word in a single operation, thereby improving performance in the best- and average-cases. Here is a great bit-fiddling trick which you should commit to memory: x&(x-1) equals x with its lowest set bit erased. For example, if x= 00101100, then x-1= 00101011, so x&(x-1)=00101100 &00101011 = 00101000. This fact can be used to reduce the time complexity.Let k be the number of bits set to 1 in a particular word. (for example, for 10001010,k=3.) Then time complexity of the algorithm below is O(k)

# 44: 00101100
# &
# 43: 00101011
# -------------
# 40: 00101000

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1  # drops the lowest set bit of x
    return result


print(parity(13))

# result:0^1=1           result:1^1=0       result:0^1=1
# x:13: 0001101            12: 0001100        8: 0001000
# &
# x:12: 0001100            11: 0001011        7: 0000111
# -------------
# x:12: 0001100             8: 0001000        0: 0000000


# 3 Caching approach
# Time complexity: O(n/L), with L is the width we cache the results.
# When you have to perform a large number of parity computations, and, more generally, any kind of bit fiddling computations, two keys to performnace are processing multiple bits at a time and caching results in an array-based lookup table. First we demonstrate caching. We can compute the parity of a 64-bit integer by groupng its bits into four nonoverlapping 16 bit subwords, computing the parity of each subwords, and then computing the parity of these four subresults.  We choose 16 since 2^16 =65536 is relatively small, which makes i feasible to cache the parity of all 16-bit words using an array. Furthermore, since 16 evenly divides 64, the code is simpler than if we werer to use 10 bits subwords.We illustrate the approach with a lookup table for 2-bit words. The cache is <0,1,1,0> -- these are the parities of (00), (01), (10), (11), respectively. To compute the parity of (11001010) we would compute the parities of (11),(00),(10),(10). By table lookup we see these are 0,0,1,1, respectively, so the final result is the parity of 0,0,1,1 which is 0.To lookup the parity of the first two bits in 11101010, we right shift by 6, to get 00000011, and use this as an index into the cache. To lookup the parity of the next two bits 10, we right shift by 4. However, right shift does not remove the leading 11 when we right shift by 4 – results in 00001110. To get the last two bits after the right shift by 4, we bitwise-AND 00001110 with 00000011 (the “mask” to extract the last 2 bits). The result is 00000010. Similar masking needed fir the two other 2-bit lookups. Given PRECOMPUTED_PARITIES is an array of parities of all numbers from 0 up to 65535. The code is fairly understandable.


# F x 1 = 15
# F x 16 = 240
# F x 16 x 16 = 3840
# F x 16 x 16 x 16 = 61440
# 15 + 240 + 3840 + 61440 = 65535


PRECOMPUTED_PARITY = [parity1.parity(i) for i in range(1 << 16)]


def parity(x):
    mask_size = 16
    bit_mask = 0xFFFF
    # first right shift 48 to get first 16 bits
    # then righ shift 32 to get next 16 bits
    # then right shift 16 to get next 16 bits
    # final and with BIT_MASK to get the final 16 bits
    # and xor all of them together to get final result
    return (PRECOMPUTED_PARITY[x >> (3*mask_size)] ^
            PRECOMPUTED_PARITY[(x >> (2*mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^ PRECOMPUTED_PARITY[x & bit_mask])


print(parity(13))


# 4 Use the parity property
# Time complexity: O(logn)
# XOR has the property of being associative, it does not matter how we group bits, as well as commutative, the order in which we perform the XORs does not change result. The XOR of a group of bits is its parity. For example, the parity of [b63,b62,…,b2,b1,b0] equals the parity of the XOR of [b63,b62,..b32] and [b31,b30,..,b2,b1]. The XOR of these two 32-bit values can be computed with a single shift and a single 32-bit XOR instruction. We repeat the same operation on 32-, 16-, 8-, 4-, 2- and 1-but operands to get the final result. Note that the leading bits are not meaningful, and we have to explicitly extract the result from the least-significant bit.

# Example with an 8-bit word. The parity of 11010111 is the asme as the parity of 1101 XOR with 0111 – results in 1010. This in turn is the same as the parity of 10 XOR with 10 – results in 00. The final result of 0 XOR with 0 is 0. Note that the first XOR yields 11011010 and only the last 4 bits are relevant going forward. The second XOR yields 11101100, and only the last 2 bits are relevant. The third XOR yields 10011010. The last bit is the result, and to extract it we have to bitwise AND with 00000001. The code:

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


print(parity(13))
