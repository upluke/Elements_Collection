# 15.2 Compute all mnemonics for a phone number

# since here are no more than 4 possible characters for each digit, the number of recursive calls, T(n), satisfies T(n)<=4T(n-1), where n is the number of digits in the number. This solves to T(n)= O(4^n). For the function calls that entail recursion, the time spent within the funciton, not including the recursive calls, is O(1). Each base case entails making a copy of a string and adding it to the result. Since each such string has length n, each base case takes time O(n), the time complexity is O(4^n n).

MAPPING = ("0", '1', "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            # All digits are precessed, so add partial_mnemonic to mnemonics
            # (we add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # try all possible characters for this digit
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit+1)

    mnemonics = []
    partial_mnemonic = ['0']*len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


print(phone_mnemonic("22"))


# version to understand
MAPPING = ("0", '1', "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


def phone_mnemonic(phone_number):
    def helper(digit):
        if digit == len(phone_number):
            res.append(''.join(temp))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                temp[digit] = c
                helper(digit+1)

    res = []
    temp = ['0']*len(phone_number)
    helper(0)
    return res


print(phone_mnemonic("23"))
