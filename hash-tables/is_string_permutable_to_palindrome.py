# 12.1 Test for palindromic permutations
# time O(n), where n is the length of the string. The space complexity is O(c), where c is the number of distinct characters appearing in the string.
import collections


def can_form_palindrome(s):
    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1

    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
    # 0, 0, 0, 0, 1, 1, 1


print(can_form_palindrome("geeksforgeeks"))
print(can_form_palindrome("geeksoskeeg"))


# https://www.geeksforgeeks.org/check-characters-given-string-can-rearranged-form-palindrome/
# # gfg (3)
# This problem can be solved in O(n) time

# where n is the number of characters in the string and O(1) space.
# The string to be palindrome all the characters should occur an even number of times if the string is of even length and at most one character can occur an odd number of times if the string length is odd. Track of the count of the characters is not required instead, it is sufficient to keep track if the counts are odd or even.
# This can be achieved by using a variable as bit vector.
# For every character in the string:
# if the bit corresponding to character is not set: //if  it is the character’s odd occurrence set the bit
# else if the bit corresponding to character is set: //if it is the character’s even occurrence toggle the bit
# This is similar to performing an XOR operation between bit vector and mask.

def canFormPalindrome(s):
    bitvector = 0
    for str in s:
        bitvector ^= 1 << ord(str)
    return bitvector == 0 or bitvector & (bitvector - 1) == 0


print(canFormPalindrome("geeksforgeeks"))
print(canFormPalindrome("geeksogeeks"))

# gfg (2)
# We can do it in O(n) time using a count array.


def canFormPalindrome(strr):
    listt = []

    for i in range(len(strr)):
        if (strr[i] in listt):
            listt.remove(strr[i])
        else:
            listt.append(strr[i])
    print(listt)
    # if character length is even
    # list is expected to be empty
    # or if character length is odd
    # listt size is expected to be 1
    if (len(strr) % 2 == 0 and len(listt) == 0 or
            (len(strr) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False


print(canFormPalindrome("geeksforgeeks"))
print(canFormPalindrome("geeksogeeks"))


# gfg (1)
# We can do it in O(n) time using a count array.
NO_OF_CHARS = 256


def canFormPalindrome(st):

    # Create a count array and initialize
    # all values as 0
    count = [0] * (NO_OF_CHARS)

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
    print(count)
    # Count odd occurring characters
    odd = 0

    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            print(count[i] & 1)
            odd = odd + 1

        if (odd > 1):
            return False

    # Return true if odd count is 0 or 1,
    return True


print(canFormPalindrome("geeksforgeeks"))
print(canFormPalindrome("geeksogeeks"))

# init:
# import collections

# def can_form_palindrome(s):
#   res=0
#   for value in collections.Counter(s).values():
#     if value==1:
#       res+=1
#   return True if res==1 else False


# print(can_form_palindrome("geeksoskeeg"))
