# 6.6 Reverse all the words in a sentence
# Since we spend O(1) per character, the time complexity is O(n), where n is the length of s. The computation in place, i.e., the addtional space complexity is O(1)


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']
import functools


def reverse_words(s):
    # ['A', 'l', 'i', 'c', 'e', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'B', 'o', 'b']
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start+1, finish-1

    # first, reverse the whole string
    reverse_range(s, 0, len(s)-1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        if finish == len(s):
            break
        # reverses each word in the string
        reverse_range(s, start, finish-1)
        start = finish + 1
    # reverses the last word
    reverse_range(s, start, len(s)-1)


print(reverse_words(list("Alice likes Bob")))  # Bob likes Alice

# varient:
# https://leetcode.com/problems/reverse-words-in-a-string/


# lc:
# Complexity: both time and memory complexity is O(n), because we traverse all string and we create new with size O(n).
def reverseWords(self, s):
    return " ".join(s.split()[::-1])


# init:


def reverse_words(s):
    res = functools.reduce(lambda acc, curr: acc +
                           [curr], reversed(s.split(' ')), [])
    return ' '.join(res)


print(reverse_words("Alice likes Bob"))  # Bob likes Alice
