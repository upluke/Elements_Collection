# 6.5 Test Palindromicity
# We spand O(1) per character, so the tiem complexity is O(n), where n is the length of s

# ele:
def is_palindrome(s):
    # i moves forward, and j moves backward
    i, j = 0, len(s)-1
    while i < j:
        # i and j both skip non-alphanumeric characters
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1
    return True


print(is_palindrome('Able was I, ere I saw Elba!'))  # True
print(is_palindrome('Ray a Ray'))  # False

# init 2:


def is_palindrome(s):
    l, r = 0, len(s)-1
    while l <= r:
        if s[l].isalpha() and s[r].isalpha() or s[l] == ' ' and s[r] == ' ':
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        elif not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        else:
            return False
    return True


print(is_palindrome('Able was I, ere I saw Elba!'))  # True
print(is_palindrome('Ray a Ray'))  # False


# init 1:
def is_palindrome(s):
    # remove all punctuations
    clearn_s = helper(s)
    # compare strings
    return clearn_s == clearn_s[::-1]


def helper(dirty_s):
    new_s = ''
    for s in dirty_s:
        if s.isalpha():
            new_s += s.lower()
    return new_s


print(is_palindrome('Able was I, ere I saw Elba!'))  # True
print(is_palindrome('Ray a Ray'))  # False
