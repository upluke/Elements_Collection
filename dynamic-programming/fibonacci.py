# def fib(n):
#   if n<2:
#     return n

#   return fib(n-1)+fib(n-2)

# print(fib(6))

# def fib(n):
#   prev, next=1, 1
#   for i in range(2, n):
#     prev,next=next,prev+next
#   return next

# print(fib(6))

# iteratively fills in the cache in a bottom-up fashion, which allows it to
# reuse cache storage to reduce the sapce complexity of the cache
# Time Complexity:O(n)
# Extra Space: O(1)
def fibonacci(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2+f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


print(fibonacci(6))
