import functools


def roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]])


print(roman_to_integer('MCMXCIV'))

# lc:
# def romanToInt(s):
#   dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#   prev=0
#   curr=0
#   total=0

#   for i in range(len(s)):
#     curr=dic[s[i]]
#     if curr > prev:
#       total=total+curr-2*prev
#     else:
#       total+=curr
#     prev=curr
#   return total
# print(romanToInt('LVIII'))
