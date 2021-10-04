# 6.2 Base conversion
# time: O(n(1+log_b2 b1)), where n is the length of s. The reasoning is as follows. First, we ferform n multiply-and-adds to get x from s. Then we perform log_b2 x multiply and adds to get the result. The value x is upper-bounded by b1^n, and log_b2(b1^n) = nlog_b2 b1

import string
import functools


def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper())
    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x*b1 + string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0)
    return ('-' if is_negative else '')+('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))


print(convert_base('1010100101', 2, 16))  # 2A5


# init:
# def convert_base(num_as_string, b1, b2):
#   decimal_num, base=0, 1

#   for n in reversed(num_as_string):
#     if n=='1':
#       decimal_num+= base
#     if base==1:
#       base=2
#     else:
#       base*=b1


#   res,base,tracker,unit_num,flag="",16,1,0,True

#   while flag :
#     unit_num=(decimal_num%base)

#     if unit_num==decimal_num:
#         flag=False

#     unit_num//=tracker

#     if unit_num<10:
#       res+= str(unit_num)
#     if unit_num<=15 and unit_num>9:
#       res+=chr(unit_num+55)

#     if tracker==1:
#         tracker=16
#     else:
#         tracker*=b2

#     base*=b2

#   return res[::-1]


# print(convert_base('1010100101',2,16))
