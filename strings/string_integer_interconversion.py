
import string
import functools


def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0')+x % 10))
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '')+''.join(reversed(s))


print(int_to_string(314))

# note:
# In Python, string.digits will give the lowercase letters ‘0123456789’.
# print(type(string.digits.index('3'))) # <class 'int'>
# print(s[s[0] in '-+':]) $ 315
# if s[s[0] in '-+' is true, s[1:] else s[0:]
# print("str", type(s[s[0] in '-+':])) # <class 'str'>


# functools.reduce(function, iterable[, initializer])
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

# procedure:
# running_sum =0
# c = "3" => return 3 => running_sum=3
# c= "1" => return 31 => running_sum=31
# c= "5" => return -315


def string_to_int(s):
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] in '-+':], 0)


print(string_to_int('-315'))
