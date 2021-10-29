# 12.2 is an anonymous letter constructible
# in the worst-case, the letter is not construcible or the last character of the magazine is essentially required. Therefore, the time complexity is O(m+n) where m and n are the number of characters in the letter and magazine, respectively. The space complexity is the size of the hash table constructed in the pass over the letter, i.e., O(L), where L is the number of distinct chracters appearing in the letter.
# https://leetcode.com/problems/ransom-note/

import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # compute the frequencies for all chars in letter_text
    char_frequency_for_letter = collections.Counter(letter_text)

    # check if characters in magazine_text can cover characters in char_frequency_for_letter
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
            if not char_frequency_for_letter:
                # all chracters for letter_text are matched
                return True

    # Empty char_frequency_for_letter means every char in letter_text can be covered by a character in magazine_text
    return not char_frequency_for_letter


print(is_letter_constructible_from_magazine("aa", "aab"))


# pythonic solutin that exploits collections.Counter. Note that the subtraction only kees keys with postive counts
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return (not collections.Counter(letter_text)-collections.Counter(magazine_text))


print(is_letter_constructible_from_magazine("a", "b"))


# lc brute force:
# this approach is potentially slow bc it iterates over all characters, including those that do not occur in the letter or magazine. It also makes multiple passes over both the letter and the magazine-as many passes as there are characters in the character set.
def is_letter_constructible_from_magazine(letter_text, magazine_text):

    for letter in set(letter_text):
        if letter_text.count(letter) > magazine_text.count(letter):
            return False
    return True


print(is_letter_constructible_from_magazine("a", "b"))

# lc:
# if the chracters are coded in ASCII, we could away with the hash table and use a 256 entry integer array A, with A[i] being set to the number of times the chracter i appears in the letter.


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    count = [0] * 26
    for i in range(26):
        x = chr(97 + i)
        count[i] = letter_text.count(x)
        count[i] -= magazine_text.count(x)

        if count[i] < 0:
            return False
    return True


print(is_letter_constructible_from_magazine("a", "b"))
