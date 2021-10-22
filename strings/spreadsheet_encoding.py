# 6.3 Compute the spreadshit column encoding
# https://leetcode.com/problems/excel-sheet-column-title/
# time: O(n)


import functools


def ss_decode_col_id(col):
    return functools.reduce(lambda result, c: result*26+ord(c)-ord('A')+1, col, 0)


print(ss_decode_col_id("ZZ"))

# lc:


def titleToNumber(columnTitle):
    res = 0
    unit = 1
    for i in range(len(columnTitle)-1, -1, -1):
        res += (ord(columnTitle[i])-64)*unit
        unit *= 26
    return res


print(titleToNumber("FXSHRXW"))

# liz:


def excel_column_to_number(column):

    total = 0
    power = 0
    for i in range(0, len(column)):
        power = len(column)-i-1
        total += (ord(column[i])-64) * (26**power)

    return total
