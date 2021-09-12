def h_index(citations):
    citations.sort()
    size = len(citations)
    for count, item in enumerate(citations):
        if item >= size-count:
            return size-count
    return 0


print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))  # 4
