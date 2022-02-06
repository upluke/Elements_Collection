# 4.6 Compute quotient without arithmetical operators
# https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
# Input : a = 10, b = 3
# Output : 3

# Input : a = 43, b = -8
# Output :  -5

# ele:
def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result


print(divide(10, 3))


# gfg:
# Time complexity : O(a)
# Auxiliary space : O(1)

# def divide(dividend, divisor):

#     # Calculate sign of divisor i.e.,
#     # sign will be negative only iff
#     # either one of them is negative
#     # otherwise it will be positive
#     sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1

#     # Update both divisor and
#     # dividend positive
#     dividend = abs(dividend)
#     divisor = abs(divisor)

#     # Initialize the quotient
#     quotient = 0
#     while (dividend >= divisor):
#         dividend -= divisor
#         quotient += 1

#      #if the sign value computed earlier is -1 then negate the value of quotient

#     if sign ==-1:
#       quotient=-quotient

#     return quotient


# a = 10
# b = 3
# print(divide(a, b))
# a = 43
# b = -8
# print(divide(a, b))

# As every number can be represented in base 2(0 or 1), represent the quotient in binary form by using shift operator as given below :

# Determine the most significant bit in the quotient. This can easily be calculated by iterating on the bit position i from 31 to 1.
# Find the first bit for which divisor << i                     is less than dividend and keep updating the ith bit position for which it is true.
# Add the result in temp variable for checking the next position such that (temp + (divisor << i) ) is less than dividend.
# Return the final answer of quotient after updating with corresponding sign.
def divide(dividend, divisor):

    sign = (-1 if((dividend < 0) ^
                  (divisor < 0)) else 1)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i

    if sign == -1:
        quotient = -quotient
    return quotient


a = 10
b = 3
print(divide(a, b))

# a = 43;
# b = -8;
# print(divide(a, b));
