# 12.5 Find the nearest repeated entries in an array
# The time complexity is O(n), since we perform a constant amount of work per entry. The space complexity is O(d), where d is the number of distinct entries in the array

# Problem :Write a program that takes as input an array and finds the distance between a closest pair
# of equal entries
# Ex. ["All","Work","and","no","play","makes","for","no","word","no","fun","and","no","result"]
# Answer is 2 in this case, which is distance between second and third no.

# Input:
# [
#   "This",
#   "is",
#   "a",
#   "sentence",
#   "with",
#   "is",
#   "repeated",
#   "then",
#   "repeated"
# ]
# Output: 2
# Explanation: "repeated" (index 6) and "repeated" (index 8) are 2 positions away.

# Input:
# [
#   "This",
#   "is",
#   "a"
# ]
# Output: -1
# Explanation: There are no repeated entries.
import typing


# def find_nearest_repetition(paragraph) -> int:

#     word_to_latest_index = {}
#     nearest_repeated_distance = float('inf')
#     for i, word in enumerate(paragraph):
#         if word in word_to_latest_index:
#             latest_equal_word = word_to_latest_index[word]
#             nearest_repeated_distance = min(nearest_repeated_distance,
#                                             i - latest_equal_word)
#         word_to_latest_index[word] = i
#     return typing.cast(int, nearest_repeated_distance
#                        ) if nearest_repeated_distance != float('inf') else -1


# simplified ver:
def find_nearest_repetition(paragraph) -> int:

    hp = {}
    res = float('inf')
    for i, word in enumerate(paragraph):
        if word in hp:
            latest_equal_word = hp[word]
            res = min(res, i - latest_equal_word)
        hp[word] = i
    return typing.cast(int, res) if res != float('inf') else -1


print(find_nearest_repetition(["All", "Work", "and", "no", "play",
      "makes", "for", "no", "word", "no", "fun", "and", "no", "result"]))

print(find_nearest_repetition(
    ["This", "is", "a", "sentence", "with", "is", "repeated", "then", "repeated"]))

print(find_nearest_repetition(["This", "is", "a"]))

# init:


def find_nearest_repetition2(paragraph):
    hp = {}
    for i in range(len(paragraph)):
        hp[paragraph[i]] = hp.get(paragraph[i], [])+[i]

    indices = []
    for k, v in hp.items():
        if len(v) > 1:
            indices += v
            indices.append('_')

    if not indices:
        return -1

    res = len(paragraph)
    i = 1
    while i < len(indices):
        if indices[i] == '_':
            i += 2
        else:
            res = min(abs(indices[i]-indices[i-1]), res)
            i += 1

    return res


print(find_nearest_repetition2(["All", "Work", "and", "no", "play",
      "makes", "for", "no", "word", "no", "fun", "and", "no", "result"]))

print(find_nearest_repetition2(
    ["This", "is", "a", "sentence", "with", "is", "repeated", "then", "repeated"]))

print(find_nearest_repetition2(["This", "is", "a"]))
