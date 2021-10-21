# 5.2
# time:O(n), where n is the length of A
def plus_one(A):

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            # There is a carry-out, so we need one more digit to store the result.
            # A slick way to do this is to append a 0 at the end of the array,
            # and update the first entry to 1.
            A[0] = 1
            A.append(0)
    return A

# Yt:


def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits


print(plusOne([9, 5, 9]))
