# 6.4 Replace and remove
# https://leetcode.com/problems/find-and-replace-in-string/
# replace each 'a' by two 'd's
# delete each entry containing a 'b'
# The forward and abckward iterations each take O(n) time, so the total time complexity is O(n). No addtional space is allocated.
# exmple 1:
# 7	["c", "c", "d", "d", "a", "a", "a", "", "", "", "", "", "", ""]
# ["c", "c", "d", "d", "d", "d", "d", "d", "d", "d"]


# exmaple 2:
# 3	["d", "c", "c", "", "", ""]
# .  ["d", "c", "c"]

def replace_and_remove(size, s):
    # Forward iteration: remove 'b's and count the number of 'a's.
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # Backward iteration: replace 'a's with 'dd's starting from the end.
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    print(s)
    return final_size


print(replace_and_remove(7, ["c", "c", "d", "d",
      "a", "a", "a", "", "", "", "", "", "", ""]))
# init:
# def replace_and_remove(size, s):
#   i=0;
#   while i<len(s):
#     if s[i]=='a':
#         s[i]='d'
#         s.insert(i, 'd')
#     elif s[i]=='b':
#         s.remove('b')
#     i+=1
#   return s
# print(replace_and_remove(7, ["c", "c", "d", "d", "a", "a", "a"]    ))
