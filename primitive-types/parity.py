# 4.1 computing the parity of a word
# parity checks are used to detect single bit errors in data storage and communicaiton
# t:O(n) where n is the word size
def parity(x):
    result = 0
    while x:
        result ^= x & 1  # 1step: x & 1 2step: result ^=...
        x >>= 1
    return result


print(parity(13))

# 13: 1101     13&1=1   result:0 ^ 1=1
# 6:  0110     6&1=0    result:1 ^ 0=1
# 3:  0011     3&1=1    result:1 ^ 1=0
# 1:  0001     1&1=1    result:0 ^ 1=1
