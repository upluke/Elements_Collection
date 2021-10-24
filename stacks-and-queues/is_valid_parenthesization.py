# 8.3 Is a string well-formed
#
# time: O(n) since for each character we perform O(1) operations
def is_well_formed(s):
    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            # unmatched right char or mismatched chars
            return False
    return not left_chars


print(is_well_formed("([]){()}"))


# liz:

def isValid(s):
    stack = []
    for letter in s:
        if ((letter == '(') or (letter == '[') or (letter == '{')):
            stack.insert(0, letter)
        else:
            if (len(stack) == 0):
                return False
            match = stack.pop(0)
            if ((letter == ')') and (match == '(')):
                continue
            if ((letter == ']') and (match == '[')):
                continue
            if ((letter == '}') and (match == '{')):
                continue
            return False
    if (len(stack) == 0):
        return True
    else:
        return False


print(is_well_formed("([]){()}"))
print(is_well_formed("[()[]{()()"))
