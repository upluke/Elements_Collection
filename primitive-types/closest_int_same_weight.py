# 4.4 Find a closest integer with the same weight
# The time complexity is O(n), where n is the interger width
# https://www.geeksforgeeks.org/find-closest-integer-with-the-same-weight/
# The count of ones in binary representation of integer number is called the weight of that number. The following algorithm finds the closest integer with the same weight. For example, for 123 (0111 1011)₂, the closest integer number is 125 (0111 1101)₂.

# Input: X = 92
# Output: 90
# 90 is the closest number to 92 having
# equal number of set bits.

# Input: X = 17
# Output: 18

# Suppose we flip the bit at index k1 and flip the bit at index k2, k1>k2. Then the absolute value of the difference between the orignial integer and the new one is 2^k1 - 2^k2. To minimize this, we should make k1 as small as possible and k2 as close to k1. Since we must preserve the weight, the bit at index k1 has to be different from the bit in k2, otherwise the flips lead to an integer with different weight. This means the smallest k1 is the rightmost bit that's diffferent from the LSB, and k2 must be the very next bit. In summary, the correct approach is to swap the two rightmost consecutive bits that differ.

#                         &1
# 92 =1011100             0
# 46 =101110              0

# 46 =101110              0
# 23 =10111               1

# i=1
# 1<<i = 2:0010
# 1<<(i+1) =4:0100
# 2 | 4 =6:0110

# 92:1011100^6:0110
# 1011100
# ^
#    0110
# ------------
# 1011010: 90

def closest_int_same_bit_count(x):
    num_unsighned_bits = 64

    for i in range(num_unsighned_bits-1):
        print("i:", i, "x: ", x, 'x>>i: ', x >> i, 'x>>i&1: ', x >> i &
              1, 'x>>(i+1):', x >> (i+1), '(x>>(i+1))&1:', (x >> (i+1)) & 1)

        if(x >> i) & 1 != (x >> (i+1)) & 1:
            print("in: ", i, 1 << i, 1 << (i+1), (1 << i) | (1 << (i+1)))
            # swaps bit-i and bit-(i+1) #**** this how you get the number of the close 1 counts
            x ^= (1 << i) | (1 << (i+1))
            return x

    # raise error if all bits of x are 0 or 1
    raise ValueError('All bits are 0 or 1')


print(closest_int_same_bit_count(92))  # 90
